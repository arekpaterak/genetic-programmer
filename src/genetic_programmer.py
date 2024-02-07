from __future__ import annotations
import os
from typing import Callable

import json
import random

import numpy as np
import pandas as pd

from src.generator.generator import Generator
from src.generator.program import Program
from src.language.interpreter import MiniLanguageInterpreter

from src.library import genetic_operators, genetic_selectors

from src.task import Task


class GeneticProgrammer:
    def __init__(self, config: dict, task: Task, fitness_function: Callable) -> None:
        self.config = config
        self.params = config["genetic_programmer"]
        self.task = task
        self.fitness_function = fitness_function

        self.seed = self.params.get("seed")
        self.random = random.Random(self.seed)

        match self.params["population_init_method"]:
            case "full" | "grow" as method:
                self.generator = Generator(config["generator"], method=method)
            case "half_and_half":
                self.generators = {
                    "full": Generator(config["generator"], method="full"),
                    "grow": Generator(config["generator"], method="grow"),
                }
                self.generator = self.generators["full"]

        self.intepreter = MiniLanguageInterpreter(
            limit_of_instructions=config["interpreter"]["limit_of_instructions"]
        )

        self.tournament = genetic_selectors.Tournament(
            tournament_size=self.params["tournament_size"]
        )
        self.negative_tournament = genetic_selectors.NegativeTournament(
            tournament_size=self.params["tournament_size"]
        )

        self.population: list[Program] = []
        self.fitness_of_individuals: list[int | float] = []

        self.create_population()
        self.evaluate_fitness_of_population()

        self.results_dir = config["results_dir"]

    @classmethod
    def from_config_file(
        cls, config_file: str, fitness_function: Callable
    ) -> GeneticProgrammer:
        """
        Creates a GeneticProgrammer from a config file.
        """
        with open(config_file, "r") as f:
            config = json.load(f)

        TASK_FILE_NAME = os.path.basename(config_file)

        TASK_FILE_PATH = os.path.join(config["tasks_dir"], TASK_FILE_NAME)

        task = Task.from_json(TASK_FILE_PATH)

        return cls(config, task, fitness_function)

    def create_population(self):
        """
        Initializes the population.

        Three methods are available:
            - full
            - grow
            - half_and_half: half the initial population is constructed using full method and half is constructed using grow method
        """

        match self.params["population_init_method"]:
            case "full" | "grow":
                for _ in range(self.params["population_size"]):
                    self.population.append(self.generator.generate())
            case "half_and_half":
                for _ in range(self.params["population_size"] // 2):
                    self.population.append(self.generators["full"].generate())
                    self.population.append(self.generators["grow"].generate())

    def evaluate_fitness_of_population(self):
        """
        Evaluates the fitness of the population.
        """
        self.fitness_of_individuals = [
            self.evaluate_fitness_of_individual(individual)
            for individual in self.population
        ]

    def evaluate_fitness_of_individual(self, individual: Program) -> int | float:
        fitness = 0
        for inputs, target_outputs in zip(self.task.inputs, self.task.outputs):
            outputs = self.intepreter.run(str(individual.root), inputs)
            fitness += self.fitness_function(outputs, target_outputs)

        return fitness

    def evolve(self):
        """
        Evolves the population.
        """
        # print("Generation,\tBest Fitness,\tAverage Fitness,\tBest Individual")

        stats = []

        max_generations = self.params["max_generations"]
        for generation in range(max_generations):
            for _ in range(self.params["changes_per_generation"]):
                if self.random.random() < self.params["crossover_probability"]:
                    parent_1 = self.tournament.select(
                        self.population, self.fitness_of_individuals
                    )
                    parent_2 = self.tournament.select(
                        self.population, self.fitness_of_individuals
                    )
                    # new_individual = genetic_operators.crossover(parent_1, parent_2)
                    new_individual = genetic_operators.crossover(parent_1, parent_2)
                else:
                    parent = self.tournament.select(
                        self.population, self.fitness_of_individuals
                    )
                    new_individual = genetic_operators.mutate(parent, self.generator)
                index_of_individual_to_replace = self.negative_tournament.select_index(
                    self.population, self.fitness_of_individuals
                )

                self.population[index_of_individual_to_replace] = new_individual
                fitness_of_new_individual = self.evaluate_fitness_of_individual(
                    new_individual
                )
                self.fitness_of_individuals[
                    index_of_individual_to_replace
                ] = fitness_of_new_individual

            self.log_generation(generation)

            stats.append(
                [
                    generation,
                    self.best_fitness,
                    self.average_fitness,
                    str(self.best_individual).replace("\n", " "),
                ]
            )

            # early stopping
            if self.best_fitness == 0:
                print("Early stopping.")
                break

        # create folder if it doesn't exist
        os.makedirs(f"{self.results_dir}/{self.task.name}", exist_ok=True)
        with open(f"{self.results_dir}/{self.task.name}/best_individual.txt", "w") as f:
            f.write(str(self.best_individual))

        df = pd.DataFrame(
            stats,
            columns=[
                "Generation",
                "Best Fitness",
                "Average Fitness",
                "Best Individual",
            ],
        )

        df.to_csv(f"{self.results_dir}/{self.task.name}/generations.csv", index=False)

        # save config
        with open(f"{self.results_dir}/{self.task.name}/config.json", "w") as f:
            json.dump(self.config, f, indent=4)

    @property
    def best_fitness(self) -> int | float:
        return max(self.fitness_of_individuals)

    @property
    def average_fitness(self) -> float:
        return np.mean(self.fitness_of_individuals)

    @property
    def best_individual(self) -> Program:
        return self.population[np.argmax(self.fitness_of_individuals)]

    def log_generation(self, generation):
        best_individual = str(self.best_individual).replace("\n", " ")
        print(
            f"Generation: {generation}, Best Fitness: {self.best_fitness}, Average Fitness: {self.average_fitness}, Best Individual: {best_individual}, Best output for input {self.task.inputs[0]}: {self.intepreter.run(str(self.best_individual.root), self.task.inputs[0])}"
        )

import json
import os


from src.genetic_programmer import GeneticProgrammer
from src.library import fitness_functions, genetic_operators, genetic_selectors
from src.task import Task


def test_mutate():
    CONFIG_FILE_PATH = "configs/1_1_A.json"

    fitness_function = fitness_functions.value_present

    genetic_programmer = GeneticProgrammer.from_config_file(
        CONFIG_FILE_PATH, fitness_function
    )

    # # test mutation
    print("Mutation")
    program = genetic_programmer.population[0]
    print(f"program:\n{program}\n")

    child = genetic_operators.mutate(program, genetic_programmer.generator)

    print(f"program:\n{child}\n")


if __name__ == "__main__":
    test_mutate()

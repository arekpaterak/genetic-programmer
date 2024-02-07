from abc import ABC, abstractmethod

import random

from src.generator.program import Program


class BaseSelector(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def select(self, population):
        pass


class Tournament(BaseSelector):
    def __init__(self, tournament_size: int) -> None:
        super().__init__()
        self.tournament_size = tournament_size
        self.random = random.Random()

    def select(self, population, fitness_of_individuals) -> Program:
        return population[self.select_index(population, fitness_of_individuals)]

    def select_index(self, population, fitness_of_individuals) -> int:
        index_of_selected = self.random.randint(0, len(population) - 1)
        for _ in range(self.tournament_size):
            index = self.random.randint(0, len(population) - 1)
            if (
                fitness_of_individuals[index]
                > fitness_of_individuals[index_of_selected]
            ):
                index_of_selected = index
        return index_of_selected


class NegativeTournament(Tournament):
    def __init__(self, tournament_size) -> None:
        super().__init__(tournament_size)

    def select_index(self, population, fitness_of_individuals) -> int:
        index_of_selected = self.random.randint(0, len(population) - 1)
        for _ in range(self.tournament_size):
            index = self.random.randint(0, len(population) - 1)
            if (
                fitness_of_individuals[index]
                < fitness_of_individuals[index_of_selected]
            ):
                index_of_selected = index
        return index_of_selected

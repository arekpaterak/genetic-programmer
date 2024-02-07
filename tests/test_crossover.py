import json
import os


from src.genetic_programmer import GeneticProgrammer
from src.library import fitness_functions, genetic_operators, genetic_selectors
from src.task import Task


def test_crossover():
    CONFIG_FILE_PATH = "configs/1_1_A.json"

    fitness_function = fitness_functions.value_present

    genetic_programmer = GeneticProgrammer.from_config_file(
        CONFIG_FILE_PATH, fitness_function
    )

    # test crossover
    print("Crossover")
    program1 = genetic_programmer.population[0]
    program2 = genetic_programmer.population[1]

    print(f"program1:\n{program1}\n")
    print(f"program2:\n{program2}\n")

    child = genetic_operators.crossover(program1, program2)

    print(f"child:\n{child}\n")


if __name__ == "__main__":
    test_crossover()

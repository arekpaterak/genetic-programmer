import json
import os
import sys


from src.genetic_programmer import GeneticProgrammer
from src.library import fitness_functions, genetic_operators, genetic_selectors
from src.task import Task

from tests.test_crossover import test_crossover
from tests.test_mutate import test_mutate
from tests.test_serialize import test_serialize

CONFIGS_DIR = "configs"


def main():
    if len(sys.argv) > 1:
        CONFIG_FILE_PATH = os.path.join(CONFIGS_DIR, sys.argv[1])
    else:
        CONFIG_FILE_PATH = os.path.join(CONFIGS_DIR, "1_3_A.json")

    fitness_function = fitness_functions.single_value

    genetic_programmer = GeneticProgrammer.from_config_file(
        CONFIG_FILE_PATH, fitness_function
    )

    genetic_programmer.evolve()


if __name__ == "__main__":
    main()

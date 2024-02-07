import json
import os


from src.genetic_programmer import GeneticProgrammer
from src.library import fitness_functions, genetic_operators, genetic_selectors
from src.task import Task
from src.generator.program import Program


def test_serialize():
    CONFIG_FILE_PATH = "configs/1_1_A.json"

    fitness_function = fitness_functions.value_present

    genetic_programmer = GeneticProgrammer.from_config_file(
        CONFIG_FILE_PATH, fitness_function
    )

    print("Serialization")
    program = genetic_programmer.population[0]
    print(f"program:\n{program}\n")

    program.serialise("test_serialise.pkl")

    deserialised_program = Program.deserialise("test_serialise.pkl")

    print(f"program:\n{program}\n")


if __name__ == "__main__":
    test_serialize()

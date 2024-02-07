import json
import os
import sys


from src.language.interpreter import MiniLanguageInterpreter


def main():
    # program_path = "results/boolean_regression/k2_xor/best_individual.txt"
    program_path = "results/basic_tests/1_3_A/best_individual.txt"

    with open(program_path, "r") as file:
        program = file.read()

    interpreter = MiniLanguageInterpreter()
    output = interpreter.run(program, [0, 0])

    print(output)


if __name__ == "__main__":
    main()

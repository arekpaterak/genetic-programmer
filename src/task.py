from __future__ import annotations

from dataclasses import dataclass
import json
import os

Input = list[int | float | bool]
Output = list[int | float | bool]


@dataclass
class Task:
    """
    A task is a problem that Genetic Programmer tries to solve.
    """

    # test_cases: list[tuple[Input, Output]]
    name: str
    inputs: list[Input]
    outputs: list[Output]

    @classmethod
    def from_json(cls, path: str) -> Task:
        """
        Creates a Task from a json file.
        """
        name = os.path.basename(path).replace(".json", "")

        with open(path, "r") as f:
            test_cases = json.load(f)
            inputs = [
                inputs if (inputs := test_case["inputs"]) else []
                for test_case in test_cases
            ]
            outputs = [
                outputs if (outputs := test_case["outputs"]) else []
                for test_case in test_cases
            ]
        return cls(name, inputs, outputs)

    def __str__(self) -> str:
        return f"Task(inputs={self.inputs}, outputs={self.outputs})"


if __name__ == "__main__":
    task = Task.from_json("tasks/basic_tests/1_1_A.json")
    print(task)

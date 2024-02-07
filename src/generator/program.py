from __future__ import annotations

from dataclasses import dataclass
import pickle

from src.generator.node import Node


@dataclass
class Program:
    root: Node

    def serialise(self, path) -> None:
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialise(cls, path) -> Program:
        with open(path, "rb") as f:
            return pickle.load(f)

    def __str__(self) -> str:
        return str(self.root)

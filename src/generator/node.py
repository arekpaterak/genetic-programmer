from __future__ import annotations

from dataclasses import dataclass, field
import pickle
from enum import Enum


class NodeType(Enum):
    PROGRAM = "program"
    ASSIGNMENT = "assignment"
    LOOP = "loop"
    CONDITIONAL = "conditional"
    BLOCK = "block"
    INPUT = "input"
    OUTPUT = "output"
    LOGIC_EXPRESSION = "logic_expression"
    NEGATION = "negation"
    NUMERICAL_EXPRESSION = "numerical_expression"
    MINUS = "minus"
    RELATIONAL_EXPRESSION = "relational_expression"
    VAR_ID = "var_id"
    BOOL = "bool"
    INT = "int"
    FLOAT = "float"
    OPERATOR = "operator"


@dataclass
class Node:
    type_of_node: NodeType
    children: list[Node] = field(default_factory=list)
    value: str | int | float | bool | None = None

    def is_terminal(self) -> bool:
        return len(self.children) == 0

    def is_equivalent(self, other: Node) -> bool:
        match self.type_of_node:
            case NodeType.PROGRAM:
                raise Exception("No need to compare programs")

            case NodeType.ASSIGNMENT | NodeType.LOOP | NodeType.CONDITIONAL | NodeType.BLOCK | NodeType.INPUT | NodeType.OUTPUT:
                return other.type_of_node in [
                    NodeType.ASSIGNMENT,
                    NodeType.LOOP,
                    NodeType.CONDITIONAL,
                    NodeType.BLOCK,
                    NodeType.INPUT,
                    NodeType.OUTPUT,
                ]

            case NodeType.LOGIC_EXPRESSION | NodeType.NEGATION | NodeType.NUMERICAL_EXPRESSION | NodeType.MINUS | NodeType.RELATIONAL_EXPRESSION:
                return other.type_of_node in [
                    NodeType.LOGIC_EXPRESSION,
                    NodeType.NEGATION,
                    NodeType.NUMERICAL_EXPRESSION,
                    NodeType.MINUS,
                    NodeType.RELATIONAL_EXPRESSION,
                ]

            case NodeType.BOOL | NodeType.INT | NodeType.FLOAT:
                return other.type_of_node in [
                    NodeType.BOOL,
                    NodeType.INT,
                    NodeType.FLOAT,
                ]

            case NodeType.VAR_ID:
                return other.type_of_node == NodeType.VAR_ID

            case NodeType.OPERATOR:
                return other.type_of_node == NodeType.OPERATOR

            case _:
                raise Exception(f"Unknown node type: {self.type_of_node}")

    def __str__(self) -> str:
        match self.type_of_node:
            case NodeType.PROGRAM:
                statements = self.children
                return "\n".join(map(str, statements))

            case NodeType.ASSIGNMENT:
                var_id, expression = self.children
                return f"{var_id} <- {expression};"

            case NodeType.LOOP:
                condition, block = self.children
                return f"while ({condition}) {block};"

            case NodeType.CONDITIONAL:
                if len(self.children) == 2:
                    condition, block = self.children
                    return f"if ({condition}) {block};"
                else:
                    condition, block, else_block = self.children
                    return f"if ({condition}) {block} else {else_block};"

            case NodeType.BLOCK:
                statements = self.children
                return "{\n  " + "\n  ".join(map(str, statements)) + "\n}"

            case NodeType.INPUT:
                var_id = self.children[0]
                assert var_id.type_of_node == NodeType.VAR_ID, var_id
                return f"{var_id} <- input;"

            case NodeType.OUTPUT:
                expression = self.children[0]
                return f"output <- {expression};"

            case NodeType.LOGIC_EXPRESSION:
                return " ".join(map(str, self.children))

            case NodeType.NEGATION:
                return f"(not {self.children[0]})"

            case NodeType.NUMERICAL_EXPRESSION:
                return " ".join(map(str, self.children))

            case NodeType.MINUS:
                return f"(- {self.children[0]})"

            case NodeType.RELATIONAL_EXPRESSION:
                left, operator, right = self.children
                return f"{left} {operator} {right}"

            case NodeType.VAR_ID:
                name = self.value
                return str(name)

            case NodeType.BOOL:
                value = self.value
                return str(value)

            case NodeType.INT:
                value = self.value
                return str(value)

            case NodeType.FLOAT:
                value = self.value
                return str(value)

            case NodeType.OPERATOR:
                value = self.value
                return str(value)

            case _:
                raise Exception(f"Unknown node type: {self.type_of_node}")

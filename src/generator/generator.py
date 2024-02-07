from __future__ import annotations

from functools import partial
import random
import json

from src.generator.node import *
from src.generator.program import Program


class Generator:
    """
    Generates a program according to the prepared grammar of MiniLanguage and restricted by the given parameters.
    """

    def __init__(self, params: dict, method: str = None) -> None:
        self.params = params

        self.seed = self.params.get("seed")
        self.random = random.Random(self.seed)

        self.use_floats = params.get("use_floats", False)

        if method is None:
            self.full_method = params.get("full_method", True)
        else:
            self.full_method = method == "full"

        self.highest_variable_id = 0
        self.current_expression_size = 0
        self.current_program_depth = 1
        # self.current_program_width = 0

    @classmethod
    def from_config_file(cls, config_file: str) -> Generator:
        """
        Creates a Generator from a config file.
        """
        with open(config_file, "r") as f:
            config = json.load(f)
        return cls(config["generator"])

    def reset(self) -> None:
        self.highest_variable_id = 0
        self.current_expression_size = 0
        self.current_program_depth = 1
        # self.current_program_width = 0

    def generate(self) -> Program:
        """
        Generates a program.
        """
        return Program(self.generate_program())

    def generate_program(self) -> Node:
        self.reset()

        statements = []
        # if self.full_method:
        #     width = self.params.get("max_program_width")
        #     for _ in range(width):
        #         statement = self.generate_statement()
        #         statements.append(statement)
        #         self.current_program_depth = 1
        # else:
        width = self.random.randint(1, self.params.get("max_program_width"))
        for _ in range(width):
            statement = self.generate_statement()
            statements.append(statement)
            self.current_program_depth = 1

        return Node(NodeType.PROGRAM, statements)

    def generate_statement(self) -> Node:
        choices = []
        if self.full_method:
            if self.current_program_depth < self.params.get("max_program_depth"):
                choices += [self.generate_conditional]
                if self.params.get("use_loops", True):
                    choices.append(self.generate_loop)
            else:
                choices += [
                    self.generate_assignment,
                    self.generate_input,
                    self.generate_output,
                ]
        else:
            choices += [
                self.generate_assignment,
                self.generate_input,
                self.generate_output,
            ]
            if self.current_program_depth < self.params.get("max_program_depth"):
                choices += [self.generate_conditional]
                if self.params.get("use_loops", True):
                    choices.append(self.generate_loop)

        return self.random.choice(choices)()

    def generate_assignment(self) -> Node:
        var_id = self.generate_var_id()
        expression = self.generate_expression()
        return Node(NodeType.ASSIGNMENT, [var_id, expression])

    def generate_loop(self) -> Node:
        self.current_program_depth += 1

        condition = self.generate_condition()
        block = self.generate_block()
        return Node(NodeType.LOOP, [condition, block])

    def generate_conditional(self) -> Node:
        self.current_program_depth += 1

        condition = self.generate_condition()
        block = self.generate_block()
        if self.random.choice([True, False]):
            return Node(NodeType.CONDITIONAL, [condition, block])
        else:
            else_block = self.generate_block()
            return Node(NodeType.CONDITIONAL, [condition, block, else_block])

    def generate_block(self) -> Node:
        statements = []
        # if self.full_method:
        #     width = self.params.get("max_block_width")
        #     for _ in range(width):
        #         statement = self.generate_statement()
        #         statements.append(statement)
        # else:
        width = self.random.randint(1, self.params.get("max_block_width"))
        for _ in range(width):
            statement = self.generate_statement()
            statements.append(statement)

        return Node(NodeType.BLOCK, statements)

    def generate_input(self) -> Node:
        self.highest_variable_id += 1
        var_id = self.generate_var_id()

        assert var_id.type_of_node == NodeType.VAR_ID, var_id

        return Node(NodeType.INPUT, [var_id])

    def generate_output(self) -> Node:
        expression = self.generate_expression()

        return Node(NodeType.OUTPUT, [expression])

    def generate_expression(self) -> Node:
        self.current_expression_size = 0

        choices = [
            self.generate_numerical_expression,
            self.generate_logic_expression,
        ]

        return self.random.choice(choices)()

    def generate_condition(self) -> Node:
        self.current_expression_size = 0
        return self.generate_logic_expression()

    def generate_logic_expression(self) -> Node:
        # if self.full_method:
        #     expr = [self.generate_logic_literal()]
        #     while self.current_expression_size < self.params.get("max_expression_size"):
        #         operation = self.random.choice(["and", "or"])
        #         expr += [operation]
        #         expr += [self.generate_logic_literal()]
        # else:
        expr = [self.generate_logic_literal()]
        while self.current_expression_size < self.params.get("max_expression_size"):
            operation = self.random.choice(["and", "or", None])
            if operation is None:
                break
            else:
                operation = Node(NodeType.OPERATOR, value=operation)
                expr += [operation]
                expr += [self.generate_logic_literal()]

        return Node(NodeType.LOGIC_EXPRESSION, expr)

    def generate_logic_literal(self, negation=True) -> Node:
        self.current_expression_size += 1

        choices = [
            self.generate_bool,
            self.generate_id,
        ]

        if negation:
            choices.append(self.generate_negation)

        if self.current_expression_size < self.params.get("max_expression_size"):
            choices.append(self.generate_relational_expression)

        return self.random.choice(choices)()

    def generate_negation(self) -> Node:
        return Node(NodeType.NEGATION, [self.generate_logic_literal(negation=False)])

    def generate_relational_expression(self) -> Node:
        numerical_expression1 = self.generate_numerical_expression()
        numerical_expression2 = self.generate_numerical_expression()

        operator = self.random.choice(["==", "!=", "<", ">", "<=", ">="])
        operator = Node(NodeType.OPERATOR, value=operator)

        return Node(
            NodeType.RELATIONAL_EXPRESSION,
            [numerical_expression1, operator, numerical_expression2],
        )

    def generate_numerical_expression(self) -> Node:
        # if self.full_method:
        #     expr = [self.generate_numerical_literal()]
        #     while self.current_expression_size < self.params.get("max_expression_size"):
        #         operation = self.random.choice(["*", "/", "+", "-"])
        #         expr += [operation]
        #         expr += [self.generate_numerical_literal()]

        # else:
        expr = [self.generate_numerical_literal()]
        while self.current_expression_size < self.params.get("max_expression_size"):
            operation = self.random.choice(["*", "/", "+", "-", None])
            if operation is None:
                break
            else:
                operation = Node(NodeType.OPERATOR, value=operation)
                expr += [operation]
                expr += [self.generate_numerical_literal()]

        return Node(NodeType.NUMERICAL_EXPRESSION, expr)

    def generate_numerical_literal(self, minus=True) -> Node:
        self.current_expression_size += 1

        choices = [
            self.generate_id,
            self.generate_int,
        ]
        if self.use_floats:
            choices.append(self.generate_float)
        if minus:
            choices.append(self.generate_minus)

        return self.random.choice(choices)()

    def generate_minus(self) -> Node:
        return Node(NodeType.MINUS, [self.generate_numerical_literal(minus=False)])

    def generate_id(self) -> Node:
        return self.generate_var_id()

    def generate_var_id(self) -> Node:
        name = f"VAR_{random.randint(0, self.highest_variable_id)}"
        return Node(NodeType.VAR_ID, value=name)

    def generate_bool(self) -> Node:
        value = self.random.choice([True, False])
        return Node(NodeType.BOOL, value=value)

    def generate_int(self) -> Node:
        value = self.random.randint(
            self.params.get("int_min"), self.params.get("int_max")
        )
        return Node(NodeType.INT, value=value)

    def generate_float(self) -> Node:
        value = self.random.uniform(
            self.params.get("float_min"), self.params.get("float_max")
        )
        return Node(NodeType.FLOAT, value=value)

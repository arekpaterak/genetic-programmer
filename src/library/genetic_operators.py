from src.generator.program import Program
from src.generator.node import Node
from src.generator.generator import Generator

import random
import copy


def naive_crossover(parent1: Program, parent2: Program) -> Program:
    def random_node(nodes) -> Node:
        return random.choice(nodes)

    child = copy.deepcopy(parent1)
    parent2 = copy.deepcopy(parent2)

    current_root1 = child.root
    current_root2 = parent2.root

    node1 = random_node(current_root1.children)
    node2 = random_node(current_root2.children)

    current_root1.children[current_root1.children.index(node1)] = node2

    assert child is not parent1

    return parent1


def crossover(parent1: Program, parent2: Program, max_iterations: int = 100) -> Program:
    def random_node(nodes) -> Node:
        return random.choice(nodes)

    child = copy.deepcopy(parent1)
    parent2 = copy.deepcopy(parent2)

    current_root1 = child.root
    current_root2 = parent2.root

    iteration = 0
    while iteration < max_iterations:
        iteration += 1

        node1 = random_node(current_root1.children)
        node2 = random_node(current_root2.children)

        if node1.is_terminal() or node2.is_terminal():
            break

        if not node1.is_equivalent(node2) or random.random() < 0.1:
            if random.random() < 0.5:
                continue
            else:
                current_root1 = node1
                current_root2 = node2
        else:
            break

    if node1.is_equivalent(node2):
        current_root1.children[current_root1.children.index(node1)] = node2

    assert child is not parent1

    return child


def mutate(individual: Program, generator: Generator) -> Program:
    """
    Subtree mutation.
    """
    temp = generator.generate()

    return crossover(individual, temp)

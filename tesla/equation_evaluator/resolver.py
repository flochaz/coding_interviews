from abc import ABC, abstractmethod

import numpy as np

from equation_evaluator.equation import Equation


class Resolver(ABC):

    def __init__(self, file_path):
        if file_path:
            self.equations = equations_from_file(file_path)
        super(Resolver, self).__init__()

    @abstractmethod
    def resolve(self):
        pass


def equations_from_file(file_path):
    equations = []
    with open(file_path, mode='r') as file:
        for line in file:
            equations.append(Equation(line))

    return equations
import os
from unittest import TestCase

import collections

from equation_evaluator.numpy_matrix_resolver import NumpyMatrixResolver as Resolver


class TestNumpyMatrixResolver(TestCase):
    def test_matrixes_from_equations(self):
        with open(os.path.join(os.path.dirname(__file__), "data", "test_data_from_tesla.txt"), "r") as test_data:
            matrix = Resolver(os.path.join(os.path.dirname(__file__), "data", "test_data_from_tesla.txt"))
        self.assertEqual(['random', 'offset', 'origin', 'location'], matrix.variables)
        self.assertEqual([[1, -1, 0, 0], [0, 1, 1, -1], [0, 0, -1, 0], [-1, 0, 0, 0]], matrix.A)
        self.assertEqual([-5, -1, -8, -2], matrix.B)


    def test_resolve_using_np(self):
        result_test_data_from_tesla = collections.OrderedDict()
        result_test_data_from_tesla['random'] = 2
        result_test_data_from_tesla['offset'] = 7
        result_test_data_from_tesla['origin'] = 8
        result_test_data_from_tesla['location'] = 16

        with open(os.path.join(os.path.dirname(__file__), "data", "test_data_from_tesla.txt"), "r") as test_data:
            resolver = Resolver(os.path.join(os.path.dirname(__file__), "data", "test_data_from_tesla.txt"))

        solution = resolver.resolve()
        i = 0
        for key, value in result_test_data_from_tesla.items():
            print("{variable} = {value}".format(variable=key, value=value))
            self.assertEqual(value, solution[i])
            i += 1


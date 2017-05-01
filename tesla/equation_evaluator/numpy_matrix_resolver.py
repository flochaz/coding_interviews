import numpy as np

from equation_evaluator.resolver import Resolver


def matrixes_from_equations(equations):
    variables_name = []
    coefs = []
    constants = []

    for equation in equations:
        for variable in equation.right_hand_side.variables.values():
            if variable.name not in variables_name:
                variables_name.append(variable.name)
        if equation.left_hand_side.name not in variables_name:
            variables_name.append(equation.left_hand_side.name)

    for equation in equations:
        eq_coefs, eq_const = equation.get_array_of_coefs(variables_name)
        coefs.append(eq_coefs)
        constants.append(eq_const)

    return variables_name, coefs, constants


class NumpyMatrixResolver(Resolver):

    def __init__(self, file_path):
        super().__init__(file_path)
        if self.equations:
            self.variables, self.A, self.B = matrixes_from_equations(self.equations)

    def resolve(self):
        A = np.array(self.A)
        B = np.array(self.B)

        return np.linalg.solve(A, B)

from unittest import TestCase

from equation_evaluator.equation import Equation, Variable, extract_LHS_and_RHS


class TestEquation(TestCase):
    def setUp(self):
        self.equation = Equation()

    def test_str(self):
        string_eq = "a = 1"
        eq = Equation(string_eq)
        self.assertEqual(string_eq, str(eq))

    def test_extract_LHS_and_RHS_easy_case(self):
        actual_LHS, actual_RHS = extract_LHS_and_RHS("a = 1")
        self.assertEqual("a", actual_LHS.name)
        self.assertEqual(len(actual_RHS.variables), 0)
        self.assertEqual(actual_RHS.integer, 1)

    def test_extract_LHS_and_RHS_harder_case(self):
        actual_LHS, actual_RHS = extract_LHS_and_RHS("my_variable = test1 + 1 +2+  3+ test2+test3")
        self.assertEqual("my_variable", actual_LHS.name)
        self.assertEqual(len(actual_RHS.variables), 3)
        self.assertEqual(actual_RHS.integer, 6)

    def test_resolv_integers_only(self):
        self.equation.right_hand_side.add_element(1)
        self.equation.right_hand_side.add_element(3)
        self.equation.right_hand_side.add_element(5)
        actual_result = self.equation.resolve()

        self.assertEqual(actual_result.value, 9)

    def test_resolv_variable_only(self):
        self.equation.right_hand_side.add_element(Variable("b", 1))
        actual_result = self.equation.resolve()

        self.assertEqual(actual_result.value, 1)

    def test_resolv_variable_only_with_coef(self):
        self.equation.right_hand_side.add_element(Variable("b", 1))
        self.equation.right_hand_side.add_element(Variable("b", 1))
        actual_result = self.equation.resolve()

        self.assertEqual(actual_result.value, 2)

    def test_resolv_integers_with_resolved_variables(self):
        self.equation.left_hand_side = Variable("test")
        self.equation.right_hand_side.add_element(Variable(name="a", value=1))
        self.equation.right_hand_side.add_element(Variable(name="b", value=2))
        self.equation.right_hand_side.add_element(5)
        actual_result = self.equation.resolve()

        self.assertEqual(actual_result.value, 8)

    def test_resolv_integers_with_unresolved_variables(self):
        self.equation.left_hand_side = Variable("test")
        self.equation.right_hand_side.add_element(Variable("a"))
        self.equation.right_hand_side.add_element(Variable("b", 2))
        self.equation.right_hand_side.add_element(5)
        with self.assertRaises(Exception):
            self.equation.resolve()


    def test_get_array_of_coefs(self):
        self.equation.left_hand_side = Variable("c", coef=-1)
        self.equation.right_hand_side.add_element(Variable("a"))
        self.equation.right_hand_side.add_element(Variable("b"))
        self.equation.right_hand_side.add_element(5)
        variables_name = ['a', 'b', 'c']
        expected_result = [1,1,-1]
        coefs, constant = self.equation.get_array_of_coefs(variables_name)
        self.assertEqual(expected_result, coefs)
        self.assertEqual(-5, constant)




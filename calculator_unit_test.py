"""module
"""

import unittest
import math
from postfix_calculator import PostfixCalculator

class CalculatorTestCase(unittest.TestCase):
    """Unit test for the postfix calculator
    """

    calculator = PostfixCalculator()

    def evaluate(self, expression):
        """A Method
        """
        return self.calculator.evaluate_postfix_expression(
            self.calculator.convert_infix_to_postfix(expression))

    def test_addition(self):
        """A Method
        """
        self.assertEqual(self.evaluate("12 + 30"), 12 + 30)

    def test_multiplication(self):
        """A Method
        """
        self.assertEqual(self.evaluate("12 * 30"), 12 * 30)

    def test_modulo(self):
        """A Method
        """
        self.assertEqual(self.evaluate("1294 % 9"), 1294 % 9)

    def test_sqrt(self):
        """A Method
        """
        self.assertEqual(self.evaluate("sqrt ( 21532 )"), math.sqrt(21532))

    def test_sin(self):
        """A Method
        """
        self.assertEqual(self.evaluate("sin ( 0 )"), math.sin(0))

    def test_asin(self):
        """A Method
        """
        self.assertEqual(self.evaluate("asin ( 0 )"), math.asin(0))

    def test_pi(self):
        """A Method
        """
        self.assertEqual(self.evaluate("pi"), math.pi)

    def test_e(self):
        """A Method
        """
        self.assertEqual(self.evaluate("e"), math.e)

    def test_all_operators(self):
        """A Method
        """
        self.assertEqual(self.evaluate("1294 % 9 + 12 - 30 * 9 / 10 + 0.5 ^ 2 * 44"),
                         1294 % 9 + 12 - 30 * 9 / 10 + 0.5 ** 2 * 44)

    def test_breackets(self):
        """A Method
        """
        self.assertEqual(self.evaluate("( 328 * ( e ^ ( pi - e ) - ( 29 * ( 50 + ( 0 - 30 ) ) ) )"),
                         (328 * (math.e ** (math.pi - math.e) - (29 * (50 + (0 - 30))))))

    def test_faculty(self):
        """A Method
        """
        self.assertEqual(self.evaluate("fac ( 5 )"), 120)

    def test_faculty_negative(self):
        """A Method
        """
        self.assertRaises(Exception, self.evaluate, "fac ( -1 )")

if __name__ == '__main__':
    unittest.main()

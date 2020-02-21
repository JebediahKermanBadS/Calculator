"""Module for the PostifxOperator class
"""

import operator
import math

class PostfixOperator():
    """A class for the basic math operators
    """

    predance = 0
    associativity = 0
    function = 0

    def __init__(self, predance, associativity, function):
        self.predance = predance
        self.associativity = associativity
        self.function = function

class PostfixFunction():
    """A class for a math function. e.g. sin(a)
    """

    parameter_count = 0
    function = 0

    def __init__(self, parameter_count=0, function=0):
        self.parameter_count = parameter_count
        self.function = function

    @staticmethod
    def fac(_n):
        """Calculate the faculty of a number n
        Arguments:
            n {int} -- The number to calculate
        Raises:
            Exception: If n < 0
        Returns:
            int -- The faculty
        """
        if _n < 0:
            raise Exception(f"To calculate the faculty n should be greather than 0. It was {_n}")

        result = 1
        for i in range(2, _n + 1):
            result *= i
        return result

class PostfixCalculator():
    """The PostfixCalulator class
    """

    operatorList = {
        '+': PostfixOperator(2, 0, lambda a, b: a + b),
        '-': PostfixOperator(2, 0, operator.sub),
        '*': PostfixOperator(3, 0, operator.mul),
        '/': PostfixOperator(3, 0, operator.itruediv),
        '%': PostfixOperator(3, 0, operator.mod),
        '^': PostfixOperator(4, 1, operator.ipow),
    }

    functionList = {
        'sqrt': PostfixFunction(1, math.sqrt),
        'sin' : PostfixFunction(1, math.sin),
        'cos' : PostfixFunction(1, math.cos),
        'tan' : PostfixFunction(1, math.tan),
        'acos': PostfixFunction(1, math.acos),
        'asin': PostfixFunction(1, math.asin),
        'atan': PostfixFunction(1, math.atan),
        'rad' : PostfixFunction(1, math.radians),
        'deg' : PostfixFunction(1, math.degrees),
        'fac' : PostfixFunction(1, PostfixFunction.fac),
        'min' : PostfixFunction(2, min),
        'max' : PostfixFunction(2, max),
    }

    constValueList = {
        'pi': math.pi,
        'e': math.e
    }

    def check_token_is_operator(self, token):
        """A Method
        """
        return self.operatorList.keys().__contains__(token)

    def check_token_is_function(self, token):
        """A Method
        """
        return self.functionList.keys().__contains__(token)

    def check_token_is_const_value(self, token):
        """A Method
        """
        return self.constValueList.keys().__contains__(token)

    def get_operator_precedance(self, token):
        """A Method
        """
        if token == '(':
            return 0
        return self.operatorList[token].predance

    def get_operator_associatvity(self, token):
        """A Method
        """
        return self.operatorList[token].associativity

    def convert_infix_to_postfix(self, expression):
        """A Method
        """
        operator_stack = []
        output_queue = []

        tokens = str.split(expression.lower(), " ")

        for token in tokens:
            if self.check_token_is_operator(token):
                while len(operator_stack) > 0 and (
                         self.check_token_is_function(operator_stack[-1])
                         or (self.get_operator_precedance(operator_stack[-1]) > self.get_operator_precedance(token))
                         or (self.get_operator_precedance(operator_stack[-1]) == self.get_operator_precedance(token) and self.get_operator_associatvity(token) == 0)
                         and (operator_stack[-1] != '(')
                    ):
                    output_queue.append(operator_stack.pop())

                operator_stack.append(token)

            elif self.check_token_is_function(token):
                operator_stack.append(token)

            elif self.check_token_is_const_value(token):
                output_queue.append(self.constValueList[token])

            elif token == '(':
                operator_stack.append(token)

            elif token == ')':
                while operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())

                if operator_stack[-1] == '(':
                    operator_stack.pop()

            else:
                if token.isdigit():
                    output_queue.append(int(token))
                else:
                    output_queue.append(float(token))

        while len(operator_stack) > 0:
            output_queue.append(operator_stack.pop())

        return output_queue

    def evaluate_postfix_expression(self, expression):
        """A Method
        """
        stack = []

        for token in expression:
            if self.check_token_is_operator(token):
                _n2 = stack.pop()
                _n1 = stack.pop()

                operator_func = self.operatorList[token].function

                stack.append(operator_func(_n1, _n2))

            elif self.check_token_is_function(token):

                result = 0
                parameter_count = self.functionList[token].parameter_count
                operator_func = self.functionList[token].function

                _n = []
                for _ in range(0, parameter_count):
                    _n.insert(0, stack.pop())

                if parameter_count == 1:
                    result = operator_func(_n[0])
                elif parameter_count == 2:
                    result = operator_func(_n[0], _n[1])

                stack.append(result)

            else:
                stack.append(token)

        return stack[0]

if __name__ == "__main__":
    pass

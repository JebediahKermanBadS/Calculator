"""Module description
"""

from postfix_calculator import PostfixCalculator

def main():
    """Main method
    """

    calculator = PostfixCalculator()

    while True:
        infix_expression = input("Enter your calculation: ")

        if infix_expression[0] == "&":
            break

        for _c in calculator.operatorList:
            infix_expression = infix_expression.replace(_c, f" {_c} ")
        for _c in calculator.functionList:
            infix_expression = infix_expression.replace(_c, f" {_c} ")

        infix_expression = infix_expression.replace("(", " ( ")
        infix_expression = infix_expression.replace(")", " ) ")
        while infix_expression.__contains__("  "):
            infix_expression = infix_expression.replace("  ", " ")

        if infix_expression.endswith(" "):
            infix_expression = infix_expression[:-1]
        if infix_expression.startswith(" "):
            infix_expression = infix_expression[1:]

        postfix_expression = calculator.convert_infix_to_postfix(infix_expression)

        print(f" = {calculator.evaluate_postfix_expression(postfix_expression)}")

if __name__ == "__main__":
    main()

from sympy import symbols, Eq, solve, diff, integrate, sympify
from math_parser import parse_text
import re

def preprocess_expression(expression):
    """
    Preprocesses the mathematical expression to make it Python-evaluable.
    Adds implicit multiplication between numbers and variables (e.g., '3x' -> '3*x').
    """
    # Add multiplication where needed (e.g., between a number and a variable or parentheses)
    expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)  # 3x -> 3*x
    expression = re.sub(r'(\d)(\()', r'\1*(', expression)         # 3(x) -> 3*(x)
    expression = re.sub(r'(\))(\d)', r')*\2', expression)         # (x)3 -> (x)*3
    return expression

def main():
    input_text = input("Enter a math problem (e.g., 'Solve x^2 - 4 = 0'): ")
    parsed = parse_text(input_text)

    print(f"Parsed Expression: {parsed['expression']}")  # Debugging

    # Preprocess the expression for correct evaluation
    expression = parsed["expression"].replace("^", "**")  # Convert '^' to '**'
    expression = preprocess_expression(expression)        # Add implicit multiplication

    # Dynamically detect variables (alphabets) in the expression
    variables = set(char for char in expression if char.isalpha())
    symbols_dict = {var: symbols(var) for var in variables}

    if "=" in expression:
        lhs, rhs = expression.split("=")  # Split into left and right sides
    else:
        lhs, rhs = expression, "0"  # Assume '= 0' if no '=' provided

    try:
        # Sympify expressions to avoid eval
        lhs_sympy = sympify(lhs.strip(), locals=symbols_dict)
        rhs_sympy = sympify(rhs.strip(), locals=symbols_dict)
        equation = Eq(lhs_sympy, rhs_sympy)

        if parsed["operation"] == "solve":
            solutions = solve(equation)
            print(f"Solutions: {solutions}")
        elif parsed["operation"] == "differentiate":
            variable = list(symbols_dict.values())[0]  # Differentiate w.r.t the first variable
            derivative = diff(lhs_sympy, variable)
            print(f"Derivative: {derivative}")
        elif parsed["operation"] == "integrate":
            variable = list(symbols_dict.values())[0]  # Integrate w.r.t the first variable
            integral = integrate(lhs_sympy, variable)
            print(f"Integral: {integral}")
        else:
            print("Operation not recognized.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
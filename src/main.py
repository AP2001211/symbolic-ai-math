from sympy import symbols, Eq, solve, diff, integrate

def main():
    x = symbols('x')  # Define a symbol x

    # Example 1: Solve a simple equation
    equation = Eq(x**2 - 4, 0)
    solutions = solve(equation, x)
    print("Solutions to the equation x^2 - 4 = 0:", solutions)

    # Example 2: Differentiate a function
    function = x**3 + 2*x**2 + 3*x + 4
    derivative = diff(function, x)
    print("Derivative of x^3 + 2x^2 + 3x + 4:", derivative)

    # Example 3: Integrate a function
    integral = integrate(function, x)
    print("Integral of x^3 + 2x^2 + 3x + 4:", integral)

if __name__ == "__main__":
    main()

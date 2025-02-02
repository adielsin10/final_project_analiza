import math


def print_iteration_header():
    """
    Prints the header for the Newton-Raphson iteration table.
    """
    print("{:<10} {:<15} {:<15}".format("Iteration", "p0", "p1"))


def print_iteration_values(i, p0, p):
    """
    Prints the values for each iteration of the Newton-Raphson method.
    """
    print("{:<10} {:<15.9f} {:<15.9f}".format(i, p0, p))


def newton_raphson(f, df, p0, TOL, N=50):
    """
    Performs the Newton-Raphson method to find the root of the function f.

    Parameters:
        f: The function for which we want to find the root.
        df: The derivative of the function f.
        p0: Initial guess for the root.
        TOL: Tolerance for stopping criteria.
        N: Maximum number of iterations.

    Returns:
        The approximate root of the function f.
    """
    print_iteration_header()

    for i in range(N):
        derivative_value = df(p0)
        if derivative_value == 0 or math.isnan(derivative_value):
            print("Derivative is zero or undefined at p0, method cannot continue.")
            return None

        p = p0 - f(p0) / derivative_value

        if abs(p - p0) < TOL:
            return p  # Procedure completed successfully

        print_iteration_values(i, p0, p)
        p0 = p

    return None  # Did not converge


def f(x):
    """Computes the function f(x) = (2x e^(-x) + ln(2x^2)) * (2x^2 - 3x - 5)"""
    if x == 0 or 2 * x ** 2 <= 0:  # Prevent math domain errors
        return float('nan')

    return (2 * x * math.exp(-x) + math.log(2 * x ** 2)) * (2 * x ** 2 - 3 * x - 5)


def df(x):
    """Computes the derivative f'(x)"""
    if x == 0 or 2 * x ** 2 <= 0:
        return float('nan')

    # Compute the derivative using the product rule
    term1 = 2 * math.exp(-x) - 2 * x * math.exp(-x)  # Derivative of 2x e^(-x)
    term2 = (1 / (2 * x ** 2)) * (4 * x)  # Derivative of ln(2x^2)
    term3 = 4 * x - 3  # Derivative of (2x^2 - 3x - 5)

    return (term1 + term2) * (2 * x ** 2 - 3 * x - 5) + (2 * x * math.exp(-x) + math.log(2 * x ** 2)) * term3


def result():
    TOL = 1e-6
    N = 100
    arr=[]
    # Check for sign changes in the range [-3, 2] with steps of 0.1
    a = -3
    b = a + 0.1
    while b <= 2:
        fa = f(a)
        fb = f(b)

        if math.isnan(fa) or math.isnan(fb):
            print(f"Skipping interval [{a}, {b}] due to math domain error")
        elif fa * fb < 0:  # Sign change detected
            p0 = (a + b) / 2  # Midpoint as initial guess
            print(f"\nSign change detected between {a} and {b}")
            root = newton_raphson(f, df, p0, TOL, N)
            arr.append(root)
            if root is not None:
                print(f"The equation f(x) has an approximate root at x = {root:<15.9f}")
            else:
                print("Newton-Raphson method did not converge.")

        a += 0.1
        b = a + 0.1
    return max(arr)
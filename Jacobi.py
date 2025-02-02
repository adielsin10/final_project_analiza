import numpy as np
from numpy.linalg import norm


def is_diagonally_dominant(A):
    """
    בודק האם המטריצה דומיננטית אלכסונית.
    """
    n = len(A)
    for i in range(n):
        if abs(A[i, i]) < sum(abs(A[i, j]) for j in range(n) if j != i):
            return False
    return True


def swap_rows_to_attempt_dominance(A, b):
    """
    מנסה לסדר את המטריצה כך שתהיה דומיננטית אלכסונית על ידי החלפת שורות.
    """
    n = len(A)
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r, i]))
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
    return A, b


def initialize_guess_vector(b):
    """
    מאתחל את וקטור הניחוש X0 באפסים.
    """
    return np.zeros_like(b, dtype=np.double)


def is_converged(x_new, x_old, tol):
    """
    בודק אם האלגוריתם התכנס.
    """
    return norm(x_new - x_old, np.inf) < tol


def print_iteration_header(A):
    """
    מדפיס את כותרת הטבלה.
    """
    print("Iteration" + "\t\t".join(["{:>12}".format(f"x{i}") for i in range(1, len(A) + 1)]))
    print("-" * 100)


def print_iteration_values(k, x):
    """
    מדפיס את ערכי x בכל איטרציה.
    """
    print("{:<15} ".format(k) + "\t\t".join(["{:<15.10f} ".format(val) for val in x]))


def jacobi_step(A, b, X0):
    """
    מבצע צעד אחד של שיטת ג'קובי.
    """
    n = len(A)
    x = np.zeros(n, dtype=np.double)

    for i in range(n):
        if A[i, i] == 0:
            raise ValueError(f"Zero found on diagonal at row {i}. Jacobi method cannot proceed.")

        sigma = sum(A[i, j] * X0[j] for j in range(n) if j != i)
        x[i] = (b[i] - sigma) / A[i, i]

    return x


def jacobi_iterative(A, b, X0=None, TOL=1e-10, N=200):
    """
    מבצע איטרציות של שיטת ג'קובי לפתרון Ax = b.
    """
    A, b = swap_rows_to_attempt_dominance(A, b)

    if not is_diagonally_dominant(A):
        print("Matrix is not diagonally dominant. Jacobi method may not converge.")
        return None

    n = len(A)
    if X0 is None:
        X0 = initialize_guess_vector(b)

    print_iteration_header(A)

    for k in range(1, N + 1):
        x_new = jacobi_step(A, b, X0)
        print_iteration_values(k, x_new)

        if is_converged(x_new, X0, TOL):
            return tuple(x_new)

        X0 = x_new.copy()

    print("Maximum number of iterations exceeded")
    return tuple(x_new)


def result():
    A = np.array([[0, 1, 2], [-2, 1, 0.5], [1, -2, -0.5]], dtype=np.double)
    b = np.array([0, 4, -4], dtype=np.double)

    try:
        solution = jacobi_iterative(A, b)
        if solution:
            print("\nApproximate solution:", solution)
    except ValueError as e:
        print(f"Error: {e}")
    return solution[0]
print(result())

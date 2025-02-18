def neville(x_data, y_data, x_interpolate):
    """
    Neville's Interpolation Method

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x_interpolate (float): The x-value where you want to interpolate.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    tableau = initialize_tableau(y_data, n)

    for j in range(1, n):
        for i in range(n - j):
            tableau[i][j] = compute_tableau_entry(tableau, x_data, x_interpolate, i, j)

    return tableau[0][n - 1]

def initialize_tableau(y_data, n):
    """
    Initializes the tableau for Neville's method.
    """
    tableau = [[0.0] * n for _ in range(n)]
    for i in range(n):
        tableau[i][0] = y_data[i]
    return tableau

def compute_tableau_entry(tableau, x_data, x_interpolate, i, j):
    """
    Computes an entry in the Neville tableau.
    """
    return ((x_interpolate - x_data[i + j]) * tableau[i][j - 1] -
            (x_interpolate - x_data[i]) * tableau[i + 1][j - 1]) / (x_data[i] - x_data[i + j])

def result():
    # Example usage:
    # x_data = [1, 2, 5, 7]
    # y_data = [1, 0, 2, 3]
    # x_interpolate = 3

    x_data = [1.2, 1.3, 1.4, 1.5, 1.6]
    y_data = [1.5095, 1.6984, 1.9043, 2.1293, 2.3756]
    x_interpolate = 1.47

    interpolated_value = neville(x_data, y_data, x_interpolate)
    print(f"\nInterpolated value at x = {x_interpolate} is y = {interpolated_value}")
    return interpolated_value
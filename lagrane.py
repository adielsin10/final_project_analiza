def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = compute_term(x_data, y_data, x, i)
        result += term

    return result

def compute_term(x_data, y_data, x, i):
    term = y_data[i]
    for j in range(len(x_data)):
        if i != j:
            term *= (x - x_data[j]) / (x_data[i] - x_data[j])
    return term

def result():
    # x_data = [1, 2, 5]
    # y_data = [1, 0, 2]
    # x_interpolate = 3  # The x-value where you want to interpolate


    x_data = [1.2, 1.3, 1.4, 1.5, 1.6]
    y_data = [1.5095, 1.6984, 1.9043, 2.1293, 2.3756]
    x_interpolate = 1.47

    y_interpolate = lagrange_interpolation(x_data, y_data, x_interpolate)
    print(f"\nInterpolated value at x = {x_interpolate} is y = {y_interpolate}")
    return y_interpolate

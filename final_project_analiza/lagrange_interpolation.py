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


    x_data = [0.2,0.35,0.45,0.6,0.75,0.85,0.9]
    y_data = [13.7241,13.9776,14.0625,13.9776,13.7241,13.3056,12.7281]
    x_interpolate = 0.65

    y_interpolate = lagrange_interpolation(x_data, y_data, x_interpolate)
    print(f"\nInterpolated value at x = {x_interpolate} is y = {y_interpolate}")
    return y_interpolate

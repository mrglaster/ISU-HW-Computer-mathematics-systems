from matplotlib import pyplot as plt

from modules.approximation.approximation import linear_approximation, power_polynomial_approximation
from modules.interpolation.interpolation_graphics import smooth_x
from modules.matrix_operations.matrix_operations import *


def linear_approximation_graphics(system, x_values):
    """Graphical Demonstration of linear approximation"""
    approximated_values = linear_approximation(system, x_values, 'y')
    src_transposed = transpose_matrix(system)

    x_array = vec_to_array(src_transposed[0])
    y_array = vec_to_array(src_transposed[1])
    plt.plot(x_array, y_array, color="blue")
    plt.scatter(x=x_values, y=approximated_values, c='orange')

    plt.title("Linear Approximation")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid()
    plt.show()


def power_polynomial_approximation_graphics(system, x_values, power):
    """Graphical demonstration of Nth power polynomial approximation"""
    if power < 2:
        raise ValueError(f"Wrong power for polynomial approximation: {power}")
    x_smoothed = smooth_x(min(x_values), max(x_values))
    approximated_values = power_polynomial_approximation(system, x_smoothed, power, 'y')
    src_transposed = transpose_matrix(system)

    x_array = vec_to_array(src_transposed[0])
    y_array = vec_to_array(src_transposed[1])
    plt.plot(x_smoothed, approximated_values, 'blue')
    plt.scatter(x=x_array, y=y_array, c='orange')
    plt.title(f"Approximation by Polynomial of Power {power}")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid()
    plt.show()


def demo_linear_approximation():
    """DEMO of linear approximation"""
    test_values = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    test_x = [1, 3, 5]
    linear_approximation_graphics(test_values, test_x)

def demo_power_polynomial_approximation_graph():
    """DEMO of Nth power polynomial approximation"""
    test_values = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    test_x = [1, 3, 5]
    power_polynomial_approximation_graphics(test_values, test_x, 3)

demo_linear_approximation()
demo_power_polynomial_approximation_graph()
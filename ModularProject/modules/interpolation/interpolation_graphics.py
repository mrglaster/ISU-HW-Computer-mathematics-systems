from modules.matrix_operations import *
from modules.vector_operations import *
from modules.matrix_operations.matrix_operations import *
from modules.matrix_operations.matrix_parameters import *
from modules.interpolation.interpolation import *
from matplotlib import pyplot as plt

def _generate_plot(x, y):
    """Generates Plot with legend"""
    plt.plot(x, y)
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.grid()
    plt.show()


def _get_right_value(origins_matrix, value, type):
    """Returns interpolated/extrapolated value and color for graphics"""
    if type == 'interpolation':
        try:
            return get_interpolated_value(origins_matrix, value), 'blue'
        except:
            return get_extrapolated_value(origins_matrix, value), 'orange'
    try:
        return get_extrapolated_value(origins_matrix, value), 'orange'
    except:
        return get_interpolated_value(origins_matrix, value), 'blue'


def _check_origins_type(origins_matrix, origins_type):
    """Method checking format of origins and turns it into UV array if required"""
    if origins_type != 'UV':
        return classic_to_vector(origins_matrix)
    return origins_matrix

def _get_origins(origins_matrix):
    """Returns X and Y values from array of UV"""
    return get_col_bid_arr(origins_matrix, 0), get_col_bid_arr(origins_matrix, 1)


def demonstrate_basic_interpolation(origins_matrix, interpolation_x, extrapolation_x, origins_type='UV'):
    """Line Equation interpolation graphical demonstration"""
    is_matrix_twopointed(origins_matrix, True)
    origins_matrix = _check_origins_type(origins_matrix, origins_type)
    interpolated_value, interpolated_color = _get_right_value(origins_matrix, interpolation_x, 'interpolation')
    extrapolated_value, extrapolation_color = _get_right_value(origins_matrix, extrapolation_x, 'extrapolation')
    x_origins, y_origins = _get_origins(origins_matrix)
    plt.scatter(interpolated_value[0], interpolated_value[1],  color=interpolated_color)
    plt.scatter(extrapolated_value[0], extrapolated_value[1], color=extrapolation_color)
    plt.title("Interpolation demonstration")
    _generate_plot(x_origins, y_origins)


def demonstrate_linear_partial_interpolation(origins_matrix, values_to_calculate, origins_type='UV'):
    """Graphical demonstration of partial linear interpolation"""
    is_matrix_twopointed(origins_matrix, True)
    origins_matrix = _check_origins_type(origins_matrix, origins_type)
    if len(values_to_calculate) == 0:
        raise ValueError("Unable to calculate interpolation for matrix with size = 0!")
    x_origins, y_origins = _get_origins(origins_matrix)
    result = solve_partial_linear_interpolation(origins_matrix, values_to_calculate)
    for i in range(len(values_to_calculate)):
        plt.scatter(values_to_calculate[i], result[i], color='orange')
    plt.title("Demonstration of partial linear interpolation")
    _generate_plot(x_origins, y_origins)


def smooth_x(start, end, step=0.1):
    """Creates array with values between start and end with some step"""
    result_array = [start]
    current_value = start
    while current_value < end:
        current_value+=step
        result_array.append(current_value)
    return result_array

def demonstrate_lagrange_polynomial(origins_matrix, origins_type='UV'):
    """Graphical demonstration of lagrange polynomial"""
    origins_matrix = _check_origins_type(origins_matrix, origins_type)
    x_origins, y_originals = _get_origins(origins_matrix)
    for i in range(len(x_origins)):
        plt.scatter(x_origins[i], y_originals[i], color='green')
    y_origins = []
    x_origins = sorted(x_origins)
    smoothed_x = smooth_x(x_origins[0], x_origins[-1])

    for i in smoothed_x:
        y_origins.append(lagrange_polynomial(origins_matrix, i))
    plt.title("Lagrange polynomial")
    _generate_plot(smoothed_x, y_origins)


#########################################
#            DEMO FUNCTIONS            ##
#########################################

def demo_basic_interp():
    test = classic_to_vector([[2, 5], [6, 9]])
    demonstrate_basic_interpolation(test, 3, 1, 'UV')

def demo_partial_linear_interp():
    test_data = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    values_calculus = [-1.5, 3, 2, 5, 9]
    demonstrate_linear_partial_interpolation(test_data, values_calculus)

def demo_lagrange_polynomial():
    data_xy = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    demonstrate_lagrange_polynomial(data_xy)

demo_basic_interp()
demo_partial_linear_interp()
demo_lagrange_polynomial()

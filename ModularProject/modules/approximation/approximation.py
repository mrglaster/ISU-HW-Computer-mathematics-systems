from modules.linear_equations_system.les_solver import *
from modules.matrix_operations.matrix_operations import *


def _generate_ones_array(length):
    """Generates Vector of length N filled with 1"""
    ones_result = []
    for i in range(length):
        ones_result.append(1)
    return array_to_vec(ones_result)


def least_square_method(system):
    """Least squares method"""
    matrix_existance(system)
    source_copy = transpose_matrix(system)
    a_matrix = source_copy[:-1]
    b_matrix = transpose_matrix([source_copy[-1]])
    a_transposed = a_matrix
    a_matrix = transpose_matrix(a_matrix)
    a_waved = matrix_mul_matrix(a_transposed, a_matrix)
    b_waved = transpose_matrix(matrix_mul_matrix(a_transposed, b_matrix))
    if len(a_waved) == len(b_waved) == 1:
        return array_to_vec([b_waved[0][0] / a_waved[0][0]])
    return matrix_mul_matrix(b_waved, inverse_matrix(a_waved))


def _get_right_amatrix(approximation_power, copy_value):
    """Retyrns A matrix depended from the polynomial's power"""
    a_matrix = []
    if approximation_power == 0 or approximation_power == 1:
        a_matrix = copy_value[:-1]
        a_matrix.append(_generate_ones_array(len(a_matrix[0])))
        return a_matrix
    start = approximation_power
    while start >= 0:
        a_matrix.append(vec_power(copy_value[0], start))
        start -= 1
    return a_matrix


def get_approximation_equation(system, approximation_type, arbitary_function=None):
    """Returns equation for current type of approximation
       :param system - system of equations
       :param approximation_type - type of approximation
              There are few possible variants:
              -1 - arbitary function
              0 or 1- Linear approximation
              2 or more - approximation of polynomial of power n
       :param arbitary_function - Arbitary function. Default = None
        """
    if approximation_type < -1:
        raise ValueError(f"Wrong approximation equation type! Expected  0 <= x <= 3. Got: {approximation_type}")
    if approximation_type == -1:
        raise ValueError("Sorry, arbitrary function approximation wasn't done yet")
    matrix_existance(system)
    source_copy = transpose_matrix(system)
    b_matrix = transpose_matrix([source_copy[-1]])
    a_matrix = _get_right_amatrix(approximation_type, source_copy)
    a_transposed = a_matrix
    a_matrix = transpose_matrix(a_matrix)
    a_waved = matrix_mul_matrix(a_transposed, a_matrix)
    b_waved = transpose_matrix(matrix_mul_matrix(a_transposed, b_matrix))
    if approximation_type == 0:
        b_waved = transpose_matrix(b_waved)
        return solve_les_invmatrix_separated(a_waved, b_waved)
    return matrix_div_matrix(b_waved, a_waved)


def linear_approximation(system, x_array, output_format='y'):
    """Linear approximation"""
    equation_parameters = transpose_matrix(get_approximation_equation(system, 0))
    our_result = []
    for i in x_array:
        la_value = i * equation_parameters[0][0] + equation_parameters[0][1]
        if output_format == 'y':
            our_result.append(la_value)
        else:
            our_result.append(array_to_vec([i, la_value]))
    return our_result


def _calculate_power_value(equation_parameters, power, x):
    """Calculats value of equation for polynomial"""
    calculations_result = 0
    current_power = power
    cur_mul = 0
    while current_power > 0:
        calculations_result += pow(x, current_power) * equation_parameters[cur_mul]
        cur_mul += 1
        current_power -= 1
    calculations_result += equation_parameters[cur_mul]
    return calculations_result


def power_polynomial_approximation(system, x_array, power, output_format='y'):
    """Approximation by polynomial of power N"""
    equation_parameters = get_approximation_equation(system, power)
    calculations_result = []
    for i in x_array:
        la_value = _calculate_power_value(equation_parameters[0], power, i)
        if output_format == 'y':
            calculations_result.append(la_value)
        else:
            calculations_result.append(array_to_vec([i, la_value]))
    return calculations_result

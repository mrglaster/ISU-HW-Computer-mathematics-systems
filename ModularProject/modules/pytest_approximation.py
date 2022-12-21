from modules.matrix_operations.matrix_operations import *
from modules.approximation.approximation import *

def test_least_squares_single():
    matrix_test = classic_to_vector(([2, 4], [3, 9]))
    result = round(least_square_method(matrix_test)[0], 2)
    expected_result = array_to_vec([2.69])
    assert result == expected_result[0]

def test_least_squares_multiple():
    matrix_test_2 = classic_to_vector([[2, 3, 7], [3, 3, 7], [4, 7, 3]])
    result = round_matrix(least_square_method(matrix_test_2), round_number=2)
    expected_result = classic_to_vector([[4.68, -2.06]])
    assert result == expected_result

def test_linear_approx_equations():
    test_values = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    expected_result = classic_to_vector([[0.99], [0.67]])
    equations = round_matrix(get_approximation_equation(test_values, 0), 2)
    assert expected_result == equations

def test_2ndpower_polynomial_equations():
    test_values = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    expected_result = array_to_vec([0.13, 0.07, 1.89])
    assert round_matrix(get_approximation_equation(test_values, 2), 2)[0] == expected_result

def test_3rdpower_polynomial_equations():
    test_values = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    expected_result = array_to_vec([0.48, -4.8, 13.96, -7.64])
    assert round_matrix(get_approximation_equation(test_values, 3), 2)[0] == expected_result


def test_linear_approximation():
    test_values = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    test_x = [1, 3, 5]
    result = round_matrix(linear_approximation(test_values, test_x, 'UV'), 2)
    expected_result = classic_to_vector([[1.0, 1.66], [3.0, 3.63], [5.0, 5.6]])
    assert result == expected_result

def test_2power():
    test_values = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    test_x = [1, 3, 5]
    result = round_matrix(power_polynomial_approximation(system=test_values, x_array=test_x, power=2, output_format='UV'), 2)
    expected_result = classic_to_vector([[1.0, 2.09], [3.0, 3.26], [5.0, 5.46]])
    assert result == expected_result

def test_3power():
    test_values = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    test_x = [1, 3, 5]
    expected_result = [[1.0, 2.0], [3.0, 4.0], [5.0, 2.16]]
    result = round_matrix(power_polynomial_approximation(system=test_values, x_array=test_x, power=3, output_format='UV'), 2)
    assert expected_result == result

def test_3power():
    test_values = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    test_x = [1, 3, 5]
    expected_result = [[1.0, 488.08], [3.0, 14975.59], [5.0, 113797.23]]
    result = round_matrix(power_polynomial_approximation(system=test_values, x_array=test_x, power=4, output_format='UV'), 2)
    for i in range(len(expected_result)):
        for j in range(len(expected_result[0])):
            assert expected_result[i][j] == result[i][j]
from modules.interpolation.interpolation import *

def test_get_linear_interpolated_value_y():
    test = classic_to_vector([[2, 5], [6, 9]])
    result = get_interpolated_value(test, 4, 'y')
    assert result == 7.0

def test_get_linear_interpolated_value_universal_vector():
    test = classic_to_vector([[2, 5], [6, 9]])
    result = get_interpolated_value(test, 4, result_type='uv')
    uv = array_to_vec([4.0, 7.0])
    assert result == uv

def test_get_linear_extrapolated_value_y():
    test = classic_to_vector([[2, 5], [6, 9]])
    result = get_extrapolated_value(test, 1, result_type='y')
    assert result == 4.0

def test_get_linear_extrapolated_value_universal_vector():
    test = classic_to_vector([[2, 5], [6, 9]])
    result = get_extrapolated_value(test, 1, result_type='uv')
    uv = array_to_vec([1.0, 4.0])
    assert result == uv

def test_linear_partial_interpolation():
    test_data = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    values_calculus = [-1.5, 3, 2, 5, 9]
    answer = [-0.5, 4.0, 3.0, 5.4, 11.8]
    assert solve_partial_linear_interpolation(test_data, values_calculus) == answer

def test_lagrange_polynomial():
    data_xy = classic_to_vector([[1, 2], [3, 4], [3.5, 3], [6, 7]])
    for vector in data_xy:
        assert vector[1] == lagrange_polynomial(data_xy, vector[0])

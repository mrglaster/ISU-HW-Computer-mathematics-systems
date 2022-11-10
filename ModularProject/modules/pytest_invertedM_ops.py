from modules.matrix_operations.matrix_operations import *
from modules.linear_equations_system.les_solver import *


def test_invert_twosize():
    test_matrix = [[1, 1], [-1, 3]]
    excepted_result = classic_to_vector([[0.75, -0.25], [0.25, 0.25]])
    assert (
        inverse_twosized_matrix(
            m=test_matrix, do_round=False, round_after=0, determinant=4.0
        )
        == excepted_result
    )


def test_invert_larger_matrix():
    test_matrix = [[2, 1, 0, 0], [3, 2, 0, 0], [1, 1, 3, 4], [2, -1, 2, 3]]
    result = inverse_larger_matrix(
        m=test_matrix,
        determinant=get_determinant(classic_to_vector(test_matrix)),
        do_round=True,
        round_after=0,
    )
    expected = classic_to_vector(
        [[2, -1, 0, 0], [-3, 2, 0, 0], [31, -19, 3, -4], [-23, 14, -2, 3]]
    )
    assert result == expected


def test_inverted_matrix_autodetect():
    test_matrix = classic_to_vector(
        [[2, 1, 0, 0], [3, 2, 0, 0], [1, 1, 3, 4], [2, -1, 2, 3]]
    )
    result = inverse_matrix(test_matrix, do_round=True, round_after=0)
    expected = classic_to_vector(
        [[2, -1, 0, 0], [-3, 2, 0, 0], [31, -19, 3, -4], [-23, 14, -2, 3]]
    )
    assert result == expected


def test_inverce_self():
    test_matrix = [[1, 2], [3, 4]]
    result = matrix_inverce_test(test_matrix)
    excepted = True
    assert result == excepted

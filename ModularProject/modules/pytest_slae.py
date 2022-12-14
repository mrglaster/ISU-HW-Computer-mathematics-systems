from modules.matrix_operations.matrix_operations import *
from modules.linear_equations_system.les_solver import *

def test_reverse_matrix():
    matrix_test = classic_to_vector([[1, 2, 3], [0, 1, 2], [0, 0, 1]])
    result = reverse_matrix_cols(matrix_test)
    excepted_result = classic_to_vector([[2, 1, 0], [1, 0, 0], [3, 2, 1]])
    assert result == excepted_result

def test_sort_md_rows():
    matrix_test = classic_to_vector([[1, -2, -6, 15], [0, 0, 18, 36], [0, 2, 12, 20]])
    excepted_answer = classic_to_vector([[1, -2, -6, 15], [0, 2, 12, 20], [0, 0, 18, 36]])
    assert matrix_sort_md_rows(matrix_test) == excepted_answer

def test_solve_les_2d():
    equal_test = classic_to_vector([[2, 3, 2], [4, 3, 7]])
    excepted_result = array_to_vec([-1.0, 2.5])
    assert get_les_result(equal_test) == excepted_result

def test_solve_les_3d():
    equal_test = classic_to_vector([[-1, 2, 6, 15], [3, -6, 0, -9], [1, 0, 6, 5]])
    excepted_result = array_to_vec([-2.0, 2.0, -7.0])
    result = get_les_result(equal_test)
    assert result == excepted_result

def test_solve_slae_invertedm():
    test_matrix = [[1, 2, 6], [3, 4, 8]]
    got_answer = solve_les_invmatrix(classic_to_vector(test_matrix), True)
    excepted_answer = classic_to_vector([[-4.0, 5.0]])
    assert got_answer == excepted_answer

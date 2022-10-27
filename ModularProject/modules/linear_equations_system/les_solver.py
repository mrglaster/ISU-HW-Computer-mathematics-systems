from modules.linear_equations_system.les_parameters import *
from modules.matrix_operations.matrix_operations import *
from modules.matrix_operations.matrix_io import *
from modules.matrix_operations.matrix_operations import *
from modules.vector_operations.vec_basic_operations import *

POTENTIAL_REPLACER = -1
global first_row


def is_left_correct(les_matrix):
    """Checks if there is any row first element of which != zero """
    global POTENTIAL_REPLACER
    left = get_col_bid_vec(matrix=les_matrix, id=0)
    for i in range(len(left)):
        if left.get_dimval(i) != 0:
            swap_rows(les_matrix, 0, i)
            return True
    raise ValueError("The first left column contains only zeroes! We can't solve such linear equations system")


def get_les_result(les_matrix):
    """Returns result of Linear equation system"""
    is_left_correct(les_matrix)
    result = solve_les(les_matrix)
    return result[0]


def solve_les(combined_matrix, reversed=False):
    """Solves Linear Equations System"""
    copied_matrix = get_copy(combined_matrix)
    for i in range(0, len(combined_matrix)):
        mul_row_scalar(matrix=copied_matrix, rowid=i, scalar=1 / copied_matrix[i].get_dimval(i), do_copy=False)
        for j in range(i + 1, len(combined_matrix)):
            b_matrix = mul_row_scalar(matrix=copied_matrix, scalar=copied_matrix[j].get_dimval(i), rowid=i, do_copy=True)
            diff_two_matrix_rows(matrix_first=copied_matrix, matrix_second=b_matrix, source_id=j, divider_id=i)
        matrix_sort_md_rows(copied_matrix)
    return reverse_matrix_all(transpose_matrix(copied_matrix)) if reversed else solve_les(reverse_matrix_all(copied_matrix), reversed=True)
















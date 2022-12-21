from modules.matrix_operations.matrix_parameters import matrix_exists
from modules.matrix_operations.matrix_parameters import matrix_sizepar
from modules.matrix_operations.matrix_parameters import massive_existance_check
from modules.matrix_operations.matrix_parameters import get_col_bid_vec
from modules.matrix_operations.matrix_parameters import get_row_bid
from modules.matrix_operations.matrix_parameters import is_square_matrix
from modules.matrix_operations.matrix_parameters import matrix_existance
from modules.matrix_operations.matrix_parameters import row_in_matrix
from modules.matrix_operations.matrix_generators import generate_zero_square_matrix
from modules.matrix_operations.matrix_parameters import matrixes_canworktogether

from modules.matrix_operations.matrix_parameters import get_matrix_cols

from modules.matrix_operations.matrix_io import print_matrix

from modules.vector_operations.vec_io import array_to_vec
from modules.vector_operations.vec_io import vec_to_array
from modules.vector_operations.vec_basic_operations import *

import copy


def matrix_summ(matrix_1, matrix_2):
    """sum of matrices"""
    matrix_result = []
    matrixes_canworktogether(matrix_1, matrix_2)
    for i in range(len(matrix_1)):
        matrix_result.append(vec_summ(matrix_1[i], matrix_2[i]))
    return matrix_result


def matrix_diff(matrix_1, matrix_2):
    """Matrix difference"""
    matrix_result = []
    matrixes_canworktogether(matrix_1, matrix_2)
    for i in range(len(matrix_1)):
        matrix_result.append(vec_diff(matrix_1[i], matrix_2[i]))
    return matrix_result


def matrix_mul_scalar(matrix, scalar):
    """Multiplying a Matrix by a Number"""
    matrix_existance(matrix)
    matrix_new = []
    for i in range(len(matrix)):
        matrix_new.append(vec_mulnum(matrix[i], scalar))
    return matrix_new


def transpose_matrix(matrix):
    """Matrix transposition"""
    matrix_new = []
    if matrix_exists(matrix):
        if len(matrix) == 1:
            for i in range(len(matrix[0])):
                matrix_new.append(array_to_vec([matrix[0].get_dimval(i)]))
            return matrix_new
        for i in range(len(matrix[0])):
            matrix_new.append(get_col_bid_vec(matrix, i))
    return matrix_new


def matrix_mul_matrix(matrix1, matrix2):
    """Matrix multiplication"""
    if get_matrix_cols(matrix1) == len(matrix2):
        matrix_mulresult = []
        for i in range(len(matrix1)):
            current_matrix = []
            for j in range(len(matrix2[0])):
                current_matrix.append(
                    vec_mulscalar(
                        get_row_bid(id=i, matrix=matrix1), get_col_bid_vec(matrix2, j)
                    )
                )
            matrix_mulresult.append(array_to_vec(current_matrix))
        return matrix_mulresult
    raise ValueError(f"Matrix size aren't correct: {len(matrix1)}x{len(matrix1[0])}  and {len(matrix2)}x{len(matrix2[0])}")


def matrix_div_matrix(matrix1, matrix2):
    """Divide matrix by matrix"""
    massive_existance_check([matrix1, matrix2])
    # matrixes_canworktogether(matrix1, matrix2)
    return matrix_mul_matrix(matrix1, inverse_matrix(matrix2))


def mul_row_scalar(matrix, rowid, scalar, do_copy=False):
    """Multiply a matrix row by a number"""
    matrix_existance(matrix)
    if rowid > len(matrix):
        raise ValueError("Unavailable index!")
    if do_copy:
        copy = get_copy(matrix)
        copy[rowid] = vec_mulnum(copy[rowid], scalar)
        return copy
    else:
        matrix[rowid] = vec_mulnum(matrix[rowid], scalar)
        return matrix


def dif_rows_multiplied(matrix, row1, row2, scalar):
    """Multiply a row by a number and subtract it from another"""
    matrix_existance(matrix)
    if row1 > len(matrix) or row2 > len(matrix):
        raise ValueError(f"Unavailable index(es): {row1} , {row2}")
    temp = vec_mulnum(matrix[row1], scalar)
    matrix[row2] = vec_diff(matrix[row2], temp)
    # return matrix


def sum_rows_multiplied(matrix, row1, row2, scalar):
    """Multiply a row by a number and add another to it"""
    matrix_existance(matrix)
    rows_check(len(matrix), row1, row2)
    matrix[row1] = vec_mulnum(matrix[row1], scalar)
    matrix[row1] = vec_summ(matrix[row1], matrix[row2])
    return matrix


def swap_rows(matrix, row1, row2):
    """swap rows"""
    matrix_existance(matrix)
    rows_check(len(matrix), row1, row2)
    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp
    return matrix


def swap_columns(matrix, col1, col2):
    """Swaps columns of matrix"""
    matrix_existance(matrix)
    matrix = transpose_matrix(matrix)
    rows_check(len(matrix), col1, col2)
    matrix = swap_rows(matrix, col1, col2)
    return transpose_matrix(matrix)


def matrix_to_classic(matrix):
    """Converts a matrix from an Array of UniversalVectors to an Array of Arrays """
    matrix_existance(matrix)
    array = []
    for i in matrix:
        array.append(vec_to_array(i))
    return array


def classic_to_vector(matrix):
    """Converts the matrix of the format Array of Arrays into an Array of UniversalVectors"""
    result = []
    if len(matrix) == 0:
        raise ValueError("Matrix size can't be zero!")
    for i in range(len(matrix)):
        result.append(array_to_vec(matrix[i]))
    return result


def LU_decomposition_arrays(A):
    """
    Find Lower (L) and Upper (U) matrices for source matrix A
    """
    matrix_existance(A)
    A = matrix_to_classic(A)
    if is_square_matrix(A):
        n = len(A[0])
        L = matrix_to_classic(generate_zero_square_matrix(matrix_size=n))
        U = matrix_to_classic(generate_zero_square_matrix(matrix_size=n))
        for i in range(n):
            L[i][i] = 1
            if i == 0:
                U[0][0] = A[0][0]
                for j in range(1, n):
                    U[0][j] = A[0][j]
                    L[j][0] = A[j][0] / U[0][0]
            else:
                for j in range(i, n):
                    c = 0
                    for k in range(0, i):
                        c = c + L[i][k] * U[k][j]
                    U[i][j] = A[i][j] - c
                for j in range(i + 1, n):
                    c = 0
                    for k in range(0, i):
                        c = c + L[j][k] * U[k][i]
                    if U[i][i] != 0:
                        L[j][i] = (A[j][i] - c) / U[i][i]
                    else:
                        L[j][i] = 0
        return L, U
    raise ValueError(f"LU decomposition can't be done for rectangle matrix!")


def LU_decomposition_vectors(matrix):
    """LU decomposition. Matrices L and U are represented as two UniversalVector arrays"""
    matrix_existance(matrix)
    L, U = LU_decomposition_arrays(matrix_to_classic(matrix))
    return classic_to_vector(L), classic_to_vector(U)


def get_determinant(matrix):
    """Finding the matrix determinant"""
    matrix_existance(matrix)
    if len(matrix) == 2 and len(matrix[0]) == 2:
        matrix_c = matrix_to_classic(matrix)
        return matrix_c[0][0] * matrix_c[1][1] - matrix_c[0][1] * matrix_c[1][0]
    matrix = matrix_to_classic(matrix)
    L, U = LU_decomposition_arrays(matrix)
    O = 1
    for i in range(len(U[0])):
        O *= U[i][i]
    return O


def matrix_append_row_array(matrix, row):
    """Add a row to the end of the matrix, which is an array"""
    matrix_existance(matrix)
    row = array_to_vec(row)
    matrix.append(row)
    return matrix


def matrix_append_row_vec(matrix, row):
    """Add a row to the end of the matrix that is UniversalVec"""
    matrix_existance(matrix)
    matrix.append(row)
    return matrix


def matrix_insert_row(matrix, id, row):
    """Insert UniversalVector Format row into Matrix"""
    matrix_existance(matrix)
    matrix.insert(id, row)
    return matrix


def matrix_delete_row(matrix, id):
    """Remove row from matrix"""
    matrix_existance(matrix)
    row_in_matrix(matrix, id)
    matrix.pop(id)
    return matrix


def get_matrix_minor(m, i, j):
    """Finds a minot of matrix m. Format of matix m: array of arrays"""
    return [row[:j] + row[j + 1 :] for row in (m[:i] + m[i + 1 :])]


def _is_roundable(matrix):
    """Is it possible to round elements of matrix?"""
    if len(matrix) == 0:
        raise ValueError("Unable to round elements of zero size matrix!")


def round_matrix(matrix, round_number):
    """Rounds elements of matrix if it's possible"""
    _is_roundable(matrix)
    _do_round_check(round_number)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = round(matrix[i][j], round_number)
    return matrix


def _do_round_check(round_after):
    """Is rounding number available to be used?"""
    if round_after < 0:
        raise ValueError(f"Wrong rounding argument: {round_after} is below zero!")


def inverse_twosized_matrix(m, determinant, do_round=False, round_after=0):
    """Inverts matrix of size 2x2"""
    matrix_existance(m)
    if len(m) != 2 or len(m[0]) != 2:
        raise ValueError("Wrong input matrix: 2x2 matrix excepted!")
    determinant_zerocheck(determinant)
    result = [
        [m[1][1] / determinant, -1 * m[0][1] / determinant],
        [-1 * m[1][0] / determinant, m[0][0] / determinant],
    ]
    if do_round:
        round_matrix(result, round_after)
    return classic_to_vector(result)


def inverse_larger_matrix(m, determinant, do_round=False, round_after=0):
    """Inverts matrix larger than 2x2"""
    matrix_existance(m)
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = get_matrix_minor(m, r, c)
            cofactorRow.append(
                ((-1) ** (r + c)) * get_determinant(classic_to_vector(minor))
            )
        cofactors.append(cofactorRow)
    cofactors = matrix_to_classic(transpose_matrix(classic_to_vector(cofactors)))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    if do_round:
        return classic_to_vector(round_matrix(cofactors, round_after))
    return classic_to_vector(cofactors)


def _floatify_matrix(matrix):

    """
   #Turns matrix from matrixn of ints to matrix of floats
    if len(matrix) == 0:
        raise ValueError("Unable to floatify zero size matrix")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = float(matrix[i][j])
    return matrix
    """
    return matrix

def square_check(matrix):
    """Throws error if current matrix isn't zero matrix"""
    if not is_square_matrix(matrix):
        raise ValueError("Unable to do operation with rectangular matrix")


def determinant_zerocheck(determinant):
    """Throws error if determinant = 0"""
    if determinant == 0:
        raise ValueError("Unable to do operation: Determinant is zero!")


def inverse_matrix(matrix, do_round=False, round_after=0):
    """Find inverted matrix"""
    matrix_existance(matrix)
    square_check(matrix)
    determinant = get_determinant(matrix)
    determinant_zerocheck(determinant)
    m = _floatify_matrix(matrix_to_classic(matrix))
    determinant = float(determinant)
    if len(m) == 2:
        return inverse_twosized_matrix(m, determinant, do_round, round_after)
    return inverse_larger_matrix(m, determinant, do_round, round_after)


def matrix_sort_md_rows(matrix):
    """Sorts matrix rows by main diagonal"""
    matrix_existance(matrix)
    for i in range(len(matrix[0])):
        index_md = -1
        for j in range(i, len(matrix)):
            if matrix[j].get_dimval(i) == 0:
                index_md = j
            elif index_md != -1:
                swap_rows(matrix=matrix, row1=index_md, row2=j)
    return matrix


def reverse_matrix_all(matrix):
    """Reverses direction of rows and columns in the matrix"""
    matrix = reverse_matrix_rows(matrix)
    matrix = reverse_matrix_cols(matrix)
    return transpose_matrix(matrix)


def reverse_matrix_rows(matrix):
    """Reverse matrix rows"""
    for i in range(len(matrix) // 2):
        matrix = swap_rows(matrix, i, len(matrix) - i - 1)
    return matrix


def reverse_matrix_cols(matrix):
    """Reverse matrix columns"""
    last_col = transpose_matrix(matrix)[-1]
    matrix = reverse_matrix_rows(transpose_matrix(matrix)[:-1])
    matrix_append_row_vec(matrix=matrix, row=last_col)
    return matrix


def get_copy(original_object):
    """Returns copy of original object"""
    return copy.deepcopy(original_object)


def rows_check(len_matrix, row1, row2):
    """Do two rows belong to matrix?"""
    if row1 < 0 or row2 < 0 or row1 > len_matrix or row2 > len_matrix:
        raise ValueError("Unavailable indexes!")


def diff_matrix_rows(matrix, source_id, divider_id):
    """Row2-Row1"""
    matrix_existance(matrix)
    rows_check(len(matrix), source_id, divider_id)
    matrix[source_id] = vec_diff(matrix[source_id], matrix[divider_id])
    return matrix


def diff_two_matrix_rows(matrix_first, matrix_second, source_id, divider_id):
    if len(matrix_second) != len(matrix_first):
        raise ValueError("Unavailable matrices size")
    rows_check(len(matrix_first), source_id, divider_id)
    matrix_first[source_id] = vec_diff(
        matrix_first[source_id], matrix_second[divider_id]
    )
    return matrix_first


def matrix_inverce_test(matrix):
    test_matrix = matrix
    inverted_one = inverse_matrix(test_matrix)
    result = matrix_mul_matrix(classic_to_vector(test_matrix), inverted_one)
    result = matrix_to_classic(result)
    for i in range(len(result)):
        for j in range(len(result[0])):
            if not result[i][i]:
                return False
            if result[i][j] != 0 and j != i:
                return False
    return True


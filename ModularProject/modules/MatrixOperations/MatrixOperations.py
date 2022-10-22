from modules.MatrixOperations.MatrixParameters import matrix_exists
from modules.MatrixOperations.MatrixParameters import matrix_sizepar
from modules.MatrixOperations.MatrixParameters import massive_existance_check
from modules.MatrixOperations.MatrixParameters import get_col_bid_vec
from modules.MatrixOperations.MatrixParameters import get_row_bid
from modules.MatrixOperations.MatrixParameters import is_square_matrix
from modules.MatrixOperations.MatrixParameters import matrix_existance
from modules.MatrixOperations.MatrixParameters import row_in_matrix
from modules.MatrixOperations.MatrixGenerators import generate_zero_square_matrix
from modules.MatrixOperations.MatrixParameters import matrixes_canworktogether

from modules.VectorOperations.VecKbRead import array_to_vec
from modules.VectorOperations.VecKbRead import vec_to_array
from modules.VectorOperations.VecBasicOperations import *


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
        for i in range(len(matrix[0])):
            matrix_new.append(get_col_bid_vec(matrix, i))
    return matrix_new


def matrix_mul_matrix(matrix1, matrix2):
    """Matrix multiplication"""
    if len(matrix1) == len(matrix2[0]) and len(matrix2) == len(matrix1[0]):
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
    raise ValueError("Matrix size aren't correct!")


def mul_row_scalar(matrix, rowid, scalar):
    """Multiply a matrix row by a number"""
    matrix_existance(matrix)
    if rowid > len(matrix):
        raise ValueError("Unavailable index!")
    matrix[rowid] = vec_mulnum(matrix[rowid], scalar)
    return matrix


def dif_rows_multiplied(matrix, row1, row2, scalar):
    """Multiply a row by a number and subtract another from it"""
    matrix_existance(matrix)
    if row1 > len(matrix) or row2 > len(matrix):
        raise ValueError(f"Unavailable index(es): {ro1} , {row2}")
    matrix[row1] = vec_mulnum(matrix[row1], scalar)
    matrix[row1] = vec_diff(matrix[row1], matrix[row2])
    return matrix


def sum_rows_multiplied(matrix, row1, row2, scalar):
    """Multiply a row by a number and add another to it"""
    matrix_existance(matrix)
    if row1 > len(matrix) or row2 > len(matrix):
        raise ValueError(f"Unavailable index(es): {ro1} , {row2}")
    matrix[row1] = vec_mulnum(matrix[row1], scalar)
    matrix[row1] = vec_summ(matrix[row1], matrix[row2])
    return matrix


def swap_rows(matrix, row1, row2):
    """swap rows"""
    matrix_existance(matrix)
    if row1 < 0 or row2 < 0 or row1 > len(matrix) or row2 > len(matrix):
        raise ValueError("Unavailable index")
    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp
    return matrix


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
        raise ValueError("Wrong matrix size!")
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
    raise ValueError("LU decomposition can't be done for rectangle matrix!")


def LU_decomposition_vectors(matrix):
    """LU decomposition. Matrices L and U are represented as two UniversalVector arrays"""
    matrix_existance(matrix)
    L, U = LU_decomposition_arrays(matrix_to_classic(matrix))
    return classic_to_vector(L), classic_to_vector(U)


def get_determinant(matrix):
    """Finding the matrix determinant"""
    matrix_existance(matrix)
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

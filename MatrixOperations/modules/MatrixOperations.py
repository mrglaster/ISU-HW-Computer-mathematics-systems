from .MatrixParameters import matrix_exists
from .MatrixParameters import matrix_sizepar
from .MatrixParameters import massive_existance_check
from .MatrixParameters import get_col_bid_vec
from .MatrixParameters import get_row_bid
from .MatrixParameters import is_square_matrix
from .MatrixParameters import matrix_existance
from .MatrixParameters import row_in_matrix
from .MatrixGenerators import generate_zero_square_matrix
from .MatrixParameters import matrixes_canworktogether

from .VecKbRead import array_to_vec
from .VecKbRead import vec_to_array
from .VecBasicOperations import *


def matrix_summ(matrix_1, matrix_2):
    """Сумма матриц"""
    matrix_result = []
    matrixes_canworktogether(matrix_1, matrix_2)
    for i in range(len(matrix_1)):
        matrix_result.append(vec_summ(matrix_1[i], matrix_2[i]))
    return matrix_result


def matrix_diff(matrix_1, matrix_2):
    """Разность матриц"""
    matrix_result = []
    matrixes_canworktogether(matrix_1, matrix_2)
    for i in range(len(matrix_1)):
        matrix_result.append(vec_diff(matrix_1[i], matrix_2[i]))
    return matrix_result


def matrix_mul_scalar(matrix, scalar):
    """Умножение матрицы на число"""
    matrix_existance(matrix)
    matrix_new = []
    for i in range(len(matrix)):
        matrix_new.append(vec_mulnum(matrix[i], scalar))
    return matrix_new


def transpose_matrix(matrix):
    """Транспонирование матрицы"""
    matrix_new = []
    if matrix_exists(matrix):
        for i in range(len(matrix[0])):
            matrix_new.append(get_col_bid_vec(matrix, i))
    return matrix_new


def matrix_mul_matrix(matrix1, matrix2):
    """Умножение матрицы на матрицу"""
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
    """Умножить строку матрицы на число"""
    matrix_existance(matrix)
    if rowid > len(matrix):
        raise ValueError("Unavailable index!")
    matrix[rowid] = vec_mulnum(matrix[rowid], scalar)
    return matrix


def dif_rows_multiplied(matrix, row1, row2, scalar):
    # умножить 1, вычесть 2
    """Умножаем строку на число и вычитаем из неё другую"""
    matrix_existance(matrix)
    if row1 > len(matrix) or row2 > len(matrix):
        raise ValueError(f"Unavailable index(es): {ro1} , {row2}")
    matrix[row1] = vec_mulnum(matrix[row1], scalar)
    matrix[row1] = vec_diff(matrix[row1], matrix[row2])
    return matrix


def sum_rows_multiplied(matrix, row1, row2, scalar):
    # умножить 1, вычесть 2
    """Умножаем строку на число и суммируем к ней другую"""
    matrix_existance(matrix)
    if row1 > len(matrix) or row2 > len(matrix):
        raise ValueError(f"Unavailable index(es): {ro1} , {row2}")
    matrix[row1] = vec_mulnum(matrix[row1], scalar)
    matrix[row1] = vec_summ(matrix[row1], matrix[row2])
    return matrix


def exchange_rows(matrix, row1, row2):
    """Меняем строки местами"""
    matrix_existance(matrix)
    if row1 < 0 or row2 < 0 or row1 > len(matrix) or row2 > len(matrix):
        raise ValueError("Unavailable index")
    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp
    return matrix


def matrix_to_classic(matrix):
    """Приводит матрицу из вида Массив Векторов в Массив Массивов """
    matrix_existance(matrix)
    array = []
    for i in matrix:
        array.append(vec_to_array(i))
    return array


def classic_to_vector(matrix):
    """Преобразем матриу формата Массив Массивов в Массив UniversalVector'ов"""
    result = []
    if len(matrix) == 0:
        raise ValueError("Wrong matrix size!")
    for i in range(len(matrix)):
        result.append(array_to_vec(matrix[i]))
    return result


def LU_decomposition_arrays(A):
    """
    Находим матрицы L и U для исходной матрицы A
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
    """LU разложение. Матрицы L и U представлены как два массива UniversalVector"""
    matrix_existance(matrix)
    L, U = LU_decomposition_arrays(matrix_to_classic(matrix))
    return classic_to_vector(L), classic_to_vector(U)


def get_determinant(matrix):
    """Находим определитель матрицы"""
    matrix_existance(matrix)
    matrix = matrix_to_classic(matrix)
    L, U = LU_decomposition_arrays(matrix)
    O = 1
    for i in range(len(U[0])):
        O *= U[i][i]
    return O


def matrix_append_row_array(matrix, row):
    """Добавляем в конец матрицы строку, являющуюся массивом"""
    matrix_existance(matrix)
    row = array_to_vec(row)
    matrix.append(row)
    return matrix


def matrix_append_row_vec(matrix, row):
    """Добавляем в конец матрицы строку, являющуюся UniversalVec"""
    matrix_existance(matrix)
    matrix.append(row)
    return matrix


def matrix_insert_row(matrix, id, row):
    """Вставить строку формата UniversalVector в матрицу"""
    matrix_existance(matrix)
    matrix.insert(id, row)
    return matrix


def matrix_delete_row(matrix, id):
    """Удалить строку из матрицы"""
    matrix_existance(matrix)
    row_in_matrix(matrix, id)
    matrix.pop(id)
    return matrix

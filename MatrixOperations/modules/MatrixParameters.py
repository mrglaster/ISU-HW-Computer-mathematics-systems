from .UniversalVectorClass import UniversalVector
from .VecKbRead import array_to_vec


def get_matrix_cols(matrix):
    """ Количество столбцов матрицы """
    if len(matrix) == 0:
        return 0
    return len(matrix[0])


def get_matrix_rows(matrix):
    """Количество строк матрицы"""
    return len(matrix)


def matrix_exists(matrix):
    """Проверка существования матрицы"""
    return len(matrix) and len(matrix[0])


def get_matrix_sizes(matrix):
    """Получить размерность матрицы"""
    matrix_existance(matrix)
    return get_matrix_rows(matrix), get_matrix_cols(matrix)



def matrix_sizepar(matrix1, matrix2):
    """Равны ли размерности у матриц"""
    return len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])


def massive_existance_check(matrixes):
    """Массовая проверка существования"""
    for i in matrixes:
        matrix_existance(i)
    return True


def get_row_bid(matrix, id):
    """Получить строку по индексу"""
    row_in_matrix(matrix, id)
    return matrix[id]


def get_col_bid_arr(matrix, id):
    """Получить столбец матрицы по ID как массив"""
    matrix_existance(matrix)
    row_in_matrix(matrix, id)
    array = []
    for i in range(len(matrix)):
        array.append(matrix[i].get_dimval(id))
    return array


def get_col_bid_vec(matrix, id):
    """Получить столбец матрицы по ID как UniversalVector"""
    array = get_col_bid_arr(matrix, id)
    return array_to_vec(array)


def is_square_matrix(matrix):
    """Проверка на квадратность матрицы"""
    return len(matrix) == len(matrix[0])


def matrix_existance(matrix):
    """Общая проверка на существование матрицы"""
    if not matrix_exists(matrix):
        raise ValueError("Matrix doesn't exist!")


def row_in_matrix(matrix, rowid):
    """Пренадлежит ли строка матрицу"""
    if rowid < 0 or rowid > len(matrix):
        raise ValueError("Unavailable row index")


def col_in_matrix(matrix, colid):
    """Пренадлежит ли столбец матрице"""
    matrix_existance(matrix)
    if colid < 0 or colid > len(matrix[0]):
        raise ValueError("Unavialable column index")
    return True


def matrixes_canworktogether(matrix_1, matrix_2):
    """Проверка допустимости операции между матрицами"""
    if matrix_sizepar(matrix_1, matrix_2) and massive_existance_check(
        [matrix_1, matrix_2]
    ):
        return True
    raise ValueError("Sizes of 2 matrix must be the same! ")

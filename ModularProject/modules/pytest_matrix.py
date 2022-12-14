from modules.matrix_operations import matrix_io
from modules.matrix_operations import matrix_operations
from modules.matrix_operations import matrix_parameters
from modules.matrix_operations import matrix_generators


def test_matrix_mulnum():
    """Умножение матрицы на число"""
    matrix = matrix_operations.classic_to_vector([[1, 2], [3, 4]])
    num = 2
    answer = matrix_operations.classic_to_vector([[2, 4], [6, 8]])
    assert answer == matrix_operations.matrix_mul_scalar(matrix, num)


def test_matrix_sum_matrix():
    """Сложение матриц"""
    a = matrix_operations.classic_to_vector([[1, 2], [3, 4]])
    b = matrix_operations.classic_to_vector([[3, 4], [-1, 3]])
    ans = matrix_operations.classic_to_vector([[4, 6], [2, 7]])
    assert ans == matrix_operations.matrix_summ(a, b)


def test_matrix_diff_matrix():
    """Разность матриц"""
    a = matrix_operations.classic_to_vector([[6, 7], [-4, 3]])
    b = matrix_operations.classic_to_vector([[1, 3], [2, -5]])
    ans = matrix_operations.classic_to_vector([[5, 4], [-6, 8]])
    assert ans == matrix_operations.matrix_diff(a, b)


def test_matrix_mul_matrix():
    """Умножение матрицы на матрицу"""
    a = matrix_operations.classic_to_vector([[1, 2], [3, 4]])
    b = matrix_operations.classic_to_vector([[5, 6], [7, 8]])
    ans = matrix_operations.classic_to_vector([[19, 22], [43, 50]])
    assert ans == matrix_operations.matrix_mul_matrix(a, b)


def test_transpose_matrix():
    """Транспонирование матрицы"""
    a = matrix_operations.classic_to_vector([[2, 3, 5], [5, 7, 6]])
    ans = matrix_operations.classic_to_vector([[2, 5], [3, 7], [5, 6]])
    assert ans == matrix_operations.transpose_matrix(a)


def test_get_row():
    """Получить строку матрицы"""
    a = matrix_operations.classic_to_vector([[1, 2], [3, 4], [5, 6]])
    ans = matrix_operations.array_to_vec([3, 4])
    id = 1
    assert ans == matrix_operations.get_row_bid(matrix=a, id=id)


def test_get_col():
    """Получить столбец матрицы"""
    a = matrix_operations.classic_to_vector([[1, 2], [3, 4], [5, 6]])
    ans = matrix_operations.array_to_vec([1, 3, 5])
    index = 0
    assert ans == matrix_operations.get_col_bid_vec(a, index)


def test_swap_rows():
    """Поменять строки местами"""
    a = matrix_operations.classic_to_vector([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    start_index = 0
    new_index = 1
    ans = matrix_operations.classic_to_vector([[4, 5, 6], [1, 2, 3], [7, 8, 9]])
    assert ans == matrix_operations.swap_rows(a, start_index, new_index)


def test_mulrow_scalar():
    """Умножить строку на число"""
    a = matrix_operations.classic_to_vector([[1, 2, 3], [3, 2, 1]])
    num = 2
    rowid = 0
    ans = matrix_operations.classic_to_vector([[2, 4, 6], [3, 2, 1]])
    assert ans == matrix_operations.mul_row_scalar(matrix=a, rowid=rowid, scalar=num)


def test_sum_multiplied():
    """Умножить строку на число и прибавить к ней другую строку"""
    a = matrix_operations.classic_to_vector([[1, 2], [3, 4]])
    row_to_add = 1
    row_to_mul = 0
    mulnum = 2
    ans = matrix_operations.classic_to_vector([[5, 8], [3, 4]])
    assert ans == matrix_operations.sum_rows_multiplied(
        matrix=a, row1=row_to_mul, row2=row_to_add, scalar=mulnum
    )


def test_find_determinant():
    """Найти определитель матрицы"""
    a = matrix_operations.classic_to_vector([[5, 4, 3], [21, -2, 6], [5, 4, 0]])
    ans = 282.0
    assert ans == matrix_operations.get_determinant(a)

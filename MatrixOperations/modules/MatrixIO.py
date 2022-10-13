from .VecKbRead import parse_1vec_parametrised


def print_matrix(matrix):
    """Вывести матрицы"""
    if len(matrix) == 0:
        return None
    for i in range(len(matrix)):
        print(matrix[i])
    print()


def read_rectmatrix_kb(columns, rows, debug=0):
    """Чтение ПРЯМОУГОЛЬНОЙ матрицы с клавиатуры"""
    matrix = []
    for i in range(rows):
        vector = parse_1vec_parametrised(columns, debug=1)
        if vector is not None:
            matrix.append(vector)
        else:
            raise ValueError("Not enough items! Terminating")
    if debug:
        print_matrix(matrix)
    return matrix


def read_square_matrix_kb(sizes, debug=0):
    """Чтение КВАДРАТНОЙ матрицы с клавиатуры"""
    if sizes <= 0:
        raise ValueError("Wrong argument amount!")
    return read_rectmatrix_kb(sizes, sizes, debug)

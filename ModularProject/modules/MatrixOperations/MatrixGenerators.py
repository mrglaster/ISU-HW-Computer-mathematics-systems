from modules.VectorOperations.UniversalVectorClass import UniversalVector


def generate_zero_square_matrix(matrix_size, debug=0):
    """Generate square zero matrix"""
    if matrix_size <= 0:
        raise ValueError(f"Incorrect matrix size: {matrix_size}")
    result_martrix = []
    for i in range(matrix_size):
        cur_vector = UniversalVector(matrix_size)
        for j in range(matrix_size):
            cur_vector.set_dimval(j, 0)
        result_martrix.append(cur_vector)
    return result_martrix


def generate_zero_rect_matrix(matrix_width, matrix_height, debug=0):
    """Generate Rectangular Zero Matrix"""
    if matrix_width <= 0 or matrix_height <= 0:
        raise ValueError(f"Incorrect matrix size: {matrix_width}x{matrix_height}")
    matrix = []
    for i in range(matrix_height):
        cur_vector = UniversalVector(matrix_width)
        for j in range(matrix_width):
            cur_vector.set_dimval(j, 0)
        matrix.append(cur_vector)
    return matrix

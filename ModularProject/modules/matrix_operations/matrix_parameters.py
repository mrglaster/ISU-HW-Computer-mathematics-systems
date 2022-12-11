from modules.vector_operations.universal_vector_class import UniversalVector
from modules.vector_operations.vec_io import array_to_vec


def get_matrix_cols(matrix):
    """ Amount of matrix columns """
    if len(matrix) == 0:
        return 0
    return len(matrix[0])


def get_matrix_rows(matrix):
    """Amount of matrix rows"""
    return len(matrix)


def matrix_exists(matrix):
    """Matrix existance check"""
    return len(matrix) and len(matrix[0])


def get_matrix_sizes(matrix):
    """Get matrix's sizes"""
    matrix_existance(matrix)
    return get_matrix_rows(matrix), get_matrix_cols(matrix)



def matrix_sizepar(matrix1, matrix2):
    """Check of matrices sizes equality"""
    return len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])


def massive_existance_check(matrixes):
    """Matrix existence check for array of matrices"""
    for i in matrixes:
        matrix_existance(i)
    return True


def get_row_bid(matrix, id):
    """Get row by index"""
    row_in_matrix(matrix, id)
    return matrix[id]


def get_col_bid_arr(matrix, id):
    """Get column of matrix by id (returns array)"""
    matrix_existance(matrix)
    array = []
    for i in range(len(matrix)):
        array.append(matrix[i].get_dimval(id))
    return array


def get_col_bid_vec(matrix, id):
    """Get matrix column by ID, returns UniversalVector"""
    array = get_col_bid_arr(matrix, id)
    return array_to_vec(array)


def is_square_matrix(matrix):
    """Is the matrix square?"""
    return len(matrix) == len(matrix[0])


def matrix_existance(matrix, error_message="Matrix doesn't exist!"):
    """Does the matrix exist?"""
    if not matrix_exists(matrix):
        raise ValueError(error_message)


def row_in_matrix(matrix, rowid):
    """Is there a row with concrete ID in the  matrix?"""
    if rowid < 0 or rowid > len(matrix):
        raise ValueError(f"Unavailable row index: {rowid}")


def col_in_matrix(matrix, colid):
    """Is there a column with concrete ID in the  matrix?"""
    matrix_existance(matrix)
    if colid < 0 or colid > len(matrix[0]):
        raise ValueError("Unavailable column index")
    return True


def matrixes_canworktogether(matrix_1, matrix_2):
    """Is it possible to do a operation between 2 matrices?"""
    if matrix_sizepar(matrix_1, matrix_2) and massive_existance_check(
        [matrix_1, matrix_2]
    ):
        return True
    raise ValueError("Sizes of 2 matrix must be the same! ")

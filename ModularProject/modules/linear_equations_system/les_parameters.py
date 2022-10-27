from modules.matrix_operations.matrix_parameters import matrix_existance
from modules.matrix_operations.matrix_parameters import get_col_bid_vec
from modules.matrix_operations.matrix_operations import transpose_matrix

def is_valid_les(les):
    """Is current Linear equations system valid?"""
    matrix_existance(les, error_message="Current LES isn't valid!")
    if len(les) + 1 != len(les[0]):
        raise ValueError("Input Linear equation system is not valid!")

def get_AMatrix(les):
    """Get A-matrix (Matrix of arguments)"""
    is_valid_les(les)
    result = []
    for i in range(len(les[0])-1):
        result.append(get_col_bid_vec(matrix=les, id=i))
    return transpose_matrix(result)

def get_resultsVector(les):
    """Gets the vector of LES results"""
    return transpose_matrix([get_col_bid_vec(matrix=les, id=len(les[0])-1)])


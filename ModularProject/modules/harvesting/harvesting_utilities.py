from modules.matrix_operations.matrix_parameters import *
from modules.matrix_operations.matrix_operations import *

import warnings
warnings.filterwarnings('ignore')
import numpy as np

def is_valid_leslie(leslie_matrix):
    """Checks if Leslie matrix is valid"""
    matrix_existance(leslie_matrix)
    if not is_square_matrix(leslie_matrix) or len(leslie_matrix) == len(leslie_matrix[0]) == 1:
        raise ValueError(f"Wrong Leslie matrix. Got sizes: {len(leslie_matrix)}x{len(leslie_matrix[0])}")

def get_params_leslie(leslie_matrix):
    """Returns fertility and survival matrices by Leslie matrix"""
    is_valid_leslie(leslie_matrix)
    fertility = leslie_matrix[0]
    survival = leslie_matrix[1:]
    return [fertility], survival


def get_harvesting_array(harvesting_matrix):
    """Returns non zero elements of harvesting matrix as UniversalVector"""
    result = []
    for i in range(len(harvesting_matrix[0])):
        result.append(harvesting_matrix[i][i])
    return array_to_vec(result)

def get_survival_array(survival_matrix):
    """Returns survival coefficients as one UniversalVector"""
    result = []
    for i in range(len(survival_matrix)):
        for j in range(len(survival_matrix[0])):
            if survival_matrix[i][j] != 0:
                result.append(survival_matrix[i][j])
    return array_to_vec(result)

def calculate_population_condition(leslie_matrix, popultaion_matrix, time):
    """Calculates population condition after N iterations."""
    current_matrix = popultaion_matrix
    for i in range(time):
        current_matrix = matrix_mul_matrix(leslie_matrix, current_matrix)
    return current_matrix


def prepare_survival(survival_matrix, harvesting_array):
    """Multiplies survival matrix elements by harvesting coefficients"""
    multiplied_matrix = survival_matrix
    for i in range(len(multiplied_matrix)):
        for j in range(len(multiplied_matrix[0])):
            if multiplied_matrix[i][j] != 0:
                multiplied_matrix[i][j] *= (1 - harvesting_array[i + 1])
    return multiplied_matrix


def prepare_fertility(fertility, harvesting_argument):
    """Prepares fertility array for reproduction rate calculation"""
    new_fertility = fertility
    for i in range(len(new_fertility[0])):
        new_fertility[0][i]*=(1-harvesting_argument)
    return new_fertility


def get_leslie_eigenvalue(leslie_matrix):
    """Returns maximal positive eigenvalue for Leslie matrix"""
    is_valid_leslie(leslie_matrix)
    prepared = np.array(matrix_to_classic(leslie_matrix))
    w, v = np.linalg.eig(prepared)
    result = float(max(w))
    if result < 0 or result is None:
        raise ValueError(f"Positive maximal eigenvalue wasn't found! Matrix: {print_matrix(leslie_matrix)}")
    return float(max(w))



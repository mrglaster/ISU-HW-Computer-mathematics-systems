import copy
from modules.harvesting.harvesting_utilities import *


def calculate_reproduction_rate(leslie_matrix, harvesting_matrix):
    """Calculates reproduction rate by leslie matrix and harvesting matrix"""
    is_valid_leslie(leslie_matrix)
    harvesting = get_harvesting_array(harvesting_matrix)
    fertility, mortality = get_params_leslie(leslie_matrix)
    fertility = prepare_fertility(fertility, harvesting[0])
    mortality = prepare_survival(mortality, harvesting_array=harvesting)
    result = fertility[0][0]
    for i in range(1, len(fertility[0])):
        current_value = fertility[0][i]
        copy_matrix = copy.deepcopy(mortality)
        copy_matrix = transpose_matrix(transpose_matrix(copy_matrix)[:i])
        for j in range(len(copy_matrix)):
            for k in range(len(copy_matrix[0])):
                if copy_matrix[j][k]!=0:
                    current_value*=copy_matrix[j][k]
        result+=current_value
    return result


def calculate_harvesting_argument(leslie_matrix):
    """Calculates harvesting argument for leslie matrix. Use it when harvesting indices matrix is unknown and you'r going to take the same part from every age group."""
    is_valid_leslie(leslie_matrix)
    return 1 - (1/get_leslie_eigenvalue(leslie_matrix))


def calculate_youngest_age_harvesting(leslie_matrix):
    """Calculates harvesting index for model, when only the youngest age group is harvested"""
    is_valid_leslie(leslie_matrix)
    zeroes_harvesting = generate_zero_square_matrix(len(leslie_matrix[0]))
    dirty_harvesting_index = calculate_reproduction_rate(leslie_matrix, zeroes_harvesting)
    if dirty_harvesting_index < 1:
        print(f"WARNING: Harvesting index = {dirty_harvesting_index}. Using 'Youngest Age Harvesting' is not appropriate ")
    return 1 - (1/dirty_harvesting_index)


def get_xo_harvested_population(leslie_matrix, harvesting_matrix):
    is_valid_reproduction_rate(leslie_matrix)
    """Get X1 vector for default harvest model"""
    is_valid_leslie(leslie_matrix)
    _, mortality = get_params_leslie(leslie_matrix)
    harvesting_array = get_harvesting_array(harvesting_matrix)
    mortality = get_survival_array(prepare_survival(mortality, harvesting_array))
    result_x = [1]
    current_maxlength = 1
    for i in range(len(mortality)):
        current_value = 1
        for j in range(current_maxlength):
            current_value*=mortality[j]
        result_x.append(current_value)
        current_maxlength+=1
    return array_to_vec(result_x)


def is_valid_reproduction_rate(leslie_matrix):
    """Checks if reproduction rate is greater than 1"""
    is_valid_leslie(leslie_matrix)
    zeroes_harvesting = generate_zero_square_matrix(len(leslie_matrix[0]))
    harvesting_index = calculate_reproduction_rate(leslie_matrix, zeroes_harvesting)
    if round(harvesting_index, 1) < 1:
        raise Warning(f"Cant calculate X1 for current Leslie matrix: {harvesting_index} < 1")




def get_x_universal_harvesting(leslie_matrix):
    """Get X1 vector for universal harvesting model"""
    is_valid_reproduction_rate(leslie_matrix)
    eigen_value = get_leslie_eigenvalue(leslie_matrix)
    _, mortality = get_params_leslie(leslie_matrix)
    mortality = get_survival_array(mortality)
    result_x = [1]
    current_maxlen = 1
    power = 0
    for i in range(len(mortality)):
        current_value = 1
        power+=1
        for j in range(current_maxlen):
            current_value*=mortality[j]
        result_x.append(current_value/pow(eigen_value, power))
        current_maxlen+=1
    return array_to_vec(result_x)


def get_x_youngest_harvesting(leslie_matrix):
    """Returns X1 array for youngest age group harvesting model"""
    is_valid_reproduction_rate(leslie_matrix)
    _, mortality = get_params_leslie(leslie_matrix)
    mortality = get_survival_array(mortality)
    result_x = [1]
    current_maxlen = 1
    for i in range(len(mortality)):
        current_value = 1
        for j in range(current_maxlen):
            current_value*=mortality[j]
        result_x.append(current_value)
        current_maxlen+=1
    return array_to_vec(result_x)

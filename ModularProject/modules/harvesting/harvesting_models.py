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


def get_population_after_iterations(leslie_matrix, x_matrix, iterations):
  """What happens with current population with current Leslie matrix after N iterations"""
  result_x = copy.deepcopy(x_matrix)
  leslie_copy = copy.deepcopy(leslie_matrix)
  for i in range(iterations):
    result_x = matrix_mul_matrix(leslie_copy, result_x)
  return result_x


GEMEIN_TEST_MATRIX = classic_to_vector([
        [.000, .045, .391, .472, .484, .546, .543, .502, .468, .459, .433, .421],
        [.845, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, .975, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, .965, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, .950, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, .926, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, .895, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, .850, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, .786, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, .691, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, .561, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, .370, 0]])

test_matrix = copy.deepcopy(GEMEIN_TEST_MATRIX)
expected_result = array_to_vec([1.0, 0.845, 0.8238749999999999, 0.7950393749999999, 0.7552874062499999, 0.6993961381874999, 0.6259595436778125, 0.5320656121261406, 0.4182035711311465, 0.28897866765162217, 0.16211703255256005, 0.05998330204444722])
result = get_x_youngest_harvesting(test_matrix)
for i in range(len(expected_result)):
    if expected_result[i] != result[i]:
        print(f"ERROR: {expected_result[i]} and {result[i]}, item = {i}")
    else:
        print(f"ALL IS FINE: {expected_result[i]} and {result[i]}" )
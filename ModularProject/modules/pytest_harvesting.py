import copy

from modules.harvesting.harvesting_utilities import *
from modules.harvesting.harvesting_models import *


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


def test_reproduction_rate_1():
    test_leslie = copy.deepcopy(GEMEIN_TEST_MATRIX)
    harvesting_matrix_one = classic_to_vector([[0.522, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    expected_result = 1.256680980372384
    assert expected_result == calculate_reproduction_rate(test_leslie, harvesting_matrix_one)

def test_reproduction_rate_2():
    test_leslie = copy.deepcopy(GEMEIN_TEST_MATRIX)
    harvesting_matrix_two = classic_to_vector([
        [0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0.15, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0.15, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.15]])

    expected_Result = 0.9959431250930566
    assert expected_Result == calculate_reproduction_rate(test_leslie, harvesting_matrix_two)

def test_reproduction_rate_3():
    leslie_three = classic_to_vector([
        [0.89, 0.12],
        [0.56, 0.0]]
    )

    harvesting_three = classic_to_vector([
        [0.15, 0],
        [0, 0.34]
    ])

    expected_result = 0.7941992
    assert expected_result == calculate_reproduction_rate(leslie_three, harvesting_three)


def test_eigenvalue_leslie():
    test_leslie =  copy.deepcopy(GEMEIN_TEST_MATRIX)
    expected_result = 1.175571423260434
    assert expected_result == get_leslie_eigenvalue(test_leslie)

def test_harvesting_argument():
    expected_result = 0.1493498564072684
    test_leslie = copy.deepcopy(GEMEIN_TEST_MATRIX)
    assert expected_result == calculate_harvesting_argument(test_leslie)


def test_youngest_age_harvesting():
    test_leslie = copy.deepcopy(GEMEIN_TEST_MATRIX)
    expected_result = 0.6021723301266393
    assert expected_result == calculate_youngest_age_harvesting(test_leslie)


def test_get_xo_default_harvesting():
    leslie_three = classic_to_vector([
        [0.89, 0.12],
        [0.56, 0.0]]
    )
    harvesting_three = classic_to_vector([
        [0.15, 0],
        [0, 0.34]
    ])
    result = get_xo_harvested_population(leslie_three, harvesting_three)
    expected_result = array_to_vec([1.0, 0.3696])
    assert result == expected_result


def test_get_x_universal_harvesting():
    test_matrix = copy.deepcopy(GEMEIN_TEST_MATRIX)
    expected_result = array_to_vec([1.0, 0.7187993713358581, 0.5961606187301826, 0.48937477186971085, 0.39547238396354834, 0.31151440083034143, 0.23716584396879264, 0.17148338534324312, 0.11465567996367401, 0.06739452260175169, 0.032161658944313005, 0.01012257832568932] )
    assert expected_result == get_x_universal_harvesting(test_matrix)


def test_get_x_youngest_harvesting():
    test_matrix = copy.deepcopy(GEMEIN_TEST_MATRIX)
    expected_result = array_to_vec([ 1.0, 0.845, 0.8238749999999999, 0.7950393749999999, 0.7552874062499999, 0.6993961381874999, 0.6259595436778125, 0.5320656121261406, 0.4182035711311465, 0.28897866765162217, 0.16211703255256005, 0.05998330204444722])
    assert expected_result == get_x_youngest_harvesting(test_matrix)


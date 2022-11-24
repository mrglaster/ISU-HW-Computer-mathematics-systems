from modules.matrix_operations import *
from modules.vector_operations import *
from modules.matrix_operations.matrix_operations import *
from modules.matrix_operations.matrix_parameters import *
from modules.linear_equations_system.les_solver import *


RETURN_POINT = ['uv',  'universalvector',  'v', 'vector', 'uvector']
RETURN_COORDINATE = ['y', 'answer', 'z', 'y-value']


def is_matrix_twopointed(input_matrix, raise_Exception_OnFalse=False):
    """Checks if elements of matrix are UniversalVectors with 2 dimensions"""
    matrix_existance(input_matrix)
    if raise_Exception_OnFalse and len(input_matrix[0]) != 2 :
        raise ValueError(f"Expected matrix of UniversalVectors with 2 dimensions! Got: {len(input_matrix[0])}")
    return len(input_matrix[0]) == 2

def is_matrix_of_linear_equation(input_matrix, raiseOnFalse=False):
    """Checks if data in matrix consists the linear equation"""
    if raiseOnFalse and (not is_square_matrix(input_matrix) or not is_matrix_twopointed(input_matrix)):
        raise ValueError(f"Excepted matrix of two vectors with 2 points in each one. Got: {print_matrix(input_matrix)}")
    return not is_square_matrix(input_matrix) or not is_matrix_twopointed(input_matrix)

def find_line_equation_tp(input_matrix):
    """ Finds a line equation by 2 points
        @:param input_matrix: array of objects of class UniversalVector
    """
    matrix_existance(input_matrix)
    is_matrix_twopointed(input_matrix, True)
    vector_1 = [input_matrix[0][0], 1, input_matrix[0][1]]
    vector_2 = [input_matrix[1][0], 1, input_matrix[1][1]]
    got_slae = classic_to_vector([vector_1, vector_2])
    return solve_les_invmatrix(got_slae)

def value_in_range(input_matrix, value, rightBorderOnly = False, leftBorderOnly=False, debug=False):
    """Checks if the value belongs to range defined by 2 points"""
    matrix_existance(input_matrix)
    if rightBorderOnly:
        if debug:
            print(f"checking: {value} <= {input_matrix[1][0]-0.1}. Returned: {value <= input_matrix[1][0]-0.1}")
        return value <= input_matrix[1][0]-0.1

    if leftBorderOnly:
        if debug:
            print(f"checking: {value} >= {input_matrix[0][0] }. Returned: {value >= input_matrix[0][0]}")
        return value >= input_matrix[0][0]

    if debug:
        print(f"checking: {input_matrix[0][0] } <={value} <= {input_matrix[1][0] - 0.1}. Returned: {input_matrix[0][0] <= value <= input_matrix[1][0]-0.1} ")
    return input_matrix[0][0] <= value <= input_matrix[1][0]-0.1


def value_not_in_range(input_matrix, value):
    """Checks if the value doesn't belong to range defined by 2 points"""
    return not value_in_range(input_matrix, value)


def belongs_to_output_format(value, raiseOnFalse = False):
    """Checks if output format string belongs to possible variants"""
    if value.lower() not in RETURN_POINT and value.lower() not in RETURN_COORDINATE:
        if raiseOnFalse:
            raise ValueError(f"Unknown output format: {value}")
        return False
    return True


def is_result_uv(string):
    """Checks if  result type string consists 'UV' or something similar """
    belongs_to_output_format(string.lower(), True)
    return string.lower() in RETURN_POINT

def is_result_origin(string):
    """Checks if result type string consists y or something else """
    belongs_to_output_format(string.lower(), True)
    return string.lower() in RETURN_COORDINATE


def solve_linear_equation(linear_equation_points, x, round_after_comma=1, result_type="UV"):
    """Solves linear equation for x.
        @:param linear_equation_points - array of 2 UniversalVector 2D vectors.
        @:param round_after_coma : number of symbols after comma
        @:param result_type: determines in which form should we return answer:
        UV (or 'uv',  'universalvector',  'v', 'vector', 'uvector') - as a UniversalVector object
        Y (or 'y', 'answer', 'z', 'y-value') - as an y-axis value
    """
    is_matrix_of_linear_equation(linear_equation_points, True)
    equation = find_line_equation_tp(linear_equation_points)
    belongs_to_output_format(value=result_type, raiseOnFalse=True)
    if result_type.lower() in RETURN_POINT:
        return array_to_vec([x, round(equation[0][0] * x + equation[1][0], round_after_comma)])
    return round(equation[0][0] * x + equation[1][0], round_after_comma)

def solve_linear_equation_byargs(linear_equation_data, x):
    return linear_equation_data[0][0]*x+linear_equation_data[1][0]


def get_interpolated_value(input_matrix, checking_x, result_type='UV'):
    """
        Function returns interpolated value for

        @:param input_matrix: array of objects of class UniversalVector. Should contain data about 2 points.
        @:param checking_x: x on which we look for interpolated value
        @:param result_type: determines in which form should we return answer:
        UV (or 'uv',  'universalvector',  'v', 'vector', 'uvector') - as a UniversalVector object
        Y (or 'y', 'answer', 'z', 'y-value') - as an y-axis value

        @:returns result: depended from result_type
    """
    if not value_in_range(input_matrix, checking_x):
        raise ValueError(f"You should use get_extrapolated_value or something else for x which doesn't belong to range! Got: {checking_x}")
    return solve_linear_equation(
        input_matrix, checking_x, 1, result_type)


def get_extrapolated_value(input_matrix, checking_x, result_type='UV'):
    """
        Function returns extrapolated value for

        @:param input_matrix: array of objects of class UniversalVector. Should contain data about 2 points.
        @:param checking_x: x on which we look for interpolated value
        @:param result_type: determines in which form should we return answer:
        UV (or 'uv',  'universalvector',  'v', 'vector', 'uvector') - as a UniversalVector object
        Y (or 'y', 'answer', 'z', 'y-value') - as an y-axis value

        @:returns result: UniversalVector Class object
    """
    if not value_not_in_range(input_matrix, checking_x):
        raise ValueError("You should use get_interpolated_value for x which doesn't belong to range!")
    return solve_linear_equation(input_matrix, checking_x, 1, result_type)


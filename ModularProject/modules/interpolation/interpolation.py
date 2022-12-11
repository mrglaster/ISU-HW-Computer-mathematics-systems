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
            print(f"checking: {value} <= {input_matrix[1][0]-0.1}. Returned: {value <= input_matrix[1][0]}")
        return value < input_matrix[1][0]

    if leftBorderOnly:
        if debug:
            print(f"checking: {value} >= {input_matrix[0][0] }. Returned: {value >= input_matrix[0][0]}")
        return value >= input_matrix[0][0]

    if debug:
        print(f"checking: {input_matrix[0][0] } <={value} <= {input_matrix[1][0] - 0.1}. Returned: {input_matrix[0][0] <= value <= input_matrix[1][0]-0.1} ")
    return input_matrix[0][0] <= value < input_matrix[1][0]


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



def get_ranges(data_xy):
    """Returns ranges for partial linear equation"""
    ranges = []
    for i in range(len(data_xy)-1):
        current_matrix = [data_xy[i], data_xy[i+1]]
        ranges.append(current_matrix)
    return ranges

def get_partial_linear_equations(data_xy):
    """Returns all linear equations for given data"""
    matrix_existance(data_xy)
    if len(data_xy[0]) != 2:
        raise ValueError(f"Expected matrix of UniversalVectors with 2 dimensions. Got: {len(data_xy[0])}")
    if len(data_xy) < 2:
        raise ValueError(f"Expected more or equal 2 points. Got: {len(data_xy)}")
    equations = []
    for i in range(len(data_xy)-1):
        current_matrix = [data_xy[i], data_xy[i+1]]
        equations.append(find_line_equation_tp(current_matrix))
    return equations


def solve_partial_linear_interpolation(data_origins, values_to_analyze, output_format='y'):
    """Solves partial linear interpolation

        @:param data_origins : contains data for getting of linear equations
        @:param values_to_analyze : x-es for which we'll search for interpolated value. Array of integers
        @:param output_format: determines in which form should we return answer:
        UV (or 'uv',  'universalvector',  'v', 'vector', 'uvector') - as a UniversalVector objects array
        Y (or 'y', 'answer', 'z', 'y-value') - as an y-axis values array
    """
    if len(values_to_analyze)== 0:
        raise ValueError("Expected non-zero size array of X-es. Got length: 0")
    belongs_to_output_format(output_format)
    equations = get_partial_linear_equations(data_origins)
    ranges = get_ranges(data_origins)
    result_data = []
    for current_value_index in range(len(values_to_analyze)):
        current_equation = 0
        for current_range in ranges:
            use_only_right = current_value_index == 0
            use_only_left = current_value_index == len(values_to_analyze) - 1
            real_range = current_range
            if use_only_left:
                real_range = ranges[len(ranges)-1]
                current_equation = len(equations) -1
            if value_in_range(real_range, values_to_analyze[current_value_index], rightBorderOnly=use_only_right, leftBorderOnly=use_only_left):
                if is_result_origin(output_format):
                    result_data.append(solve_linear_equation_byargs(equations[current_equation], values_to_analyze[current_value_index]))
                else:
                    result_data.append(array_to_vec([values_to_analyze[current_value_index], solve_linear_equation_byargs(equations[current_equation], values_to_analyze[current_value_index])]))
                break
            current_equation+=1
    return result_data


def lagrange_polynomial(data_xy, interpolate_Value):
    """Solves lagrange polynomial by origins from data_xy and x as interpolate value"""
    length_range = len(data_xy)
    result = 0.0
    for i in range(length_range):
        temp = data_xy[i][1]
        for j in range(length_range):
            if j!=i:
                temp *= (interpolate_Value - data_xy[j][0]) / (data_xy[i][0] - data_xy[j][0])

        result += temp
    return result
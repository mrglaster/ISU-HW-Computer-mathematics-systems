from modules.matrix_operations import *
from modules.vector_operations import *
from modules.matrix_operations.matrix_operations import *
from modules.matrix_operations.matrix_parameters import *
from modules.interpolation_extrapolation.linear_inter_extrap import *


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



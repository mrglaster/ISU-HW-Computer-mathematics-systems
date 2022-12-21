import math

from modules.matrix_operations.matrix_io import print_matrix
from modules.matrix_operations.matrix_operations import transpose_matrix, classic_to_vector
from modules.vector_operations.vec_io import array_to_vec

SUPPORTED_FUNCTIONS = ['exp','sin', 'cos', 'arcsin', 'arccos']

def is_supported_function(function):
    """Checks if function name is supported"""
    if function not in SUPPORTED_FUNCTIONS:
        raise ValueError(f"Unsopported function {function}. Supported are: {SUPPORTED_FUNCTIONS}")

def factorial(number):
    """Recursive Factorial"""
    if number < 0:
        raise ValueError(f"Cant calculate Factorial for number: {number}")
    if not number:
        return 1

    if number == 1:
        return number
    return number * factorial(number - 1)



def series_length_check(series_length):
    """Series length check"""
    if series_length <= 0:
        raise ValueError("Can't Calculate Maclaurin Series for negative amount of steps")

def process_to_origins_matrix(x_values, y_values):
    """Convert arrays of X and Y to one (x;y) Matrix"""
    if len(x_values) != len(y_values):
        raise ValueError(f"Unable to create origins matrix from 2 different sized arrays: {len(x_values)} and {len(y_values)} ")
    result_matrix = [x_values, y_values]
    return transpose_matrix(classic_to_vector(result_matrix))

def maclaurin_exponent(series_length, x_value, appending_type=1):
    """Maclaurin series for e^x"""
    series_length_check(series_length)
    result_x = []
    result_y = []
    current_value = 0
    for i in range(series_length):
        result_x.append(i)
        if not appending_type:
            result_y.append((x_value ** i) / factorial(i))
        else:
            current_value+=(x_value ** i ) / factorial(i)
            result_y.append(current_value)
    return process_to_origins_matrix(result_x, result_y)


def maclaurin_cos(series_length, x_value, appending_type=1):
    """Maclaurin series for cos"""
    series_length_check(series_length)
    result_x = []
    result_y = []
    current_value = 0
    for i in range(series_length):
        result_x.append(i)
        value = ((-1)**i) / factorial(2*i) * x_value**(2*i)
        if not appending_type:
            result_y.append(value)
        else:
            current_value+=value
            result_y.append(current_value)
    return process_to_origins_matrix(result_x, result_y)

def maclaurin_sine(series_length, x_value, appending_type=1):
    series_length_check(series_length)
    result_x = []
    result_y = []
    current_value = 0
    for i in range(series_length):
        result_x.append(i)
        value = ((-1) ** i) / factorial(2 * i + 1) * x_value ** (2 * i + 1)
        if not appending_type:
            result_y.append(value)
        else:
            current_value += value
            result_y.append(current_value)
    return process_to_origins_matrix(result_x, result_y)



def maclaurin_arcsine(series_length, x_value, appending_type=1):
    """Maclaurin series for arcsin"""
    series_length_check(series_length)
    result_x = []
    result_y = []
    current_value = 0
    for i in range(series_length):
        result_x.append(i)
        value = factorial(2*i) / (4**i * factorial(i)**2 * (2*i + 1)) * x_value ** (2*i + 1)
        if not appending_type:
            result_y.append(value)
        else:
            current_value += value
            result_y.append(current_value)
    return process_to_origins_matrix(result_x, result_y)

def maclaurin_arccos(series_length, x_value, appending_type=1):
    """Maclaurin series for arccos"""
    series_length_check(series_length)
    result_x = [0]
    result_y = [math.pi - x_value]
    current_value = result_y[0]
    for i in range(1, series_length):
        result_x.append(i)
        value = result_y[i-1] - (factorial(2*i) / (4**i * factorial(i)**2 * (2*i + 1)) * x_value ** (2*i + 1))
        if not appending_type:
            result_y.append(value)
        else:
            current_value += value
            result_y.append(current_value)
    return process_to_origins_matrix(result_x, result_y)



def maclaurin_universal(series_length, x_value, function_name = 'sine', appending_type=1):
    """Universal Maclaurin Series calculating function"""
    value = 0
    series_length_check(series_length)
    is_supported_function(function_name)
    if function_name == 'arccos':
        result_x = [0]
        result_y = [math.pi - x_value]
        current_value = result_y[0]
        start_loop = 1
    else:
        result_x = []
        result_y = []
        current_value = 0
        start_loop = 0
    for i in range(start_loop, series_length):
        result_x.append(i)
        if function_name == 'arccos':
            value = result_y[i-1] - (factorial(2*i) / (4**i * factorial(i)**2 * (2*i + 1)) * x_value ** (2*i + 1))
        elif function_name == 'arcsin':
            value = factorial(2*i) / (4**i * factorial(i)**2 * (2*i + 1)) * x_value ** (2*i + 1)
        elif function_name == 'sin':
            value = ((-1) ** i) / factorial(2 * i + 1) * x_value ** (2 * i + 1)
        elif function_name == 'cos':
            value =  ((-1)**i) / factorial(2*i) * x_value**(2*i)
        elif function_name == 'exp':
            value = (x_value ** i) / factorial(i)
        if not appending_type:
            result_y.append(value)
        else:
            current_value += value
            result_y.append(current_value)
    return process_to_origins_matrix(result_x, result_y)





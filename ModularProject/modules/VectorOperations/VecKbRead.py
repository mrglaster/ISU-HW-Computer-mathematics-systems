"""

Functions for reading vectors from the keyboard

"""
import collections.abc
from modules.VectorOperations.UniversalVectorClass import UniversalVector


def parse_2vec():
    """Reads an array of data from the command line in the format: n values the vector v1 and n for v2"""
    input_string = input()
    arr_values = input_string.split()
    if len(arr_values) % 2 != 0 or len(arr_values) <= 2:
        raise ValueError(
            "Wrong argument dimension: amount of input arguments must be even >2 number "
        )
    arr_values = [int(numeric_string) for numeric_string in arr_values]
    int_vecdims = int(len(arr_values) / 2)
    vec_1 = UniversalVector(int_vecdims)
    vec_2 = UniversalVector(int_vecdims)
    for i in range(int_vecdims):
        vec_1.set_dimval(i, arr_values[i])
    cntr = 0
    for i in range(int_vecdims, len(arr_values)):
        vec_2.set_dimval(cntr, arr_values[i])
        cntr += 1
    return vec_1, vec_2


def parse_1vec():
    """same as parse_2vec for one vector only"""
    input_string = input()
    arr_values = [int(numeric_string) for numeric_string in input_string.split()]
    if len(arr_values) == 0:
        raise ValueError("Excepted as minimum 1 input argument")
    int_vecdims = len(arr_values)
    vec_1 = UniversalVector(int_dimensions=int_vecdims)
    for i in range(int_vecdims):
        vec_1.set_dimval(i, arr_values[i])
    return vec_1


def parse_1vec_parametrised(amount, debug=False):
    """Reads a vector of a certain length"""
    input_string = input()
    arr_values = [int(numeric_string) for numeric_string in input_string.split()]
    int_vecdims = len(arr_values)
    if int_vecdims != amount or int_vecdims == 0:
        raise ValueError("Wrong input arguments data")
    vec_1 = UniversalVector(int_dimensions=int_vecdims)
    for i in range(int_vecdims):
        vec_1.set_dimval(i, arr_values[i])
    return vec_1


def array_to_vec(array):
    """Преобразует массив в вектор"""
    int_vecdims = len(array)
    if int_vecdims == 0:
        raise ValueError("Wrong vector dimensions count: <=0")
    vec_1 = UniversalVector(int_dimensions=int_vecdims)
    for i in range(int_vecdims):
        vec_1.set_dimval(i, int(array[i]))
    return vec_1


def is_array(array):
    """Converts an array to a vector"""
    return isinstance(array, collections.abc.Sequence)


def vec_to_array(vector):
    """Convert vector to array"""
    array = []
    if len(vector) <= 0:
        raise ValueError("Incorrect vector")
    if is_array(vector):
        return vector
    for i in range(len(vector)):
        array.append(vector.get_dimval(i))
    return array

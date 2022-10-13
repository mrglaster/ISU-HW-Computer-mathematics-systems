"""

Функции для считывания векторов с клавиатуры

"""
import collections.abc
from .UniversalVectorClass import UniversalVector


def parse_2vec():
    """Считывает масив данных с командной строки в формате: n значений вектора v1 и n для v2"""
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
    """то же самое, что и parse_2vec, только для одного вектора"""
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
    """Считывает вектор определённой длины"""
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
    """Является ли значение переменной массивом"""
    return isinstance(array, collections.abc.Sequence)


def vec_to_array(vector):
    """Преобразовать вектор в массив"""
    array = []
    if len(vector) <= 0:
        raise ValueError("Incorrect vector")
    if is_array(vector):
        return vector
    for i in range(len(vector)):
        array.append(vector.get_dimval(i))
    return array

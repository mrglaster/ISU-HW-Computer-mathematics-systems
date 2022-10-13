"""
Базовые операции с векторами. Деление, умножение итд.
"""

from math import sqrt
from math import acos
from .UniversalVectorClass import *
from .VecInSpace import *


def vec_summ(vec_1, vec_2, debug=0):
    """ Сумма векторов одинаковой размерности """
    if not dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    vec_3 = UniversalVector(vec_1.get_dimensions())
    for i in range(0, vec_1.get_dimensions()):
        vec_3.set_dimval(i, vec_1.get_dimval(i) + vec_2.get_dimval(i))
    if debug:
        print(f"Vector sum result: {vec_3}")
    return vec_3


def vec_diff(vec_1, vec_2, debug=0):
    """ Разность векторов одинаковой размерности"""
    if not dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    vec_3 = UniversalVector(vec_1.get_dimensions())
    for i in range(0, vec_1.get_dimensions()):
        vec_3.set_dimval(i, vec_1.get_dimval(i) - vec_2.get_dimval(i))
    if debug:
        print(f"Vector difference result: {vec_3}")
    return vec_3


def vec_mulnum(vec_1, int_scalar, debug=0):
    """  Уменожение вектора на число"""
    if not vector_exists(vec_1):
        raise ValueError("Vector doesn't exist!")
    vec_3 = vec_1
    for i in range(vec_1.get_dimensions()):
        vec_3.set_dimval(i, vec_1.get_dimval(i) * int_scalar)
    if debug:
        print(f"Vector scalar multiply result: {vec_3}")
    return vec_3


def vec_divnum(vec_1, int_scalar, debug=0):
    """  Деление вектора на число """
    if not vector_exists(vec_1):
        raise ValueError("Vector doesn't exist")
    vec_3 = vec_1
    for i in range(vec_1.get_dimensions()):
        if int_scalar == 0:
            raise ValueError("Divide by zero error!")
        vec_3.set_dimval(i, vec_1.get_dimval(i) / int_scalar)
    if not debug:
        print(f"Vector scalar divide result: {vec_3}")
    return vec_3


def vec_mulscalar(vec_1, vec_2):
    """  Скалярное произведение векторов """
    if not dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    scval = 0
    for i in range(vec_1.get_dimensions()):
        scval += vec_1.get_dimval(i) * vec_2.get_dimval(i)
    return scval


def vec_modulo(vec_1):
    """  Длина вектора """
    if not vector_exists(vec_1):
        raise ValueError("Vector doesn't exist!")
    counter = 0
    for i in range(vec_1.get_dimensions()):
        counter += vec_1.get_dimval(i) ** 2
    return sqrt(counter)

"""
Базовые операции с векторами. Деление, умножение итд.
"""

from math import sqrt
from math import acos
from modules.vector_operations.universal_vector_class import *
from modules.vector_operations.vec_in_space import *
from modules.matrix_operations.matrix_parameters import array_to_vec

def vec_summ(vec_1, vec_2, debug=0):
    """ The sum of vectors of the same dimension amount """
    dimensions_allowence(vec_1, vec_2)
    vec_3 = UniversalVector(vec_1.get_dimensions())
    for i in range(0, vec_1.get_dimensions()):
        vec_3.set_dimval(i, vec_1.get_dimval(i) + vec_2.get_dimval(i))
    if debug:
        print(f"Vector sum result: {vec_3}")
    return vec_3


def vec_diff(vec_1, vec_2, debug=0):
    """ The difference of vectors of the same dimension amount"""
    dimensions_allowence(vec_1, vec_2)
    vec_3 = UniversalVector(len(vec_1))
    for i in range(vec_1.get_dimensions()):
        vec_3.set_dimval(i, vec_1.get_dimval(i) - vec_2.get_dimval(i))
    if debug:
        print(f"Vector difference result: {vec_3}")
    return vec_3


def vec_mulnum(vec_1, int_scalar, debug=0):
    """  Multiplying a vector by a number """

    vector_existance(vec_1)
    vec_3 = vec_1
    for i in range(len(vec_3)):
        vec_3.set_dimval(i, vec_3.get_dimval(i)*int_scalar)
    if debug:
        print(f"Vector scalar multiply result: {vec_3}")
    return vec_3


def vec_divnum(vec_1, int_scalar, debug=0):
    """  Divide a vector by a number """
    vector_existance(vec_1)
    vec_3 = vec_1
    for i in range(vec_1.get_dimensions()):
        if int_scalar == 0:
            raise ValueError("Divide by zero error!")
        vec_3.set_dimval(i, vec_1.get_dimval(i) / int_scalar)
    if debug:
        print(f"Vector scalar divide result: {vec_3}")
    return vec_3


def vec_mulscalar(vec_1, vec_2):
    """  Dot product of vectors """
    dimensions_allowence(vec_1, vec_2)
    scval = 0
    for i in range(vec_1.get_dimensions()):
        scval += vec_1.get_dimval(i) * vec_2.get_dimval(i)
    return scval


def vec_modulo(vec_1):
    """  Vector's coordinate length """
    vector_existance(vec_1)
    counter = 0
    for i in range(vec_1.get_dimensions()):
        counter += vec_1.get_dimval(i) ** 2
    return sqrt(counter)

def vector_existance(vec_1):
    """Does the vector exist?"""
    if not vector_exists(vec_1):
        raise ValueError("Vector doesn't exist!")
    return True

def dimensions_allowence(vec_1, vec_2):
    """Checking the validity of an operation between two vectors"""
    if not dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    return True


def vec_power(vector, power):
    """Powers all values of vector"""
    vector_existance(vector)
    result = []
    for i in range(len(vector)):
        result.append(pow(vector[i], power))
    return array_to_vec(result)

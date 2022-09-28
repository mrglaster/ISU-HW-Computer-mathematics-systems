"""
Базовые операции с векторами. Деление, умножение итд.
"""

from .UniversalVectorClass import *
from .VecInSpace import *

#Сумма векторов одинаковой размерности
def vec_summ(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    vec_3 =  UniversalVector(vec_1.get_dimensions())
    for i in range(0, vec_1.get_dimensions()):
        vec_3.set_dimval(i, vec_1.get_dimval(i)+vec_2.get_dimval(i))
    print(f"Vector sum result: {vec_3}")
    return vec_3

#Разность векторов одинаковой размерности
def vec_diff(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    vec_3 = UniversalVector(vec_1.get_dimensions())
    for i in range(0, vec_1.get_dimensions()):
        vec_3.set_dimval(i, vec_1.get_dimval(i)-vec_2.get_dimval(i))
    print(f"Vector difference result: {vec_3c}")
    return vec_3

#Уменожение вектора на число
def vec_mulnum(vec_1, int_scalar):
    if not vector_exists(vec_1):
        return None
    vec_3 = vec_1
    for i in range(vec_1.get_dimensions()):
        vec_3.set_dimval(i, vec_1.get_dimval(i)*int_scalar)
    print(f"Vector scalar multiply result: {vec_3}")
    return vec_3

#Деление вектора на число
def vec_divnum(vec_1, int_scalar):
    if not vector_exists(vec_1):
        return None
    vec_3 = vec_1
    for i in range(vec_1.get_dimensions()):
        vec_3.set_dimval(i, vec_1.get_dimval(i)/int_scalar)
    print(f"Vector scalar divide result: {vec_3}")
    return vec_3
#Скалярное произведение векторов
def vec_mulscalar(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    scval = 0
    for i in range(vec_1.get_dimensions()):
        scval+=vec_1.get_dimval(i)*vec_2.get_dimval(i)
    return scval

#Длина вектора
def vec_modulo(vec_1):
    if not vector_exists(vec_1):
        return None
    counter = 0
    for i in range(vec_1.get_dimensions()):
        counter+= vec_1.get_dimval(i)**2
    return sqrt(counter)
    
"""
Вектора в пространстве: сонаправленность, коллинеарность итд.
"""

from .UniversalVectorClass import *
from .VecBasicOperations import *

# Коллинеарность векторов. На входе - 2 объекта класса UniversalVector
def vec_colinearcheck(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        print("Wrong dimensions amount!")
        return False
    colines = []
    for i in range(vec_1.get_dimensions()):
        colines.append(vec_1.get_dimval(i)/vec_2.get_dimval(i))
    cur = colines[0]
    for i in colines:
        if i != cur:
            return False
    return True

#Проверка сонаправленности двух векторов
def vec_codircheck(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    if  vec_colinearcheck(vec_1, vec_2) and vec_mulscalar(vec_1, vec_2)>0 :
        return True
    return False
#Являются ли векторы противоположнонаправленными
def vec_contradircheck(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    if vec_colinearcheck(vec_1, vec_2) and vec_mulscalar(vec_1, vec_2)<0:
        return True
    return False

#Проверка на равенство векторов
def vec_par(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return False
    if vec_codircheck(vec_1, vec_2) and vec_modulo(vec_1) == vec_modulo(vec_2):
        return True
    return False
#Проверка на равенство векторов с заданной точностью
def vec_par_param(vec_1, vec_2, paramater):
    if not vector_exists(vec_1) or not vector_exists(vec_2):
        print("Vector existance error!")
        return None
    for i in range(vec_1.get_dimensions()):
        if abs(vec_1.get_dimval(i) - vec_2.get_dimval(i))>=paramater:
            return False
    return True
    
#Ортогональны ли вектора
def vec_ortogonalcheck(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    if vec_mulscalar(vec_1, vec_2) ==0:
        return True
    return False

#Нормализация вектора
def vec_normalize(vec_1):
    if not vector_exists(vec_1):
        return None
    return vec_divnum(vec_1, vec_modulo(vec_1))

#Инверсия вектора
def vec_invercevec(vec_1):
    if not vector_exists(vec_1):
        return None
    return vec_mulnum(vec_1, -1)

#Угол между векторами. Ответ в радианах
def vec_angle_bv_rad(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    return arccos(vec_cosbv(vec_1, vec_2))

#Угол между векторами. Ответ в градусах
def vec_angle_bv_angle(vec_1, vec_2):
    return vec_angle_bv_rad(vec_1, vec_2)*(180/pi)

#Косинус между векторами
def vec_cosbv(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    return vec_mulscalar(vec_1, vec_2) / (vec_modulo(vec_1)*vec_modulo(vec_2))     

#Скалярная проекция вектора 1 на вектор 2
def vec_projection_scalar(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    #Проекция вектора 1 на вектор 2
    return vec_mulscalar(vec_1, vec_2)/vec_modulo(vec_2)

#Векторная проекция вектора 1 на вектор 2
def vec_projection_vector(vec_1, vec_2):
    if not dimensions_check(vec_1, vec_2):
        return None
    return vec_mulnum(vec_1, vec_projection_scalar(vec_1, vec_2))
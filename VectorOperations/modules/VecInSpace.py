"""
Вектора в пространстве: сонаправленность, коллинеарность итд.
"""
from math import sqrt
from math import acos
from math import pi

import modules.VecBasicOperations as Vbo
import modules.UniversalVectorClass as Uvc


# Коллинеарность векторов. На входе - 2 объекта класса UniversalVector
def vec_colinearcheck(vec_1, vec_2):
    if not Uvc.dimensions_check(vec_1, vec_2):
        print("Wrong dimensions amount!")
        return False
    colines = []
    for i in range(vec_1.get_dimensions()):
        if vec_2.get_dimval(i) == 0:
            return False
        colines.append(vec_1.get_dimval(i) / vec_2.get_dimval(i))
    cur = colines[0]
    for i in colines:
        if i != cur:
            return False
    return True


# Проверка сонаправленности двух векторов
def vec_codircheck(vec_1, vec_2):
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    if vec_colinearcheck(vec_1, vec_2) and vec_mulscalar(vec_1, vec_2) > 0:
        return True
    return False


# Являются ли векторы противоположнонаправленными
def vec_contradircheck(vec_1, vec_2):
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    if vec_colinearcheck(vec_1, vec_2) and vec_mulscalar(vec_1, vec_2) < 0:
        return True
    return False


# Проверка на равенство векторов
def vec_par(vec_1, vec_2):
    if not Uvc.dimensions_check(vec_1, vec_2):
        return False
    if vec_codircheck(vec_1, vec_2) and vec_modulo(vec_1) == vec_modulo(vec_2):
        return True
    return False


# Проверка на равенство векторов с заданной точностью
def vec_par_param(vec_1, vec_2, paramater):
    if not Uvc.vector_exists(vec_1) or not Uvc.vector_exists(vec_2):
        raise ValueError("Vector doesn't exist!")
    for i in range(vec_1.get_dimensions()):
        if abs(vec_1.get_dimval(i) - vec_2.get_dimval(i)) >= paramater:
            return False
    return True


# Ортогональны ли вектора
def vec_ortogonalcheck(vec_1, vec_2):
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    if Vbo.vec_mulscalar(vec_1, vec_2) == 0:
        return True
    return False


# Нормализация вектора
def vec_normalize(vec_1):
    if not Uvc.vector_exists(vec_1):
        raise ValueError("Vector doesn't exist!")
    return Vbo.vec_divnum(vec_1, Vbo.vec_modulo(vec_1))


# Инверсия вектора
def vec_invercevec(vec_1):
    if not Uvc.vector_exists(vec_1):
        raise ValueError("Vector doesn't exist!")
    return Vbo.vec_mulnum(vec_1, -1)


# Угол между векторами. Ответ в радианах
def vec_angle_bv_rad(vec_1, vec_2):
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    return acos(Vbo.vec_cosbv(vec_1, vec_2))


# Угол между векторами. Ответ в градусах
def vec_angle_bv_angle(vec_1, vec_2):
    return vec_angle_bv_rad(vec_1, vec_2) * (180 / pi)


# Косинус между векторами
def vec_cosbv(vec_1, vec_2):
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    return Vbo.vec_mulscalar(vec_1, vec_2) / (
        Vbo.vec_modulo(vec_1) * Vbo.vec_modulo(vec_2)
    )


# Скалярная проекция вектора 1 на вектор 2
def vec_projection_scalar(vec_1, vec_2):
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    # Проекция вектора 1 на вектор 2
    return Vbo.vec_mulscalar(vec_1, vec_2) / Vbo.vec_modulo(vec_2)


# Векторная проекция вектора 1 на вектор 2
def vec_projection_vector(vec_1, vec_2):
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    return Vbo.vec_mulnum(vec_1, vec_projection_scalar(vec_1, vec_2))

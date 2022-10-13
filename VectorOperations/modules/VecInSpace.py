"""
Вектора в пространстве: сонаправленность, коллинеарность итд.
"""
from math import sqrt
from math import acos
from math import pi

import modules.VecBasicOperations as Vbo
import modules.UniversalVectorClass as Uvc


def vec_colinearcheck(vec_1, vec_2):
    """Коллинеарность векторов. На входе - 2 объекта класса UniversalVector"""
    if not Uvc.dimensions_check(vec_1, vec_2):
        print("Wrong dimensions amount!")
        return False
    colines = []
    for i in range(vec_1.get_dimensions()):
        if vec_2.get_dimval(i) == 0:
            return False
        # ???????
        colines.append(vec_1.get_dimval(i) / vec_2.get_dimval(i))
    cur = colines[0]
    for i in colines:
        if i != cur:
            return False
    return True


def vec_codircheck(vec_1, vec_2):
    """Проверка на сонаправленность векторов"""
    return vec_cosbv(vec_1,vec_2) == 1

def vec_contradircheck(vec_1, vec_2):
    """Проверка на противоположнонаправленность"""
    return vec_cosbv(vec_1, vec_2) == -1

def vec_par(vec_1, vec_2):
    """Проверка на равенство векторов"""
    if not Uvc.dimensions_check(vec_1, vec_2):
        return False
    if vec_codircheck(vec_1, vec_2) and vec_modulo(vec_1) == vec_modulo(vec_2):
        return True
    return False


def vec_par_param(vec_1, vec_2, paramater):
    """Проверка на равенство векторов с заданной точностью"""
    if not Uvc.vector_exists(vec_1) or not Uvc.vector_exists(vec_2):
        raise ValueError("Vector doesn't exist!")
    for i in range(vec_1.get_dimensions()):
        if abs(vec_1.get_dimval(i) - vec_2.get_dimval(i)) >= paramater:
            return False
    return True


def vec_ortogonalcheck(vec_1, vec_2):
    """Ортогональны ли вектора"""
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    if Vbo.vec_mulscalar(vec_1, vec_2) == 0:
        return True
    return False


def vec_normalize(vec_1):
    """Нормализация вектора"""
    if not Uvc.vector_exists(vec_1):
        raise ValueError("Vector doesn't exist!")
    return Vbo.vec_divnum(vec_1, Vbo.vec_modulo(vec_1))


def vec_invercevec(vec_1):
    """Инверсия вектора"""
    if not Uvc.vector_exists(vec_1):
        raise ValueError("Vector doesn't exist!")
    return Vbo.vec_mulnum(vec_1, -1)


def vec_angle_bv_rad(vec_1, vec_2):
    """Угол между векторами. Ответ в радианах"""
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    return acos(Vbo.vec_cosbv(vec_1, vec_2))


def vec_angle_bv_angle(vec_1, vec_2):
    """Угол между векторами. Ответ в градусах"""
    return vec_angle_bv_rad(vec_1, vec_2) * (180 / pi)


def vec_cosbv(vec_1, vec_2):
    """Косинус между векторами"""
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    return Vbo.vec_mulscalar(vec_1, vec_2) / (
        Vbo.vec_modulo(vec_1) * Vbo.vec_modulo(vec_2)
    )


def vec_projection_scalar(vec_1, vec_2):
    """Скалярная проекция вектора 1 на вектор 2"""
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    # Проекция вектора 1 на вектор 2
    return Vbo.vec_mulscalar(vec_1, vec_2) / Vbo.vec_modulo(vec_2)


def vec_projection_vector(vec_1, vec_2):
    """Векторная проекция вектора 1 на вектор 2"""
    if not Uvc.dimensions_check(vec_1, vec_2):
        raise ValueError(
            f"Dimensions of vectors don't coincide: {vec_1.get_dimensions()} and {vec_2.get_dimensions()}"
        )
    return Vbo.vec_mulnum(vec_2, vec_projection_scalar(vec_1, vec_2)/Vbo.vec_modulo(vec_2))

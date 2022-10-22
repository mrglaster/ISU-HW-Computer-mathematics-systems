"""
Вектора в пространстве: сонаправленность, коллинеарность итд.
"""
from math import sqrt
from math import acos
from math import pi

import modules.VectorOperations.VecBasicOperations as Vbo
import modules.VectorOperations.UniversalVectorClass as Uvc


def vec_colinearcheck(vec_1, vec_2):
    """Collinearity of vectors. At the input - 2 objects of the UniversalVector class"""
    Vbo.dimensions_allowence(vec_1, vec_2)
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
    """Checking for codirectionality of vectors"""
    return vec_cosbv(vec_1,vec_2) == 1

def vec_contradircheck(vec_1, vec_2):
    """Check for opposite direction"""
    return vec_cosbv(vec_1, vec_2) == -1

def vec_par(vec_1, vec_2):
    """Проверка на равенство векторов"""
    if not Uvc.dimensions_check(vec_1, vec_2):
        return False
    if vec_codircheck(vec_1, vec_2) and vec_modulo(vec_1) == vec_modulo(vec_2):
        return True
    return False


def vec_par_param(vec_1, vec_2, paramater):
    """Checking for equality of vectors with a given precision"""
    vector_existance(vec_1)
    vector_existance(vec_2)
    for i in range(vec_1.get_dimensions()):
        if abs(vec_1.get_dimval(i) - vec_2.get_dimval(i)) >= paramater:
            return False
    return True


def vec_ortogonalcheck(vec_1, vec_2):
    """Are the vectors orthogonal?"""
    Vbo.dimensions_allowence(vec_1=vec_1, vec_2=vec_2)
    if Vbo.vec_mulscalar(vec_1, vec_2) == 0:
        return True
    return False


def vec_normalize(vec_1):
    """Vector normalization"""
    Vbo.vector_existance(vec_1)
    return Vbo.vec_divnum(vec_1, Vbo.vec_modulo(vec_1))


def vec_invercevec(vec_1):
    """Vector inversion"""
    Vbo.vector_existance(vec_1)
    return Vbo.vec_mulnum(vec_1, -1)


def vec_angle_bv_rad(vec_1, vec_2):
    """Angle between vectors. Answer in radians"""
    Vbo.dimensions_allowence(vec_1, vec_2)
    return acos(Vbo.vec_cosbv(vec_1, vec_2))


def vec_angle_bv_angle(vec_1, vec_2):
    """Angle between vectors. Answer in degrees"""
    return vec_angle_bv_rad(vec_1, vec_2) * (180 / pi)


def vec_cosbv(vec_1, vec_2):
    """Cosine between vectors"""
    Vbo.dimensions_allowence(vec_1, vec_2)
    return Vbo.vec_mulscalar(vec_1, vec_2) / (
        Vbo.vec_modulo(vec_1) * Vbo.vec_modulo(vec_2)
    )


def vec_projection_scalar(vec_1, vec_2):
    """Scalar projection of vector 1 onto vector 2"""
    Vbo.dimensions_allowence(vec_1, vec_2)
    return Vbo.vec_mulscalar(vec_1, vec_2) / Vbo.vec_modulo(vec_2)


def vec_projection_vector(vec_1, vec_2):
    """Vector projection of vector 1 onto vector 2"""
    Vbo.dimensions_allowence(vec_1, vec_2)
    return Vbo.vec_mulnum(vec_2, vec_projection_scalar(vec_1, vec_2)/Vbo.vec_modulo(vec_2))
from modules import VecKbRead
from modules import UniversalVectorClass
from modules import VecBasicOperations
from modules import VecInSpace


def test_add_vectors():
    """Сложение векторов"""
    a = VecKbRead.array_to_vec([1, 2, 5])
    b = VecKbRead.array_to_vec([4, 8, 1])
    exp = VecKbRead.array_to_vec([5, 10, 6])
    assert exp == VecBasicOperations.vec_summ(a, b)


def test_sub_vectors():
    """Вычитание векторов"""
    a = VecKbRead.array_to_vec([1, 2, 5])
    b = VecKbRead.array_to_vec([4, 8, 1])
    exp = VecKbRead.array_to_vec([-3, -6, 4])
    assert exp == VecBasicOperations.vec_diff(a, b, 1)


def test_mul_vec():
    """Скалярное произведение векторов"""
    a = VecKbRead.array_to_vec([1, 2, -5, 2])
    b = VecKbRead.array_to_vec([4, 8, 1, -2])
    ans = 11
    assert ans == VecBasicOperations.vec_mulscalar(a, b)

def test_angle_bvectors():
    """Угол между векторами"""
    a = VecKbRead.array_to_vec([3, 4])
    b = VecKbRead.array_to_vec([4, 3])
    ans = 16.26
    assert int(ans * 100) == int(VecInSpace.vec_angle_bv_angle(a, b) * 100)


def test_proj_scale():
    """Скалярная проекция векторов"""
    a = VecKbRead.array_to_vec([1, 2])
    b = VecKbRead.array_to_vec([3, 4])
    ans = 2.2
    assert ans == VecInSpace.vec_projection_scalar(a, b)


def test_proj_vec():
    """Векторная проекция векторов"""
    a = VecKbRead.array_to_vec([4, 5])
    b = VecKbRead.array_to_vec([6, 0])
    ans = VecKbRead.array_to_vec([4, 0])
    assert ans == VecInSpace.vec_projection_vector(a, b)


def test_mul_scale():
    """Умножение вектора на число"""
    a = VecKbRead.array_to_vec([2, 5])
    num = 5
    ans = VecKbRead.array_to_vec([10, 25])
    assert ans == VecBasicOperations.vec_mulnum(a, num)


def test_div_scale():
    """Деление вектора на число"""
    a = VecKbRead.array_to_vec([8, 16])
    num = 8
    ans = VecKbRead.array_to_vec([1, 2])
    assert ans == VecBasicOperations.vec_divnum(a, num)


def test_is_collinear():
    """Проверка на коллинеарность"""
    a = VecKbRead.array_to_vec([2, 6, -3])
    b = VecKbRead.array_to_vec([6, 18, -9])
    ans = True
    assert ans == VecInSpace.vec_colinearcheck(a, b)


def test_codircheck():
    """Проверка на сонаправленность"""
    a = VecKbRead.array_to_vec([2, 6, -3])
    b = VecKbRead.array_to_vec([6, 18, -9])
    ans = True
    assert ans == VecInSpace.vec_codircheck(a, b)


def test_contradircheck():
    """Проверка на противоположнонаправленность"""
    a = VecKbRead.array_to_vec([2, 6, -3])
    b = VecKbRead.array_to_vec([6, 18, -9])
    ans = False
    assert ans == VecInSpace.vec_contradircheck(a, b)


def test_normalisation():
    """Нормализация вектора"""
    a = VecKbRead.array_to_vec([-3, -4])
    ans = VecKbRead.array_to_vec([-0.6, -0.8])
    assert ans == VecBasicOperations.vec_normalize(a)


def test_cos_bvec():
    """Косинус между векторами"""
    a = VecKbRead.array_to_vec([3, 4])
    b = VecKbRead.array_to_vec([4, 3])
    ans = 0.96
    assert ans == VecInSpace.vec_cosbv(a, b)

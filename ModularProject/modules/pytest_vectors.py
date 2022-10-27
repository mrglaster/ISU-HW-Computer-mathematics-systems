from modules.vector_operations import vec_io
from modules.vector_operations import universal_vector_class
from modules.vector_operations import vec_basic_operations
from modules.vector_operations import vec_in_space


def test_add_vectors():
    """Сложение векторов"""
    a = vec_io.array_to_vec([1, 2, 5])
    b = vec_io.array_to_vec([4, 8, 1])
    exp = vec_io.array_to_vec([5, 10, 6])
    assert exp == vec_basic_operations.vec_summ(a, b)


def test_sub_vectors():
    """Вычитание векторов"""
    a = vec_io.array_to_vec([1, 2, 5])
    b = vec_io.array_to_vec([4, 8, 1])
    exp = vec_io.array_to_vec([-3, -6, 4])
    assert exp == vec_basic_operations.vec_diff(a, b, 1)


def test_mul_vec():
    """Скалярное произведение векторов"""
    a = vec_io.array_to_vec([1, 2, -5, 2])
    b = vec_io.array_to_vec([4, 8, 1, -2])
    ans = 11
    assert ans == vec_basic_operations.vec_mulscalar(a, b)

def test_angle_bvectors():
    """Угол между векторами"""
    a = vec_io.array_to_vec([3, 4])
    b = vec_io.array_to_vec([4, 3])
    ans = 16.26
    assert int(ans * 100) == int(vec_in_space.vec_angle_bv_angle(a, b) * 100)


def test_proj_scale():
    """Скалярная проекция векторов"""
    a = vec_io.array_to_vec([1, 2])
    b = vec_io.array_to_vec([3, 4])
    ans = 2.2
    assert ans == vec_in_space.vec_projection_scalar(a, b)


def test_proj_vec():
    """Векторная проекция векторов"""
    a = vec_io.array_to_vec([4, 5])
    b = vec_io.array_to_vec([6, 0])
    ans = vec_io.array_to_vec([4, 0])
    assert ans == vec_in_space.vec_projection_vector(a, b)


def test_mul_scale():
    """Умножение вектора на число"""
    a = vec_io.array_to_vec([2, 5])
    num = 5
    ans = vec_io.array_to_vec([10, 25])
    assert ans == vec_basic_operations.vec_mulnum(a, num)


def test_div_scale():
    """Деление вектора на число"""
    a = vec_io.array_to_vec([8, 16])
    num = 8
    ans = vec_io.array_to_vec([1, 2])
    assert ans == vec_basic_operations.vec_divnum(a, num)


def test_is_collinear():
    """Проверка на коллинеарность"""
    a = vec_io.array_to_vec([2, 6, -3])
    b = vec_io.array_to_vec([6, 18, -9])
    ans = True
    assert ans == vec_in_space.vec_colinearcheck(a, b)


def test_codircheck():
    """Проверка на сонаправленность"""
    a = vec_io.array_to_vec([2, 6, -3])
    b = vec_io.array_to_vec([6, 18, -9])
    ans = True
    assert ans == vec_in_space.vec_codircheck(a, b)


def test_contradircheck():
    """Проверка на противоположнонаправленность"""
    a = vec_io.array_to_vec([2, 6, -3])
    b = vec_io.array_to_vec([6, 18, -9])
    ans = False
    assert ans == vec_in_space.vec_contradircheck(a, b)


def test_normalisation():
    """Нормализация вектора"""
    a = vec_io.array_to_vec([-3, -4])
    ans = vec_io.array_to_vec([-0.6, -0.8])
    assert ans == vec_basic_operations.vec_normalize(a)


def test_cos_bvec():
    """Косинус между векторами"""
    a = vec_io.array_to_vec([3, 4])
    b = vec_io.array_to_vec([4, 3])
    ans = 0.96
    assert ans == vec_in_space.vec_cosbv(a, b)

from math import sqrt
from math import acos
from modules import VecKbRead
from modules import UniversalVectorClass
from modules import VecBasicOperations
from modules import VecInSpace
from modules import TestUtilities
from random import randint


def one_veclog(vec1, i, result, name, logmode):
    TestUtilities.write_monovec_log(
        test_id=i + 1,
        vector_test=vec1,
        operation_name=name,
        result=str(result),
        mode=logmode,
        testseries_name=name + "_test",
        consolename="",
    )


def two_veclog(vec1, vec2, i, result, name, logmode):
    TestUtilities.write_polyvec_log(
        test_id=i + 1,
        vector_test1=vec1,
        vector_test2=vec2,
        operation_name=name,
        result=str(result),
        mode=logmode,
        testseries_name=name + "_test",
        consolename="",
    )


def vector_summ_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "SUMM"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecBasicOperations.vec_summ(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def vector_diff_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "DIFF"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecBasicOperations.vec_diff(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def vector_mulnum_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "MULL_SCALAR"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        num = randint(-100, 100)
        result = VecBasicOperations.vec_mulnum(vec_1=vec1, int_scalar=num)
        one_veclog(vec1, i, result, name, logmode)


def vector_divnum_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "DIV_SCALAR"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        num = randint(-100, 100)
        result = VecBasicOperations.vec_divnum(vec_1=vec1, int_scalar=num)
        one_veclog(vec1, i, result, name, logmode)


def vector_vecscalarmul(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "VEC_SCALAR_MUL"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecBasicOperations.vec_mulscalar(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def vector_modulo_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "VEC_MODULO"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        result = VecBasicOperations.vec_modulo(vec1)
        one_veclog(vec1, i, result, name, logmode)


def vector_colinear_check_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "COLINEAR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_colinearcheck(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def vector_codir_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "CODIR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_codircheck(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def vector_contradir_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "CONTRADIR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_contradircheck(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def vec_par_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "PAR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_par(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def vec_par_parametred_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "PAR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_par_param(vec1, vec2, randint(1, 100))
        two_veclog(vec1, vec2, i, result, name, logmode)


def vec_ortogonal_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "ORTOGONAL_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_ortogonalcheck(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def vec_normalize_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "VEC_NORMALIZE"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        result = VecInSpace.vec_normalize(vec1)
        one_veclog(vec1, i, result, name, logmode)


def vec_invert_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "VEC_INVERT"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        result = VecInSpace.vec_invercevec(vec1)
        one_veclog(vec1, i, result, name, logmode)


def vec_angle_bv_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    NAME1 = "ANGL_B_VEC_RAD"
    NAME2 = "ANGL_B_VEC_ANGL"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 40))
        result1 = VecInSpace.vec_angle_bv_rad(vec1, vec2)
        result2 = VecInSpace.vec_angle_bv_angle(vec1, vec2)
        two_veclog(vec1, vec2, i, result1, NAME1, logmode)
        two_veclog(vec1, vec2, i, result2, NAME2, logmode)


def vec_cos_bv_check(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "COS_B_VEC"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_cosbv(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)

def vec_projection_scalar_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "VEC_PROJECTION_SCALAR"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(1, 30))
        result = VecInSpace.vec_projection_scalar(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def vec_projection_vector_test(test_amount, logmode=TestUtilities.WRITE_LOG_TO_CONSOLE):
    name = "VEC_PROJECTION_VECTOR"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(1, 30))
        result = VecInSpace.vec_projection_vector(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)


def start_tests():
    print("=" * 40)
    print("Test sequence #1 : sum test")
    print("=" * 40 + "\n" + "\n")
    vector_summ_test(5)
    print("=" * 40)
    print("Test sequence #2 : diff  test")
    print("=" * 40 + "\n" + "\n")
    vector_diff_test(5)
    print("=" * 40)
    print("Test sequence #3 : mulnum test")
    print("=" * 40 + "\n" + "\n")
    vector_mulnum_test(5)
    print("=" * 40)
    print("Test sequence #4 : divnum test")
    print("=" * 40 + "\n" + "\n")
    vector_divnum_test(5)
    print("=" * 40)
    print("Test sequence #5 : scalarmul  test")
    print("=" * 40 + "\n" + "\n")
    vector_vecscalarmul(5)
    print("=" * 40)
    print("Test sequence #6 : modulo test")
    print("=" * 40 + "\n" + "\n")
    vector_modulo_test(5)
    print("=" * 40)
    print("Test sequence #7 : colinear check test")
    print("=" * 40 + "\n" + "\n")
    vector_colinear_check_test(5)
    print("=" * 40)
    print("Test sequence #8 : contradir test")
    print("=" * 40 + "\n" + "\n")
    vector_contradir_test(5)
    print("=" * 40)
    print("Test sequence #9 : codir test")
    print("=" * 40 + "\n" + "\n")
    vector_codir_test(5)
    print("=" * 40)
    print("Test sequence #10 : par test")
    print("=" * 40 + "\n" + "\n")
    vec_par_test(5)
    print("=" * 40)
    print("Test sequence #11 : par parametred test")
    print("=" * 40 + "\n" + "\n")
    vec_par_parametred_test(5)
    print("=" * 40)
    print("Test sequence #12: ortogonal test")
    print("=" * 40 + "\n" + "\n")
    vec_ortogonal_test(5)
    print("=" * 40)
    print("Test sequence #13: normalize test")
    print("=" * 40 + "\n" + "\n")
    vec_normalize_test(5)
    print("=" * 40)
    print("Test sequence #14 : invert test")
    print("=" * 40 + "\n" + "\n")
    vec_invert_test(5)
    print("=" * 40)
    print("Test sequence #15 : angle bv test")
    print("=" * 40 + "\n" + "\n")
    vec_angle_bv_test(5)
    print("=" * 40)
    print("Test sequence #16 : cos bv test")
    print("=" * 40 + "\n" + "\n")
    vec_cos_bv_check(5)
    print("=" * 40)
    print("Test sequence #17 : proj vec  test")
    print("=" * 40 + "\n" + "\n")
    vec_projection_vector_test(5)
    print("=" * 40)
    print("Test sequence #18: proj scalar test")
    print("=" * 40 + "\n" + "\n")
    vec_projection_scalar_test(5)
    print("=" * 40)
    print("END OF TESTS")
    print("\n")


def main():
    start_tests()


if __name__ == "__main__":
    main()







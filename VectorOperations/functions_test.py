from modules import VecKbRead
from modules import UniversalVectorClass
from modules import VecBasicOperations
from modules import VecInSpace
from modules import TestUtilities
from random import randint



def one_veclog(vec1, i, result, name, logmode):
    TestUtilities.write_monovec_log(test_id=i + 1, vector_test=vec1, operation_name=name,
                                    result=str(result), mode=logmode, testseries_name=name + "_test", consolename='')

def two_veclog(vec1, vec2, i, result, name, logmode):
    TestUtilities.write_polyvec_log(test_id=i + 1, vector_test1=vec1, vector_test2=vec2, operation_name=name,
                                    result=str(result), mode=logmode, testseries_name=name + "_test", consolename='')

def vector_summ_test(test_amount, logmode):
    name = "SUMM"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecBasicOperations.vec_summ(vec1, vec2)
        two_veclog(vec1, vec2, i ,result, name, logmode )

def vector_diff_test(test_amount, logmode):
    name = "DIFF"
    for i in range(test_amount):
        vec1,vec2 = TestUtilities.vec_generate_samesizepair(randint(2,100))
        result = VecBasicOperations.vec_diff(vec1,vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)

def vector_mulnum_test(test_amount, logmode):
    name = "MULL_SCALAR"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        num = randint(-100,100)
        result = VecBasicOperations.vec_mulnum(vec_1=vec1,int_scalar=num)
        one_veclog(vec1,i,result,name,logmode)

def vector_divnum_test(test_amount, logmode):
    name = "DIV_SCALAR"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        num = randint(-100,100)
        result = VecBasicOperations.vec_divnum(vec_1=vec1,int_scalar=num)
        one_veclog(vec1,i,result,name,logmode)

def vector_vecscalarmul(test_amount, logmode):
    name = "VEC_SCALAR_MUL"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2,100))
        result = VecBasicOperations.vec_mulscalar(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logname)

def vector_modulo_test(test_amount, logmode):
    name = "VEC_MODULO"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        result = VecBasicOperations.vec_modulo(vec1)
        one_veclog(vec1,i,result,name,logmode)


def vector_colinear_check_test(test_amount, logmode):
    name = "COLINEAR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_colinearcheck(vec1,vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)

def vector_codir_test(test_amount, logmode):
    name = "CODIR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_codircheck(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)

def vector_contradir_test(test_amount, logmode):
    name = "CONTRADIR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_contradircheck(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)

def vec_par_test(test_amount, logmode):
    name="PAR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_par(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)

def vec_par_parametred_test(test_amount, logmode):
    name="PAR_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_par_param(vec1, vec2, randint(1,100))
        two_veclog(vec1, vec2, i, result, name, logmode)

def vec_ortogonal_test(test_amount, logmode):
    name="ORTOGONAL_CHECK"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2, 100))
        result = VecInSpace.vec_ortogonalcheck(vec1,vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)

def vec_normalize_test(test_amount, logmode):
    name = "VEC_NORMALIZE"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        result = VecInSpace.vec_normalize(vec1)
        one_veclog(vec1,i,result,name,logmode)

def vec_invert_test(test_amount, logmode):
    name = "VEC_INVERT"
    for i in range(test_amount):
        vec1 = TestUtilities.vec_generate_random()
        result = VecInSpace.vec_invercevec(vec1)
        one_veclog(vec1, i, result, name, logmode)

def vec_angle_bv_test(test_amount, logmode):
    NAME1 = "ANGL_B_VEC_RAD"
    NAME2 = "ANGL_B_VEC_ANGL"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(2,40))
        result1 = VecInSpace.vec_angle_bv_rad(vec1,vec2)
        result2 = VecInSpace.vec_angle_bv_angle(vec1, vec2)
        two_veclog(vec1,vec2, i,result1,NAME1,logmode)
        two_veclog(vec1,vec2,i,result2,NAME2,logmode)

def vec_cos_bv_check(test_amount,logmode):
    name = "COS_B_VEC"
    for i in range(test_amount):
        vec1,vec2 = TestUtilities.vec_generate_samesizepair(randint(2,100))
        result = VecInSpace.vec_cosbv(vec1, vec2)
        two_veclog(vec1,vec2,i,result,name,logmode)

def vec_projection_scalar_test(test_amount,logmode):
    name = "VEC_PROJECTION_SCALAR"
    for i in range(test_amount):
        vec1,vec2 = TestUtilities.vec_generate_samesizepair(randint(1,30))
        result = VecInSpace.vec_projection_scalar(vec1,vec2)
        two_veclog(vec1,vec2,i,result,name,logmode)

def vec_projection_vector_test(test_amount, logmode):
    name = "VEC_PROJECTION_VECTOR"
    for i in range(test_amount):
        vec1, vec2 = TestUtilities.vec_generate_samesizepair(randint(1, 30))
        result = VecInSpace.vec_projection_vector(vec1, vec2)
        two_veclog(vec1, vec2, i, result, name, logmode)

def main():
    #Пример теста
    vector_modulo_test(10, TestUtilities.WRITE_LOG_TO_CONSOLE)








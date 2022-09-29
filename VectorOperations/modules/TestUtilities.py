"""

Методы для тестирования функций.

"""

import sys
from random import randint
from .UniversalVectorClass import UniversalVector


# Константы для логирования
WRITE_LOG_TO_FILE = 1
WRITE_LOG_TO_CONSOLE = 0


# Генерация случайного вектора
def vec_generate_random():
    dimensions_count = randint(0, 100)
    random_vector = UniversalVector(dimensions_count)
    for i in range(dimensions_count):
        random_vector.set_dimval(i, randint(-100,100))
    return random_vector

# Генерация случайной пары векторов
def vec_generate_random_pair():
    return vec_generate_random(), vec_generate_random()


def vec_generate_bysize(size):
    if size<=0:
        return None
    vector = UniversalVector(size)
    for i in range(size):
        vector.set_dimval(i, randint(-100, 100))
    return vector

def vec_generate_samesizepair(size):
    return vec_generate_bysize(size), vec_generate_bysize(size)

# Вывод в консоль отчета для операции с одним вектором
def write_monovec_log(test_id, vector_test, operation_name, result, mode=WRITE_LOG_TO_CONSOLE, testseries_name="testseries_name_", consolename=''):
    if mode == WRITE_LOG_TO_CONSOLE:
        print(f"Test № {test_id} . Working with vector: {vector_test} . Operation Name: {operation_name} . Result: {result}\n")
    else:
        filename = str(testseries_name)+operation_name+'.txt'
        with open(filename) as file:
            file.write(f"Test № {test_id} . Working with vector: {vector_test} . Operation Name: {operation_name} . Result: {result} .   Console Output: {consolename}\n")

# Вывод в консоль отчета для операции с двумя векторами
def write_polyvec_log(test_id, vector_test1, vector_test2 ,operation_name, result, mode=WRITE_LOG_TO_CONSOLE, testseries_name="testseries_name_", consolename=''):
    if mode==WRITE_LOG_TO_CONSOLE:
        print(f"Test № {test_id} . Working with vectors: ( {vector_test1} and {vector_test2}. Operation Name: {operation_name} . Result: {result} \n")
    else:
        filename = str(testseries_name)+operation_name+'.txt'
        with open(filename) as file:
            file.write(f"Test № {test_id} . Working with vectors: ( {vector_test1} and {vector_test2}. Operation Name: {operation_name} . Result: {result} \n")

def get_curr_console_output():
    return sys.stdout.getvalue()



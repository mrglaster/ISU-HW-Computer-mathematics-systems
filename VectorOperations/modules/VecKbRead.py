"""

Функции для считывания векторов с клавиатуры

"""
from .UniversalVectorClass import UniversalVector

"""
Функция parse_2vec()

На входe: аргументы отсутствуют
На выходе: 2 объекта класса UniversalVector

Что делает?
Считывает масив данных с командной строки в формате: n значений вектора v1 и n для v2
Если кол-во чисел на входе нечётное - ошибка.
"""
def parse_2vec():
    input_string = input()
    arr_values = input_string.split()
    if len(arr_values)%2!=0 or len(arr_values) <=2:
        print("Wrong argument amount!")
        return None, None
    arr_values = [int(numeric_string) for numeric_string in arr_values]
    int_vecdims = int(len(arr_values)/2)
    vec_1 = UniversalVector(int_vecdims)
    vec_2 = UniversalVector(int_vecdims)
    print(f"Detected 2 Vectors with dimension amount: {int_vecdims}")
    for i in range(int_vecdims):
        vec_1.set_dimval(i, arr_values[i])
    cntr = 0
    for i in range(int_vecdims, len(arr_values)):
        vec_2.set_dimval(cntr, arr_values[i])
        cntr+=1
    return vec_1, vec_2


"""
Функция parse_1vec

Что делает: то же самое, что и parse_2vec, только для одного вектора

"""
def parse_1vec():
    input_string = input()
    arr_values = [int(numeric_string) for numeric_string in input_string.split()]
    int_vecdims = len(arr_values)
    vec_1 = UniversalVector(int_dimensions=int_vecdims)
    print(f"Detected dimensions: {int_vecdims}")
    for i in range(int_vecdims):
        vec_1.set_dimval(i, arr_values[i])
    return vec_1


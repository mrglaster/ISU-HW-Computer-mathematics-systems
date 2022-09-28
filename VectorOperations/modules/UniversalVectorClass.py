"""
Класс UniversalVecotor и проверка размерностей векторов.
"""

class UniversalVector:
    def __init__(self, int_dimensions):
        self.int_dimensions = int_dimensions
        self.values = {}
    #Задать значение измерению вектора (x,y,z...)
    def set_dimval(self, dimension, value):
        dimension+=1    
        if dimension>0 and dimension<=self.int_dimensions:
            self.values[dimension] = int(value)
        else:
            print("WD: ", dimension)
            print("Wrong dimension data!")
    #Добавить измерение вектору
    def expand_dimensions(self, new_dimension):
        if new_dimension not in self.values.keys():
            self.values[new_dimension] = 0
    #Получить значение измерения вектора
    def get_dimval(self, dimension):
        dimension+=1
        if dimension in self.values.keys():
            return self.values[dimension]
        print(self.values)
        print("Wrong dimension: ", dimension)
        return None
    #Получить количество измерений
    def get_dimensions(self):
        return int(self.int_dimensions)
    #Перегрузка оператора str
    def __str__(self):
        string_result = "( "
        for i in self.values.values():
            string_result+=str(i) + " ; "
        return string_result[: len(string_result)-2]+")"




#А был ли мальчик (зачёркнуто) вектор
def vector_exists(vec1):
    if vec1.get_dimensions()<=0:
        print("Created vector doesn't exist!")
        return False
    return True


"""
Что делает?

Проверяет возможность проведения операции с векторами vec1 и vec2:
если размерность векторов совпадает - вадает True
"""
def dimensions_check(vec_1, vec_2):
    if vec_1.get_dimensions() != vec_2.get_dimensions():
        print("Dimensions error! Vectors must have same dimensions amount to work with each other")
        return False
    if not vector_exists(vec_1) or not vector_exists(vec_2):
        print("One of vectors doesn't exist!")
        return False
    return True


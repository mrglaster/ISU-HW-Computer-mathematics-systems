"""
Класс UniversalVecotor и проверка размерностей векторов.
"""


class UniversalVector:
    def __init__(self, int_dimensions):
        self.int_dimensions = int_dimensions
        self.values = {}

    def set_dimval(self, dimension, value):
        """Задать значение измерению вектора (x,y,z...)"""
        dimension += 1
        if 0 < dimension <= self.int_dimensions:
            self.values[dimension] = int(value)
        else:
            raise ValueError(f"Unable to set dimension: {dimension}")

    def expand_dimensions(self, new_dimension):
        """Добавить измерение вектору"""
        if new_dimension not in self.values.keys():
            self.values[new_dimension] = 0

    def get_dimval(self, dimension):
        """Получить значение измерения вектора"""
        dimension += 1
        if dimension in self.values.keys():
            return self.values[dimension]
        raise ValueError(f"Unable to find vector's dimension: {dimension}")

    def get_dimensions(self):
        """ Получить количество измерений"""
        return int(self.int_dimensions)

    def __str__(self):
        """Перегрузка оператора str"""
        string_result = "( "
        for i in self.values.values():
            string_result += str(i) + " ; "
        return string_result[: len(string_result) - 2] + ")"

    def __len__(self):
        return self.get_dimensions()

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.get_dimval(i) != other.get_dimval(i):
                return False
        return True


def vector_exists(vec1):
    """ А был ли  вектор"""
    return len(vec1) >= 1


def dimensions_check(vec_1, vec_2):
    """
    Проверяет возможность проведения операции с векторами vec1 и vec2:
    если размерность векторов совпадает - вадает True
    """
    if vec_1.get_dimensions() != vec_2.get_dimensions():
        return False
    if not vector_exists(vec_1) or not vector_exists(vec_2):
        raise ValueError("One of vectors doesn't exist!")
    return True

"""
UniversalVector class and some methods
"""


class UniversalVector:
    def __init__(self, int_dimensions):
        self.int_dimensions = int_dimensions
        self.values = {}

    def set_dimval(self, dimension, value):
        """Set value to vector's dimension"""
        dimension += 1
        if 0 < dimension <= self.int_dimensions:
            self.values[dimension] = float(value)
        else:
            raise ValueError(f"Unable to set dimension: {dimension}")

    def expand_dimensions(self, new_dimension):
        """Add dimension to vector"""
        if new_dimension not in self.values.keys():
            self.values[new_dimension] = 0

    def get_dimval(self, dimension):
        """Get vector's dimension value"""
        dimension += 1
        if dimension in self.values.keys():
            return self.values[dimension]
        raise ValueError(f"Unable to find vector's dimension: {dimension}")

    def get_dimensions(self):
        """Get Vector's dimensions amount"""
        return int(self.int_dimensions)

    def __str__(self):
        """str operator overload"""
        string_result = "( "
        for i in self.values.values():
            string_result += str(i) + " ; "
        return string_result[: len(string_result) - 2] + ")"

    def __len__(self):
        """len operator overload"""
        return self.get_dimensions()

    def __getitem__(self, item):
        return self.get_dimval(item)

    def __setitem__(self, key, value):
        return self.set_dimval(key, value)

    def __eq__(self, other):
        """== operator overload"""
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.get_dimval(i) != other.get_dimval(i):
                return False
        return True




def vector_exists(vec1):
    """ Does the vector exist?"""
    return len(vec1) >= 1



def dimensions_check(vec_1, vec_2):
    """
    Checks the possibility of performing an operation with the vectors vec1 and vec2:
    if the dimensions of the vectors are the same, returns True
    """
    if vec_1.get_dimensions() != vec_2.get_dimensions():
        return False
    if not vector_exists(vec_1) or not vector_exists(vec_2):
        raise ValueError("One of vectors doesn't exist!")
    return True

from modules.matrix_operations.matrix_operations import *


def lagrange_polynomial(data_xy, interpolate_Value):
    length_range = len(data_xy)
    result = 0.0
    for i in range(length_range):
        temp = data_xy[i][1]
        for j in range(length_range):
            if j!=i:
                temp *= (interpolate_Value - data_xy[j][0]) / (data_xy[i][0] - data_xy[j][0])

        result += temp
    return result


from modules.matrix_operations.matrix_io import read_rectmatrix_kb
from modules.linear_equations_system.les_parameters import is_valid_les

UPPER_LINE = '¯'
STRAIGHT_LINE = '| '
SUBNUMS = ['₀','₁','₂','₃','₄','₅','₆','₇','₈','₉']


SUBSTRING = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

def to_subnum(num):
    """Converts number to substring number (123 -> ₁₂₃) """
    if not num.isnumeric():
        raise ValueError(f"Unable to convert string {num} to substring: excepted a number!")
    result = ""
    for i in str(num):
        result+=SUBNUMS[int(i)]
    return result


def read_les_kb(variables_amount):
    """Reads arguments for linear equations system from keyboard. Returns expanded matrix A|b """
    return read_rectmatrix_kb(rows=variables_amount, columns=variables_amount+1)

def print_les(les):
    """Prints linear equals system"""
    """
    Output example: 
    
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    | 1X₁ + 2X₂ + 3X₃  = 4
    | 5X₁ + 6X₂ + 7X₃  = 8
    | 1X₁ + 2X₂ + 5X₃  = 6
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    """
    is_valid_les(les)
    print('\n')
    print(UPPER_LINE*30)
    for row in les:
        current_row = STRAIGHT_LINE
        for i in range(len(row)-1):
            if row.get_dimval(i) != 0:
                current_row+=str(row.get_dimval(i))+"X"+to_subnum(str(i+1))+" + "
        current_row = (current_row[:len(current_row)-2] + "= "+str(row.get_dimval(len(row)-1))).replace("+ -", "- ")
        print(current_row)
    print(UPPER_LINE*30)





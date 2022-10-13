from modules import MatrixGenerators
from modules import MatrixIO
from modules import MatrixOperations
from modules import MatrixParameters

def main():
    a = MatrixOperations.classic_to_vector([[5, 4, 3], [21, -2, 6], [5, 4, 0]])
    a = MatrixOperations.get_determinant(matrix=a)
    print(a)




if __name__=='__main__':
    main()
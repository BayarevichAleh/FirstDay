from random import randrange

def create_matrix(n, m):
    """
    Create new matrix
    :param n: columns
    :param m: rows
    :type n,m: int
    :return: created matrix
    """
    new_matrix = list()
    for i in range(m):
        row = list()
        for j in range(n):
            row.append(randrange(-100, 100))
        new_matrix.append(row)
    return new_matrix


def sum_matrix(matrix_1, matrix_2):
    """
    Sum matrix #1 and matrix #2
    :param matrix_1: matrix #1
    :param matrix_2: matrix #2
    :return: sum matrix #1 and matrix #2
    """
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            matrix_1[i][j] += matrix_2[i][j]
    return matrix_1


column = int(input("Enter number of columns:"))
row = int(input("Enter number of rows:"))
a = create_matrix(column, row)
b = create_matrix(column, row)
print(f'You create matrix #1:\n{a}')
print(f'You create matrix #2:\n{b}')
print(f'Sum matrix #1 and matrix #2:\n{sum_matrix(a, b)}')

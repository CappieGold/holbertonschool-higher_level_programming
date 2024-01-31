#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        square = list(map(lambda x: x ** 2, i))
        square_matrix.append(square)
    return square_matrix

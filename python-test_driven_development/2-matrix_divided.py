#!/usr/bin/python3
"""
divide matrix by arg
author: Carpentier
date: 07/02/2024
"""
def matrix_divided(matrix, div):
    """
    raise error and create new matrix for divide matrix
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    row_length = None
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

   # return [[round(elem / div, 2) for elem in row] for row in matrix]
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix

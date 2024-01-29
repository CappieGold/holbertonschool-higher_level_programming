#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        j = ' '.join(map(str, i))
        print("{}".format(j))

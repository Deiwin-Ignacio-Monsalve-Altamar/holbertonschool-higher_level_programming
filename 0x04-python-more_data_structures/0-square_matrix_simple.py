#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        new_matrix.append(list(map(lambda x: x * x, x)))
    return new_matrix

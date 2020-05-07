#!/usr/bin/python3
def square_num(nu):
    nu * nu


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(square_num, i)))

    return new_matrix

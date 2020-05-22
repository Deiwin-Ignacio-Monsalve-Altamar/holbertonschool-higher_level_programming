#!/usr/bin/python3


"2-matrix_divided.py print number divididos / 2"


def matrix_divided(matrix, div):
    """
    Arguments
    matriz: data in the array
    div: number a dividor
    """
    for row in matrix:
        for number in row:
            if type(number) is not int and type(number) is not float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(set([len(row) for row in matrix])) is not 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[float("{:.2f}".format(num/div)) for num in row] for row in matrix]

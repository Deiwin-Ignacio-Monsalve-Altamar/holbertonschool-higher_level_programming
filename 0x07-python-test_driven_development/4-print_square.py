#!/usr/bin/python3


"4-print_square.py print number divididos"


def print_square(size):
    """
    Arguments
    size: longitud integer
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)

#!/usr/bin/python3


"2-square.py class square defines a square"


class Square:
    """Class square"""
    def __init__(self, size=0):
        """Inizialition of variables
        Arg self identificador
            size tamañe of square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

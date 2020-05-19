#!/usr/bin/python3


"5-square.py class square defines a square"


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

    @property
    def size(self):
        """ Returns size"""
        return self.__size

    @size.setter
    """Set in the self.__size with value"""
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Returns area the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print square # """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

#!/usr/bin/python3


"6-square.py class square defines a square"


class Square:
    """Class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Inizialition of variables
        Arg self identificador
            size tamañe of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """ Returns size
        """
        return self.__size

    @property
    def position(self):
        """ Returns position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set in the self.__position with value
        """
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Returns area the square
        """
        return self.__size * self.__size

    def my_print(self):
        """Print square #
        """
        if self.__size == 0:
            print()
        for i in range(self.position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

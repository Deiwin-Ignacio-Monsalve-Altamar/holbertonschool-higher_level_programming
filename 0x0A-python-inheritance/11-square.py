#!/usr/bin/python3


"""BaseGeometry Class module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Arguments:
        Rectangle {[type]} -- [description]
    """

    def __init__(self, size):
        """Inizialition square Class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

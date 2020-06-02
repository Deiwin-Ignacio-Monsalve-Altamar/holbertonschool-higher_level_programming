#!/usr/bin/python3


"""BaseGeometry Class module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry
    Args:
        BaseGeometry (class) : class to inherit from
    """

    def __init__(self, width, height):
        """Initailizing Rectangle in BaseGeometry"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

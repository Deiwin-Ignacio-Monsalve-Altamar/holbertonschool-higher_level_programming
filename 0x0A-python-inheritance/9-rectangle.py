#!/usr/bin/python3


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Arguments:
        BaseGeometry {[type]} -- [description]
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height

    def area(self):
        """return area"""
        return self.__width * self.__heigth

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__heigth)

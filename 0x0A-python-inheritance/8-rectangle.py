#!/usr/bin/python3


"BaseGeometry class module"


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Arguments:
        BaseGeometry {[type]} -- [description]
    """

    def __init__(self, width, height):
        """
        Arguments:
            width {[type]} -- [description]
            height {[type]} -- [description]
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height

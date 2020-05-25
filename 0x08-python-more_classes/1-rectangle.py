#!/usr/bin/python3


"1-rectangle,py print recntangule"


class Rectangle:
    """Class Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Arguments:
        width {int]: integer
        height {int}: integer
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """return property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """return property
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return property
        """
        return self.__heigth

    @height.setter
    def height(self, value):
        """return property
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = value

#!/usr/bin/python3
"""Class rectangle crate class eitn inherefemcia"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width (integer): [width in rectangle]
            height (integer): [heigth in the rectangle]
            x (int, optional): [integer asignement]
            y (int, optional): [integer asignement]
            id ([type], optional): [hereda de la clase padre].
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns: self: width in rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value (integer): [integer asignement for width]
        """
        self.__width = value

    @property
    def height(self):
        """
        Returns:
            [int]: [integer asignement for width]
        """
        return self.__heigth

    @height.setter
    def height(self, value):
        """
        Args:
            value (int): [integer asignement for height]
        """
        self.__heigth = value

    @property
    def x(self):
        """
        Returns:
            [int]: [integer asignement for x]
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Args:
            value (int): [integer asignement for x]
        """
        self.__x = value

    @property
    def y(self):
        """
        Returns:
            [int]: [integer asignement for y]
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Args:
            value (y): [integer asignement for y]
        """
        self.__y = value

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """args: argument in tuple
        """
        count = 1
        if len(args):
            for value in args:
                if count == 1:
                    self.id = value
                elif count == 2:
                    self.__width = value
                elif count == 3:
                    self.__height = value
                elif count == 4:
                    self.__x = value
                elif count == 5:
                    self.__y = value
                count += 1
        elif len(kwargs):
            for item, value in kwargs.items():
                if item == 'id':
                    self.id = value
                elif item == 'width':
                    self.__width = value
                elif item == 'height':
                    self.__height = value
                elif item == 'x':
                    self.__x = value
                elif item == 'y':
                    self.__y = value

    def area(self):
        """
        Returns:
        area: return value of the area
        """
        return self.__height * self.__width

    def display(self):
        """ function self print #
        """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def __str__(self):
        """
        Returns:
                        [type]: [description]
        """
        return '[Rectangle] ({}) {}/{} - '\
            '{}/{}'.format(self.id, self.__x, self.__y,
                           self.__width, self.__height)

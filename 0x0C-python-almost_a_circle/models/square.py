#!/usr/bin/python3
"""Class Rectangle crate class eitn inherefemcia"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns:
            [type]: [description]
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Args:
            value ([type]): [description]
        """
        self.width = value
        self.height = value

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.width)

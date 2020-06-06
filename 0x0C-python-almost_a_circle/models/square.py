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

    def update(self, *args, **kwargs):
        """Updates the square instance
        Args:
            args (list): argument lists
            kwargs (dict): argument dictionary
        """
        if len(args):
            count = 1
            for value in args:
                if count == 1:
                    self.id = value
                if count == 2:
                    self.size = value
                if count == 3:
                    self.x = value
                if count == 4:
                    self.y = value
                count += 1
        elif len(kwargs):
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']


    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.width)

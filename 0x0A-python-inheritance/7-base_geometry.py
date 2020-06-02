#!/usr/bin/python3


"class BaseGeometry (based on 6-base_geometry.py)."


class BaseGeometry():
    """class BaseGeometry
    """
    def area(self):
        """Method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Arguments:
            name {[type]} -- [description]
            value {[type]} -- [description]
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3


"""Rebel Class module"""


class MyInt(int):
    """
    Arguments:
            int {[type]} -- [description]
    """

    def __init__(self, value):
        """
        Arguments:
                value {[type]} -- [description]
        """
        self.__value = value

    def __eq__(self, other):
        """
        Arguments:
                other {[type]} -- [description]
        """
        return self.__value != other

    def __ne__(self, other):
        """
        Arguments:
                other {[type]} -- [description]
        """
        return self.__value == other

    def __str__(self):
        """Print out the string format"""
        return "{}".format(self.__value)

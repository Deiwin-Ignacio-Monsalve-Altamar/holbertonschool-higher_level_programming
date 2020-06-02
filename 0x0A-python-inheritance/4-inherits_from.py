#!/usr/bin/python3


"function that returns True if the object is an instance"


def inherits_from(obj, a_class):
    """Return True or False that inherited"""
    if issubclass(type(obj), a_class) is True:
        return True
    return False

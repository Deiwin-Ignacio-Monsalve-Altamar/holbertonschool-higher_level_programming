#!/usr/bin/python3

" function that returns True if the object is an instance of"


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance or False"""
    if isinstance(obj, a_class) is True:
        return True
    return False

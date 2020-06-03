#!/usr/bin/python3


"Added an tribute on class"


def add(obj, name, value):
    """
    Arguments:
        obj {[type]} -- [description]
        name {[type]} -- [description]
        value {[type]} -- [description]
    """
    if not hassattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)

#!/usr/bin/python3


"function that returns True if the object is an instance"


def inherits_from(obj, a_class):
    """Return True or False that inherited"""
    return issubclass(type(obj), a_class)

#!/usr/bin/python3


"3-say_my_name.py print number divididos"


def say_my_name(first_name, last_name=""):
    """
    Arguments
    first_name: in the array
    last_name: apellido
    """
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

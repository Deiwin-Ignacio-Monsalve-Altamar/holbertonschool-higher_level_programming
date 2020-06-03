#!/usr/bin/python3


"Fuction return object dict"


def class_to_json(obj):
    """
    Args:
        obj ([type]): [description]
    Returns:
        obj : dictionary
    """
    return obj.__dict__

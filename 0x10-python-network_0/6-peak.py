#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers ([type]): [description]
    """
    if len(list_of_integers) == 0:
        return

    list_of_integers.sort()
    return list_of_integers[-1]

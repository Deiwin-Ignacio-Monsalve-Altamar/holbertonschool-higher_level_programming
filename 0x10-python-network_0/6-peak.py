#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers ([type]): [description]
    """
    if len(list_of_integers) == 0:
        return

    length = len(list_of_integers)
    left, rigth = 0, length - 1

    return (find_peak_recursion(left, rigth, list_of_integers))


def find_peak_recursion(left, rigth, list_of_integers):
    """Recursion find peak"""
    if left == rigth:
        return list_of_integers[rigth]

    mid = (left + rigth) // 2

    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return find_peak_recursion(left, mid, list_of_integers)
    return find_peak_recursion(mid + 1, rigth, list_of_integers)

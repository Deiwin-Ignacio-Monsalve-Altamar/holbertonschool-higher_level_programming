#!/usr/bin/python3


"Fuction read line in file"


def read_file(filename=""):
    """
    Keyword Arguments:
        filename {str} -- [description] (default: {""})
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

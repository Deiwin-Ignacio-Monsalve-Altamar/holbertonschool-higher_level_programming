#!/usr/bin/python3


"Fuction read lines in file of nb_lines"


def read_lines(filename="", nb_lines=0):
    """
    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        nb_lines {int} -- [description] (default: {0})
    """
    with open(filename, encoding='utf-8') as f:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(f.readline(), end="")
        else:
            print(f.read(), end="")

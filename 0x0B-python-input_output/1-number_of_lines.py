#!/usr/bin/python3


"Fuction counter lines in file"


def number_of_lines(filename=""):
    """
    Keyword Arguments:
        filename {str} -- [description] (default: {""})

    Returns:
        int -- counters
    """
    with open(filename, encoding='utf-8') as f:
        for i, letras in enumerate(f):
            if i == 0:
                return 0
        return i + 1

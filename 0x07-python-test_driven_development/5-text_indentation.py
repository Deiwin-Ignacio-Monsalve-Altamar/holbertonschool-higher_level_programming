#!/usr/bin/python3


"5-text_indentation.py print number divididos"


def text_indentation(text):
    """
    Arguments:
    text: letter in text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    start = 0
    for i, c in enumerate(text):
        if i == len(text) - 1:
            print(text[start:i + 1].strip(), end="")
        elif c in ".?:":
            print(text[start:i + 1].strip(), end="\n\n")
            start = i + 1

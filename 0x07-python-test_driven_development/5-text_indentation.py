#!/usr/bin/python3


"5-text_indentation.py print number divididos"


def text_indentation(text):
    """
    Arguments:
    text: letter in text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    tmp = 0
    for i, c in enumerate(text):
        if c in ".?:":
            print(text[tmp:i + 1].strip(), end="\n\n")
            tmp = i + 1
        elif i == len(text) - 1:
            print(text[tmp:i + 1].strip(), end="")

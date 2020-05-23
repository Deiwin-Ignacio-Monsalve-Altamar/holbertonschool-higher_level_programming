#!/usr/bin/python3


"5-text_indentation.py print number divididos"


def text_indentation(text):
    """
    Arguments:
    text: letter in text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    position = ":"
    for char in text:
        if char is " " and position in ".?:":
            continue
        print(char, end="")
        if char in "?.:":
            print()
            print()
        position = char

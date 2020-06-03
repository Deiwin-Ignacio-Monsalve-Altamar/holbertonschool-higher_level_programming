#!/usr/bin/python3

"Function append_write"


def append_write(filename="", text=""):
    """
    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [lineas] -- [add apennd]
    """
    with open(filename, mode='a+', encoding="UTF-8") as f:
        lineas = f.write(text)
        return lineas

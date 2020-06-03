#!/usr/bin/python3

"Fuction write lines in file"


def write_file(filename="", text=""):
    """
    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [lines_write] -- [description]
    """
    with open(filename, mode='w', encoding="UTF-8") as f:
        lines_write = f.write("{}".format(text))
        return lines_write

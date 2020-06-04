#!/usr/bin/python3

"""function that writes an Object to a text file, using a JSON representation
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args
        filename:
        search_string:
        new_string:
    """
    aux = ""
    with open(filename, mode='r', encoding="UTF8") as file:
        for k in file:
            if search_string in k:
                aux += k[:] + new_string
            else:
                aux += k[:]
    with open(filename, mode='w', encoding="UTF8") as file:
        file.write(aux)

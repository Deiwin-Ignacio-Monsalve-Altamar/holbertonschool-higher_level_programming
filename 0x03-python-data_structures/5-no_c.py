#!/usr/bin/python3
def no_c(my_string):
    new_letter = ""
    for letter in my_string:
        if letter != 'c' or letter != 'C':
            new_letter += letter
    return new_letter

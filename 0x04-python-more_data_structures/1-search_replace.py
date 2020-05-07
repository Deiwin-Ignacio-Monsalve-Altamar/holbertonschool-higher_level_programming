#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, item in enumerate(my_list):
        if item == search:
            new_list[i] = replace
    return new_list

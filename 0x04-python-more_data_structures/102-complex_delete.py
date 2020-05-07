#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_dic = sorted(a_dictionary.items())
    for num, delete in delete_dic:
        if delete == value:
            del a_dictionary[num]
    return a_dictionary

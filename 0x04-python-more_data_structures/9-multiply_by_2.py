#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = dict(a_dictionary)
    mul = 0
    for i, value in a_dictionary.items():
        new_dic[i] = value * 2
    return new_dic

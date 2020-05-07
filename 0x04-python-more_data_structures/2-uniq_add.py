#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = set(my_list)
    result = 0
    for i in sum:
        result += i
    return result

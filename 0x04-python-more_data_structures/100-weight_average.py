#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    
    sum, div = 0, 0
    for num in my_list:
        sum += num[0] * num[1]
        div += num[1]
    return sum / div

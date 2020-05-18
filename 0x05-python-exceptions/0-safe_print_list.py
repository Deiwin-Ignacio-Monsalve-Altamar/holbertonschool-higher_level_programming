#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for index, num in enumerate(my_list):
        try:
            if x > index:
                print(num, end ="")
                counter += 1
        except IndexError:
            return counter
    print()
    return counter


#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for index, num in enumerate(my_list):
        try:
            if x > index:
                print("{:d}".format(num), end="")
                counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return counter

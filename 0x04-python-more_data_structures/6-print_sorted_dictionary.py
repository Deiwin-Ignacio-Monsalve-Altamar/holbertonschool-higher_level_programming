#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sorted_search = sorted(a_dictionary.keys())
        for i in sorted_search:
            print("{:s}: {}".format(i, a_dictionary[i]))

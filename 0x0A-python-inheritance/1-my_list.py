#!/usr/bin/python3


"0-my_list.py inherited object"


class MyList(list):
    """
    Arguments:
        list {[type]} -- [description]
    """
    def print_sorted(self):
        print(sorted(self))

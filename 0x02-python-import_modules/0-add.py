#!/usr/bin/python3
from add_0 import add


def add_numbers():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == '__main__':
    add_numbers()

#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.request
import sys


def responseHeader(arg):
    """
    Args:
        arg (argument): [url sends]
    """
    with urllib.request.urlopen(arg) as response:
        dictResponse = response.info()
        print("{}".format(dictResponse['X-Request-Id']))


if __name__ == '__main__':
    responseHeader(sys.argv[1])

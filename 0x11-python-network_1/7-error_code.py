#!/usr/bin/python3
"""sends a request to the URL"""
import requests
import sys


def errorCode(url):
    """sends a request to the URL"""
    r = requests.get(url)
    if (r.status_code == 200):
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))


if __name__ == '__main__':
    errorCode(sys.argv[1])

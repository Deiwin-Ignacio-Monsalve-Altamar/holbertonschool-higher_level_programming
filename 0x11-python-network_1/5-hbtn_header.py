#!/usr/bin/python3
"""sends a request to the URL and displays"""
import requests
import sys


def responseValue(url):
    """sends a request to the URL"""
    r = requests.get(url)
    print("{}".format(r.headers.get('X-Request-Id')))


if __name__ == '__main__':
    responseValue(sys.argv[1])

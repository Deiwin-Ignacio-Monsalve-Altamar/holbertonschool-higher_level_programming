#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST"""
import requests
import sys


def postEmail(url, email):
    """takes in a URL and an email address, sends a POST"""
    data = {'email': email}
    r = requests.post(url, data=data)
    print("{}".format(r.text))


if __name__ == '__main__':
    postEmail(sys.argv[1], sys.argv[2])

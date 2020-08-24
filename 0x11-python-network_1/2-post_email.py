#!/usr/bin/python3
"""that takes in a URL and an email"""
import urllib.parse
import urllib.request
from sys import argv


def postEmail(args, email):
    """
    Args:
        args (): [request url]
        email (): [post value]
    """
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(args, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("{}".format(html.decode('utf-8')))


if __name__ == '__main__':
    postEmail(argv[1], argv[2])

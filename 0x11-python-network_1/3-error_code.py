#!/usr/bin/python3
"""sends a request to the URL"""
import urllib.request
import sys


def desplayError(url):
    """
    Args:
        url ([type]): [description]
    """
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print("{}".format(html.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    desplayError(sys.argv[1])

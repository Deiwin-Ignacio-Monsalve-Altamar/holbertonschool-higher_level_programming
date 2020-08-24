#!/usr/bin/python3
""" """
import urllib.request


def callSecuence():
    """script that fetches"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == '__main__':
    callSecuence()

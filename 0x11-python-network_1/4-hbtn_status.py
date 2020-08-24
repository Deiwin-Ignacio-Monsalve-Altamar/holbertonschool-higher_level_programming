#!/usr/bin/python3
"""Python script that fetches"""
import requests


def statusPython():
    """Python script that fetches"""
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == '__main__':
    statusPython()

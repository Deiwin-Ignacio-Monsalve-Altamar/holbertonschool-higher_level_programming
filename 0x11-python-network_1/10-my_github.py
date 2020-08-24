#!/usr/bin/python3
"""takes your Github credential"""
import requests
import sys


def my_github(url, users, password):
    """takes your Github credential"""
    
    r = requests.get(url, auth=(users, password))
    dict_json = r.json()
    print(dict_json.get('id'))


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    users = sys.argv[1]
    password = sys.argv[2]
    my_github(url, users, password)

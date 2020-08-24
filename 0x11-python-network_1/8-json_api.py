#!/usr/bin/python3
"""script that takes in a letter"""
import requests
import sys


def search_api(url, q):
    """script that takes in a letter"""
    data = {'q': q}
    r = requests.post(url, data=data)

    try:
        n_dict = r.json()
        if n_dict:
            print("[{}] {}".format(n_dict['id'], n_dict['name']))
        else:
            print("No result")
    except Exception:
        print("Not valide JSON")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    search_api(url, q)

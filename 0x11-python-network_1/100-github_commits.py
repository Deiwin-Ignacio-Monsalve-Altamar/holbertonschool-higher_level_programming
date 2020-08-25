#!/usr/bin/python3
"""evaluates candidates applying for a back-end position"""
import requests
import sys


def time_for_interviem(owner, repo):
    """script that takes 2 arguments in order"""
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)

    dict_n = r.json()
    count = 0
    for x in dict_n:
        print("{}: {}".format(x.get('sha'), x.get(
            'commit').get('author').get('name')))
        count += 1
        if count == 10:
            break


if __name__ == '__main__':
    owner = sys.argv[2]
    repo = sys.argv[1]
    time_for_interviem(owner, repo)

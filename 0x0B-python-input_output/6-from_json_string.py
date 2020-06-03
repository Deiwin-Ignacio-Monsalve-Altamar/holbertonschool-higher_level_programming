#!/usr/bin/python3


"""Module function"""


import json


def from_json_string(my_str):
    """
    Arguments:
        my_str {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    return json.loads(my_str)

#!/usr/bin/python3
import json


"Fuction convert string in Json"


def from_json_string(my_str):
    """
    Arguments:
        my_str {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    return json.loads(my_str)

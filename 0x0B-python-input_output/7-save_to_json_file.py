#!/usr/bin/python3


"""Fuction save to json file"""


import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(my_obj, f)

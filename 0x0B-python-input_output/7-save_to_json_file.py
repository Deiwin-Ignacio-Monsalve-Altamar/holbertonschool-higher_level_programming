#!/usr/bin/python3
import json


"Fuction save to json file"


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3


"""Module containg funtion convert to json"""


import json



def to_json_string(my_obj):
    """
    Arguments:
        my_obj {[type]} -- [description]

    Returns:
        [json.dupms] -- [convert string]
    """
    return json.dumps(my_obj)

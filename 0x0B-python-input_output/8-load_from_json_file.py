#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    Args:
        filename ([type]): [description]

    Returns:
        [type]: [description]
    """
    with open(filename, encoding="UTF-8") as f:
        return json.load(f)

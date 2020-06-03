#!/usr/bin/python3


"""Add item module
"""


import json
import sys

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    new_list = load_from_json_file(filename) + sys.argv[1:]
except Exception:
    new_list = sys.argv[1:]

save_to_json_file(new_list, filename)

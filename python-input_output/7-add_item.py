#!/usr/bin/python3
"""module to add item to a list"""

import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """function to add item to a list"""
    filename = "add_item.json"
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
        my_list.extend(sys.argv[1:])
    else:
        my_list = sys.argv[1:]

    save_to_json_file(my_list, filename)

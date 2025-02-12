#!/usr/bin/python3
"""module to convert from json string"""

def from_json_string(my_str):
    import json
    return json.loads(my_str)

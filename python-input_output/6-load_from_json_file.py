#!/usr/bin/python3
"""module to load from json file"""

def load_from_json_file(filename):
    import json
    with open(filename, 'r') as f:
        return json.loads(f.read())

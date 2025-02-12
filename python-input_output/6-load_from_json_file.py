#!/usr/bin/python3

def load_from_json_file(filename):
    import json
    with open(filename, 'r') as f:
        return json.loads(f.read())

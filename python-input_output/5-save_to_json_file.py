#!/usr/bin/python3
"""module to save to json file"""

def save_to_json_file(my_obj, filename):
    """function to save to json file"""
    import json
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))

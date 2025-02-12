#!/usr/bin/python3
"""module to write a file"""


def write_file(filename="", text=""):
    """function to write a file"""
    with open(filename, 'w') as f:
        return f.write(text)

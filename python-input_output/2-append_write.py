#!/usr/bin/python3
"""module to append a file"""

def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        return f.write(text)

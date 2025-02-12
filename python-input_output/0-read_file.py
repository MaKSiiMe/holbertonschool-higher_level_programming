#!/usr/bin/python3
"""Module for read_file"""

def read_file(filename=""):
    """Function to read a file"""
    with open(filename, 'r') as f:
        print(f.read(), end="")

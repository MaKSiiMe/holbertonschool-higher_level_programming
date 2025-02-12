#!/usr/bin/python3
"""module to convert to json string"""

def class_to_json(obj):
    """function to convert to json string"""
    return obj.__dict__

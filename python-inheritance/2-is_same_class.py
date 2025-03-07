#!/usr/bin/python3

""" Module that defines a function that returns the
    list of available attributes and methods of an object"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class;
    otherwise False
    """
    return type(obj) is a_class

#!/usr/bin/python3

""" Module that defines a function that returns the
    list of available attributes and methods of an object"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ;
    otherwise False
    """
    return type(obj) is a_class or issubclass(type(obj), a_class)

#!/usr/bin/python3

""" Module that defines a function that returns the
    list of available attributes and methods of an object"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ;
    otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

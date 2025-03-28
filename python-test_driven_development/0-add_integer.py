#!/usr/bin/python3

"""
Module that adds two integers
2
3
"""


def add_integer(a, b=98):

    """
    Function that adds two integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

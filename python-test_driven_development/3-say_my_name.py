#!/usr/bin/python3
"""
This module contains a function that prints a name.
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints a name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name.isdigit():
        raise TypeError("first_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

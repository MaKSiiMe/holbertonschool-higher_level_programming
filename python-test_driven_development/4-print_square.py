#!/usr/bin/python3
"""
Module for print_square
"""


def print_square(size):
    """
    Print a square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

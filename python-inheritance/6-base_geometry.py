#!/usr/bin/python3

""" Module that defines a function that returns the
    list of available attributes and methods of an object"""


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        raise Exception("area() is not implemented")

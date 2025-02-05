#!/usr/bin/python3

""" Module that defines a function that returns the
    list of available attributes and methods of an object"""


class MyList(list):
    """ Class MyList that inherits from list """
    def print_sorted(self):
        """ Prints the list, but sorted """
        print(sorted(self))

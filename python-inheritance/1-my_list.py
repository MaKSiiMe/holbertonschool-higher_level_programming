#!/usr/bin/python3

class MyList(list):
    """ Class MyList that inherits from list """
    def print_sorted(self):
        """ Prints the list, but sorted """
        print(sorted(self))

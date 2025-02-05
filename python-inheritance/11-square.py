#!/usr/bin/python3

""" Module that defines a function that returns the
    list of available attributes and methods of an object"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Instantiation with size """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ Return a string """
        return "[Square] {}/{}".format(self.__size, self.__size)

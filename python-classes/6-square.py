#!/usr/bin/python3
"""
Module that defines a class Square
"""


class Square:
    """
    Class that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(num, int)
                    and num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

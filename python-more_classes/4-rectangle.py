#!/usr/bin/python3
"""
Module that defines a class Rectangle
"""


class Rectangle:
    """
    Class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Constructor for the Rectangle class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle
        """
        self.__height = value

    def area(self):
        """
        Method that returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method that returns the perimeter of the rectangle
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Method that returns the string representation of the rectangle
        """
        return "\n".join(["#" * self.width for i in range(self.height)])

    def __repr__(self):
        """
        Method that returns the string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

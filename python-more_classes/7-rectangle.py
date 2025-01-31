#!/usr/bin/python3
"""
Module that defines a class Rectangle
"""


class Rectangle:
    """
    Class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor for the Rectangle class
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol)
                          * self.width for i in range(self.height)])

    def __repr__(self):
        """
        Method that returns the string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Destructor of the rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

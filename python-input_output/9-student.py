#!/usr/bin/python3
"""module to create a class Student"""

class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """module to convert to json string"""
    def to_json(self):
        return self.__dict__

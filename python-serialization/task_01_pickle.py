#!/usr/bin/python3

"""This module is for creating custom objects and serializing them"""

import pickle


class CustomObject:
    """class for creating custom objects"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        for key, value in self.__dict__.items():
            print("{}: {}".format(key, value))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            return None

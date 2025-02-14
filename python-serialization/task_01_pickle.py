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
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

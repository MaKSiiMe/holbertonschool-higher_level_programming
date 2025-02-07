#!/usr/bin/python3


class CountedIterator:
    def __init__(self, data):
        self.iterator = iter(data)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

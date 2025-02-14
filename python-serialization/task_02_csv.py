#!/usr/bin/python3

"""This module is for converting csv file to json file"""

import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, "r") as csv_file:
            csv_file = csv.DictReader(csv_file)
            data = list(csv_file)
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
        return True
    except FileNotFoundError:
        return False

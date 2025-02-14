#!/usr/bin/python3

"""This module is for converting csv file to json file"""

import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
        with open(data.json, 'w') as json_file:
            json.dump(data, json_file)
    except Exception as e:
        return e
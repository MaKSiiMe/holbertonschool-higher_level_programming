#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(disctionary, filename):
    root = ET.Element('data')
    for key, value in disctionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary

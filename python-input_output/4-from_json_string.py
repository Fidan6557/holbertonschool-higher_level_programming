#!/usr/bin/python3
"""a function that returns an object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """ A function that converts JSON formats to object"""
    return json.loads(my_str)

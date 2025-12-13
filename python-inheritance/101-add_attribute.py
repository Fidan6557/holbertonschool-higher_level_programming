#!/usr/bin/python3
"""Function to add new attribute to an object"""


def add_attribute(obj, name, value):
    """Adds a new attribute to obj if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

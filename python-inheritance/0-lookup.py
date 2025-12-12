#!/usr/bin/python3
"""The list of available attributes and methods of an object"""


def lookup(obj):
    """ a function that returns the list of available attributes and methods"""
    return list(dir(obj))

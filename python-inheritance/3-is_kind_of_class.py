#!/usr/bin/python3
"""""Documentation for inheritance"""


def is_kind_of_class(obj, a_class):
    """Checking the kind of class"""
    return type(obj) is a_class or isinstance(obj, a_class)

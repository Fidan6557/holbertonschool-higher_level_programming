#!/usr/bin/python3
"""""Return True if obj is an instance of a_class or its subclass, else False."""


def is_kind_of_class(obj, a_class):
    """Checking if obj is an instance of a_class or its subclass, else return False."""
    return type(obj) is a_class or isinstance(obj, a_class)

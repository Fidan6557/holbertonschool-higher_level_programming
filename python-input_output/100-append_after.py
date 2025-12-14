#!/usr/bin/python3
"""a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """ A function that inserts a line of text to a file"""
    with open(filename, "w") as f:
        f.write(new_string)

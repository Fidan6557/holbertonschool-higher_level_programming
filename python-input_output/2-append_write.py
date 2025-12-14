#!/usr/bin/python3
""" Appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file (UTF8) """
    with open(filename, "a") as f:
        return f.write(text)

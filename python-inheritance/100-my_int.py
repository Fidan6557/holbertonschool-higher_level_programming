#!/usr/bin/python3
"""MyInt class that inverts == and != operators"""


class MyInt(int):
    """ Rebel int class"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)

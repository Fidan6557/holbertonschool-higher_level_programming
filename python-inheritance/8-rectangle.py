#!/usr/bin/python3
#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """a class BaseGeometry"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("%s must be an integer" % name)
        if value <= 0:
            raise ValueError("%s must be greater than 0" % name)

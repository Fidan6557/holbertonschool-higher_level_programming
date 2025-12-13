#!/usr/bin/python3
""" Rectangle class """
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry()


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"[Rectangle] {self.__width} / {self.__height}"

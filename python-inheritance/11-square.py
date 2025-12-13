#!/usr/bin/python3
""" Square class that inherits from Rectangle"""
Rectangle =__import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Sqaure class that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__width} / {self.__height}"

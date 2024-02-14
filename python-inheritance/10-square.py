#!/usr/bin/python3
"""Module for class square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle.

    Represents a square with equal width and height.
    """

    def __init__(self, size):
        """Initialize a new Square instance.
        Validates size using integer_validator from Rectangle class.
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

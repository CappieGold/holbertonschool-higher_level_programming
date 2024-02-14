#!/usr/bin/python3
"""Module for the BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class for future geometric shapes.

    This class is intended to serve as a foundation for creating
    geometric shapes and includes methods to be implemented in subclasses.
    """

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry.

    Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

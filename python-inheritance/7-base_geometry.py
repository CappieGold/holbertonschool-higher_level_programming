#!/usr/bin/python3
"""Module for the BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class for future geometric shapes.

    This class serves as a foundation for creating geometric shapes.
    It includes methods that are expected to be implemented in child classes.
    """
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

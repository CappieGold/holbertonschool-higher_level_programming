#!/usr/bin/python3
"""Module for the BaseGeometry class.

This module provides the BaseGeometry class used as a base class
for other geometric shapes in future implementations.
"""

class BaseGeometry:
    """BaseGeometry class for future geometric shapes.

    This class is intended to serve as a foundation for creating
    geometric shapes and includes methods to be implemented in subclasses.
    """

    def __init__(self):
        """Initialize BaseGeometry instance."""
        pass

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: if the method is not implemented in a subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

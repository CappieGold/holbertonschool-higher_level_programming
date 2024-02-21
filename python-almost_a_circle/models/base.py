#!/usr/bin/python3
"""Module for class Base"""


class Base:
    """ Base class for future models. Manages id assignment. """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of Base.

        Args:
            id (int, optional): The id of the object. If not provided, it's
            automatically assigned based on __nb_objects.

        Attributes:
            id (int): The public id of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

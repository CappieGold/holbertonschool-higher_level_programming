#!/usr/bin/python3


class Base:
    """ Base class for future models. Manages id assignment. """

    _nb_objects = 0

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
            Base._nb_objects += 1
            self.id = Base._nb_objects

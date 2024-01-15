#!/usr/bin/python3
"""Defines the first class."""


class Base:
    """Defines base class. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructs a class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

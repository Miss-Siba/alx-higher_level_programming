#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by ALX."""

import math


class MagicClass:
    """Represents a magic circle with radius."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass with a given radius.

        Args:
            radius (int or float): The radius of the magic circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns:
            float: The area of the magic circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate and return the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return (2 * math.pi * self.__radius)

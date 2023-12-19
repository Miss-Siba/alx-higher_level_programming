#!/usr/bin/python3

"""Defines asquare"""


class Square:
    """Represents a Square."""
    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.size = size

    @property
    def size(self):
        """Returns the current Square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current Square area."""
        return (self.__size * self.__size)

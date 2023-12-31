#!/usr/bin/python3

"""Define a square class"""


class Square:
    """Represents a Square."""
    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current Square area."""
        return (self.__size * self.__size)

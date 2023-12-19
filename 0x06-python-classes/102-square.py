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

    def my_print(self):
        """Prints in stdout square with #."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square."""
        if self.__size == 0:
            return ""

        square_str = "\n" * self.__position[1]

        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"

        return square_str.rstrip("\n")

    def __eq__(self, other):
        """Equality comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparison."""
        return self.area() <= other.area()

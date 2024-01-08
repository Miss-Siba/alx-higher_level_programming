#!/usr/bin/python3
"""Defines an int subclass MyInt """


class MyInt(int):
    """ Represents MyInt function """

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value

#!/usr/bin/python3
""" Defines a function """


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class
    otherwise false. """
    return type(obj) is a_class

#!/usr/bin/python3
"""Defines an inherited class"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """Writes a class inherited from list"""
        sorted_list = sorted(self)
        print(sorted_list)

#!/usr/bin/python3
"""Defines a text reading function."""


def read_file(filename=""):
    """Reads a text file and prints to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")

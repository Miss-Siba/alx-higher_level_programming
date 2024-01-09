#!/usr/bin/python3
"""Define a string writing function. """


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
    returns number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/pythoin3
"""Defines a JSON-to-object function."""


import json


def from_json_string(my_str):
    """Returs an object (Python data structure)
    represented by a JSON string."""
    python_object = json.loads(my_str)
    return python_object

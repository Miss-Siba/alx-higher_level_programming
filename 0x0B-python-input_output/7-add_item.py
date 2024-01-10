#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""

import sys
from importlib import import_module

save_to_json_file_module = import_module('5-save_to_json_file')
load_from_json_file_module = import_module('8-load_from_json_file')


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

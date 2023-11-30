#!/usr/bin/python3
import sys


def add_int():
    num_arguments = len(sys.argv) - 1

    result = sum(int(arg) for arg in sys.argv[1:])

    print(result)


if __name__ == "__main__":
    add_int()

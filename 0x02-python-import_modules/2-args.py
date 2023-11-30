#!/usr/bin/python3
import sys


def print_arguments():
    num_arguments = len(sys.argv) - 1

    if num_arguments == 1:
        print(f"{num_arguments} argument:")
    elif num_arguments == 0:
        print("0 arguments.")
    else:
        print(f"{num_arguments} arguments:")
    for i in range(1, num_arguments + 1):
        print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":
    print_arguments()

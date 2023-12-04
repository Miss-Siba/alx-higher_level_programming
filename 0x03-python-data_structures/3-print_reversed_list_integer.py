#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list.copy()
    reversed_list.reverse()
    if my_list is None:
        return

    for num in reversed_list:
        print("{:d}".format(num))

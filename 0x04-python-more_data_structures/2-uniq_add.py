#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return (None)
    unique_integers = set()
    result = 0

    for number in my_list:
        if isinstance(number, int) and number not in unique_integers:
            result += number
            unique_integers.add(number)

    return (result)

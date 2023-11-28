#!/usr/bin/python3
for number in range(10):
    for one_digit in range(number + 1, 10):
        print("{:d}{:d}".format(number, one_digit), end=", " if one_digit < 9 else "\n")

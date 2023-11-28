#!/usr/bin/python3
for number in range(10):
    for one_digit in range(number + 1, 10):
        end_char = ", " if one_digit < 9 or number < 8 else "\n"
        print("{:d}{:d}".format(number, one_digit), end=end_char)

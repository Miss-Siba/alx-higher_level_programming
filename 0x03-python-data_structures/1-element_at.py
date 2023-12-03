#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list):
        return (None)
    else:
        current_idx = 0
        for element in my_list:
            if current_idx == idx:
                return element
            current_idx += 1

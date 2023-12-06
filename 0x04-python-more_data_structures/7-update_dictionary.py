def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
        print(value)
    else:
        a_dictionary[key] = value
        print(a_dictionary[key])

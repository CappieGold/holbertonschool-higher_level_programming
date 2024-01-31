#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for j, i in a_dictionary.items():
        i = i * 2
        new_dict[j] = i
    return new_dict

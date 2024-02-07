#!/usr/bin/python3
"""
text indentation
author: Carpentier
date: 07/02/2024
"""


def text_indentation(text):
    """
    double \n after specific char
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        print("\n\n", end="")

    char_list = [".", "?", ":"]
    new_line_added = False

    for char in text:
        if new_line_added and char == " ":
            continue
        print(char, end="")
        if char in char_list:
            print("\n\n", end="")
            new_line_added = True
        else:
            new_line_added = False

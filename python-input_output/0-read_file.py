#!/usr/bin/python3
"""read content of file with: with, r and utf 8"""


def read_file(filename=""):
    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        content = f.read()
        print(content, end='')

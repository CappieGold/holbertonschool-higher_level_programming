#!/usr/bin/python3
def read_file(filename=""):
    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        content = f.read()
        print(content)

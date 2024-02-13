#!/usr/bin/python3
"""class my list inherits list"""


class MyList(list):
    """print list sorted"""
    def print_sorted(self):
        print(sorted(self))

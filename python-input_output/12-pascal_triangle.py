#!/usr/bin/python3
"""Module to generate Pascal's triang"""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triang of n."""
    if n <= 0:
        return []

    triang = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triang[i-1][j-1] + triang[i-1][j])
        row.append(1)
        triang.append(row)

    return triang

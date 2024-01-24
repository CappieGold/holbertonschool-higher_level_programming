#!/usr/bin/python3
i = 0
j = 1
for i in range(8):
    for j in range(10):
        if i == j or i > j:
            continue
        print("{}{}, ".format(i, j), end="")
print("89")

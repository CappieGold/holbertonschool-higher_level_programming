#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    j = 1
    add = 0
    if i == 0:
        print("{}".format(i))
    else:
        while j <= i:
            add += int(argv[j])
            j += 1
        print("{}".format(add))

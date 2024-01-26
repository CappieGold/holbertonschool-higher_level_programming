#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    j = 1
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
        print("{}: {}".format(i, argv[1]))
    else:
        print("{} arguments:".format(i))
        while j <= i:
            print("{}: {}".format(j, argv[j]))
            j += 1

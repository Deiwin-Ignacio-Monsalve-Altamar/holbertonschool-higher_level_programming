#!/usr/bin/python3
def args(argv):
    num = len(argv) - 1

    if num <= 0:
        print("{} arguments.".format(num))
    elif num > 0:
        s = "s"
        if num <= 1:
            s = ""
        print("{} argument{}:".format(num, s))
        for i in range(num):
            print("{}: {}".format(i + 1, argv[i + 1]))


if __name__ == '__main__':
    import sys
    args(sys.argv)

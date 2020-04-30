#!/usr/bin/python3


def addfinite(argv):
    num = len(argv) - 1
    if num <= 0:
        print("{}".format(num))
    else:
        add = 0
        for i in argv[1:]:
            add = add + int(i)
        print("{}".format(add))


if __name__ == '__main__':
    import sys
    addfinite(sys.argv)

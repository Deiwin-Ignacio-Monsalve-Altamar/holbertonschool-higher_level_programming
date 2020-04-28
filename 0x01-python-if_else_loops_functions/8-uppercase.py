#!/usr/bin/python3
def uppercase(str):
    for leter in str:
        letter = ord(leter)
        if letter >= 97 and letter <= 122:
            letter = letter - 32
        print("{}".format(chr(letter)), end="")
    print()

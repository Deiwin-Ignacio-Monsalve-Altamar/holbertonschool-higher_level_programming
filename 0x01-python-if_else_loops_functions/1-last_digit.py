#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number >= 0:
    result = number % 10
else:
    result = number % -10

last, isstring, mayor = "Last digit of", "is", "and is less than 6 and not 0"
igual, menor = "and is 0", "and is greater than 5"

if result == 0:
    print("{} {:d} {} {:d} {}".format(last, number, isstring, result, igual))
elif result < 6:
    print("{} {:d} {} {:d} {}".format(last, number, isstring, result, mayor))
else:
    print("{} {:d} {} {:d} {}".format(last, number, isstring, result, menor))

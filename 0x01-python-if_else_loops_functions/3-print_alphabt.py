#!/usr/bin/python3
for letras in range(97, 123):
    if (letras != 113) and (letras != 101):
        print("{:c}".format(letras), end='')

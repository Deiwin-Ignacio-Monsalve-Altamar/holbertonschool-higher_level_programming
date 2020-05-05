#!/usr/bin/python3
def multiple_returns(sentence):
    longitud = len(sentence)
    if longitud > 0:
        first = sentence[0]
    else:
        first = None
    return (longitud, first)

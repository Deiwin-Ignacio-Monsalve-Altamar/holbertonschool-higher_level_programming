#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = 0
        for j in i:
            count = count + 1
            if count < len(i):
                print("{}".format(j), end=" ")
            else:
                print("{}".format(j), end="")
        print()

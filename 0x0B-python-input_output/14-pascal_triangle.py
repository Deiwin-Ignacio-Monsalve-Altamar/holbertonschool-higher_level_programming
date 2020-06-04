#!/usr/bin/python3


"""Pascal Triangle"""


def pascal_triangle(n):
    """
    Args:
        n (int): the depth of pascal's
    """
    if n <= 0:
        return []

    new_array = []
    for num in range(1, n + 1):
        new = []
        for i in range(num):
            if i == 0 or i == num - 1:
                new.append(1)
            else:
                new.append(new_array[num - 2][i] + new_array[num - 2][i - 1])
        new_array.append(new)

    return new_array

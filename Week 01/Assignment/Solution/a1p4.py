"""
ECE606, F'21, Assignment 1, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code as you like.
"""


"""
d, positive integer, is the number of digits we allow
i, an integer in the intercal [-10^d/2, 10^d/2-1]
"""
def encode(d, i):
    max = 10**d
    result = i % max

    return result

"""
d, positive integer, is the number of digits we allow
i, an integer in the intercal [0, 10^d-1]
"""
def decode(d, i): # Use the equation x = yq + r
    q = 0
    y = 10**d
    r = i

    min_int = -10**d / 2
    max_int = 10**d / 2 -1

    not_found = True
    while not_found:
        if min_int <= y*q + r <= max_int:
            result = y*q + r
            not_found = False
        q -= 1

    return result

"""
d, positive integer, is the number of digits we allow
i and j, integers in the interval [0, 10^d-1], and assume to encode intergers in interval [-10^d/2, 10^d/2-1]
"""
def add(d, i, j):
    result = decode(d, i) + decode(d, j)
    return result

"""
d, positive integer, is the number of digits we allow
i and j, integers in the interval [0, 10^d-1], and assume to encode intergers in interval [-10^d/2, 10^d/2-1]
"""
def multiply(d, i, j):
    x = i
    y = j

    if y == 0:
        return 0
    elif y > 0 and y % 2 == 0:
        return multiply(d, 2*x, y//2)
    else:
        return add(d, x , multiply(d, 2*x, y//2))
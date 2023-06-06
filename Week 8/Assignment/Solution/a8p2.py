"""
ECE606, F'21, Assignment 8, Problem 2(b)
Skeleton solution file.
"""

import random

"""
You are not allowed to import anything else. You are
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""

def avgsatisfied(G, k):
    """
    You need to implement this method. See the handout for its specs.
    NOTE: you should *NOT* modify the argument G. You should assume
          "read-only" access to it only. Make a copy of it first if you
          feel you need to modify it.
    """
    counter = 0
    a = len(G)/2
    prime = 7901
    while (counter < 5000):
        visited_edge = []
        c = 0
        for i in range(len(G)):
            vertex = G[i]
            for j in range(len(vertex)):
                if (i, vertex[j]) not in visited_edge and (vertex[j], i) not in visited_edge:
                    visited_edge.append((i, vertex[j]))

                    u = (i * prime) ** 3 % (k-1)
                    v = (vertex[j] * prime) ** 3 % (k-1)

                    if u != v:
                        c += 1
        a += c 
        counter += 1
        #print(a)
    
    return (a / 5000)

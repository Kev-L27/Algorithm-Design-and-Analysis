#! /usr/bin/python3

import sys
import random
from a8p2 import avgsatisfied

"""
Some tests.
"""

def slack(r):
    return 0.1 * r

def main():
    print('Test 1:', end = ' ')
    G = [[2,1,3], [0,3],[3,0],[1,2,0]]
    a = avgsatisfied(G, 4)
    r = 3.75
    if a and a >= r - slack(r) and a <= r + slack(r):
        print('Passed')
    else:
        print('Failed')

    G = list()

    # Vertex 0
    G.append(list())
    G[0].append(1)
    G[0].append(7)

    # Vertex 1
    G.append(list())
    G[1].append(0)
    G[1].append(2)
    G[1].append(7)

    # Vertex 2
    G.append(list())
    G[2].append(1)
    G[2].append(3)
    G[2].append(8)
    G[2].append(5)

    # Vertex 3
    G.append(list())
    G[3].append(2)
    G[3].append(5)
    G[3].append(4)

    # Vertex 4
    G.append(list())
    G[4].append(3)
    G[4].append(5)

    # Vertex 5
    G.append(list())
    G[5].append(4)
    G[5].append(3)
    G[5].append(2)
    G[5].append(6)

    # Vertex 6
    G.append(list())
    G[6].append(5)
    G[6].append(7)
    G[6].append(8)

    # Vertex 7
    G.append(list())
    G[7].append(8)
    G[7].append(0)
    G[7].append(1)
    G[7].append(6)

    # Vertex 8
    G.append(list())
    G[8].append(2)
    G[8].append(6)
    G[8].append(7)

    print('Test 2:', end = ' ')
    a = avgsatisfied(G, 7)
    r = 12

    if a and a >= r - slack(r) and a <= r + slack(r):
        print('Passed')
    else:
        print('Failed')

    print('Test 3:', end = ' ')
    a = avgsatisfied(G, 5)
    r = 11.2

    if a and a >= r - slack(r) and a <= r + slack(r):
        print('Passed')
    else:
        print('Failed')

if __name__ == '__main__':
    main()

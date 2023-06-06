#! /usr/bin/python3

import sys
import random
from a6p4 import hasmst

"""
Some tests.

If you set this file to executable, and have the a6p4.py file in
the same folder, then you should be able to run this.
"""

def main():
    print('Test 1:', end = ' ')
    G = [[[2,10],[1,10], [3,30]],[[0,10],[3,20]],[[3,20],[0,10]],[[1,20],[2,20],[0,30]]]
    e = [0,3]
    ret = hasmst(G, e)
    if ret == None or ret:
        print('Failed')
    else:
        print('Passed')

    print('Test 2:', end = ' ')
    e = [2,3]
    ret = hasmst(G, e)
    if ret == None or not ret:
        print('Failed')
    else:
        print('Passed')

    print('Test 3:', end = ' ')
    e = [3,2]
    ret = hasmst(G, e)
    if ret == None or not ret:
        print('Failed')
    else:
        print('Passed')

    G = list()

    # Vertex 0
    G.append(list())
    G[0].append([1,4])
    G[0].append([7,8])

    # Vertex 1
    G.append(list())
    G[1].append([0,4])
    G[1].append([2,8])
    G[1].append([7,11])

    # Vertex 2
    G.append(list())
    G[2].append([1,8])
    G[2].append([3,7])
    G[2].append([8,2])
    G[2].append([5,4])

    # Vertex 3
    G.append(list())
    G[3].append([2,7])
    G[3].append([5,14])
    G[3].append([4,9])

    # Vertex 4
    G.append(list())
    G[4].append([3,9])
    G[4].append([5,10])

    # Vertex 5
    G.append(list())
    G[5].append([4,10])
    G[5].append([3,14])
    G[5].append([2,4])
    G[5].append([6,2])

    # Vertex 6
    G.append(list())
    G[6].append([5,2])
    G[6].append([7,1])
    G[6].append([8,6])

    # Vertex 7
    G.append(list())
    G[7].append([8,7])
    G[7].append([0,8])
    G[7].append([1,11])
    G[7].append([6,1])

    # Vertex 8
    G.append(list())
    G[8].append([2,2])
    G[8].append([6,6])
    G[8].append([7,7])

    print('Test 4:', end = ' ')

    e = [2,3]
    ret = hasmst(G, e)
    if ret == None or not ret:
        print('Failed')
    else:
        print('Passed')

    print('Test 5:', end = ' ')
    e = [2,1]
    ret = hasmst(G, e)
    if ret == None or not ret:
        print('Failed')
    else:
        print('Passed')

    print('Test 6:', end = ' ')
    e = [8,6]
    ret = hasmst(G, e)
    if ret == None or ret:
        print('Failed')
    else:
        print('Passed')

if __name__ == '__main__':
    main()

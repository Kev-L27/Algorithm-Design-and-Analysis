#! /usr/bin/python3

import sys
import random
from a4p1 import anotherst

"""
Some tests.

If you set this file to executable, and have the a4p1.py file in
the same folder, then you should be able to run this.
"""

def isTree(G, T):
    # Basic tests first against G
    if len(T) != len(G):
        return False
    for u in range(len(T)):
        for v in T[u]:
            if v not in G[u]:
                return False

    # Now BFS on T to confirm that it's a tree
    # But need to adapt BFS somewhat carefully
    colour = list()
    pi = list()
    for i in range(len(T)):
        colour.append(False) # False == WHITE
        pi.append(-1) # -1 == NIL
    Q = list()
    Q.append(0)
    colour[0] = True
    while Q:
        u = Q.pop(0)
        for v in T[u]:
            if not colour[v]:
                colour[v] = True
                pi[v] = u
                Q.append(v)
            elif pi[u] != v: # This is the key check
                return False
    return True

def isDifferent(P, Q):
    # Are the graphs P and Q different?
    if(len(P) != len(Q)):
        return True
    
    for u in range(len(P)):
        for v in P[u]:
            if v not in Q[u]:
                return True

    for u in range(len(Q)):
        for v in Q[u]:
            if v not in P[u]:
                return True
    
    return False

def graphCopy(G):
    H = list()
    for i in range(len(G)):
        H.append(list())
        for j in G[i]:
            (H[i]).append(j)
    return H

def main():
    print('Test 1:', end = ' ')
    G = [[2,3,4],[2,3],[0,1],[0,1,4],[0,3]]
    T = [[2,3],[3],[0],[0,1,4],[3]]
    # Make a copies of G and T
    H = graphCopy(G)
    S = graphCopy(T)
    Tprime = anotherst(G, T)
    success = Tprime and (isTree(H, Tprime) and isDifferent(Tprime, S))
    if success:
        print('Passed')
    else:
        print('Failed')

    print('Test 2:', end = ' ')
    G = [[1,7],[0,2,7],[1,3,5,8],[2,4,5],[3,5],[2,3,4,6],[5,7,8],[0,1,6,8],[2,6,7]]
    T = [[1],[0,2],[1,3,5,8],[2,4],[3],[2,6],[5,7],[6],[2]]
    # Make a copies of G and T
    H = graphCopy(G)
    S = graphCopy(T)
    Tprime = anotherst(G, T)
    success = Tprime and (isTree(H, Tprime) and isDifferent(Tprime, S))
    if success:
        print('Passed')
    else:
        print('Failed')

    print('Test 3:', end = ' ')
    G = [[2, 3, 4], [2], [0, 1], [0], [0]]
    T = [[2, 3, 4], [2], [0, 1], [0], [0]]
    Tprime = anotherst(G, T)
    success = (not Tprime)
    if success:
        print('Passed')
    else:
        print('Failed')

if __name__ == '__main__':
    main()

"""
ECE606, F'21, Assignment 4, Problem 1
Skeleton solution file.
"""

"""
You are not allowed to import anything. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""

def anotherst(G, T):
    result = BFS(G, 0)
    if isDifferent(result, T):
        return result
    result = BFS(G, len(G)-1)
    if isDifferent(result, T):
        return result
    else:
        return None

def BFS(G, s):
    T_Prime = [[] for i in range(len(G))]
    color = [None]*len(G)
    pi = [None]*len(G)
    for u in range(len(G)):
        if u != s:
            color[u] = "White"
            pi[u] = None

    color[s] = "Gray"
    pi[s] = None
    queue = []
    queue.append(s)
    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if color[v] == "White":
                T_Prime[u].append(v)
                color[v] = "Gray"
                pi[v] = u
                queue.append(v)
        if pi[u] != None:
            T_Prime[u].append(pi[u])
        color[u] = "Black"
    
    return T_Prime

'''
This function isDifferent is copied from tester-a4p1.py, and credit to Professor Tripunitara
'''
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

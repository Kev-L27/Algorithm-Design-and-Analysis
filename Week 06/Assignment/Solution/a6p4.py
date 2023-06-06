"""
ECE606, F'21, Assignment 6, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything. You are
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""

def hasmst(G, e):
    """
    You need to implement this method. See the handout for its specs.
    NOTE: you should *NOT* modify either of the arguments G, e. You
          have "read-only" access to them only. If you modify them,
          you'll get an automatic 0 on this problem.
    """
    u = e[0]
    v = e[1]
    for i in G[u]:
          if i[0] == v:
            e_weight = i[1]
    result = BFS(G, u, v, e_weight)
    return (not result)


def BFS(G, s, target, e):
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
            vertex = v[0]
            weight = v[1]
            if color[vertex] == "White":
                  if weight < e:
                        if vertex == target:
                              return True
                        color[vertex] = "Gray"
                        pi[vertex] = u
                        queue.append(vertex)
        color[u] = "Black"

    
    return False
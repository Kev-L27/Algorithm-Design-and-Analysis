#!/usr/bin/python
import math

def MinCoinsDP (a, c):
    k = len(c)
    M = [None] * (a+1)
    S = [None] * (a+1)
    
    if a == 0:
        return [0]*k
    
    for i in range(a+1):
        if i == 0:
            M[i] = 0
            S[0] = [0]*k
        else:
            M[i] = math.inf
            for j in range(k):
                if i >= c[j]:
                    if M[i] > (1+M[i-c[j]]):
                        temp = S[i-c[j]][:]
                        M[i] = 1+M[i-c[j]]
                        temp[j] += 1
                        #print(temp)
            S[i] = temp[:]
            
                        
                            
    return S[a]

#test = [1,12,28,114]
test = [1,3,4]
#for i in range(7):
    #result = MinCoinsDP(i,test)
    #print(i, ": ", result)
result = MinCoinsDP(7,test)
print(result)
#print(M)#
import math

def buildbst(s):

    length = len(s)
    height = math.floor(math.log2(length))
    set = sorted(s)

    leftmost = 2**height-1
    result = [0] * len(set)
    i = 0
    node = True # T for left, F for right
    root = False # False means hasn't reached root
    check = False
    visited = []
    visited.append(leftmost)
    while i < len(s):
        #print(result)
        print(leftmost)
        
        if leftmost == 0:
            result[leftmost] = set[i]
            root = True

        if root == False:
            result[leftmost] = set[i]
            if node == True:
                parent = int((leftmost-1)/2)
                right_node = int(2*leftmost+2)
                if (right_node < len(s)):
                    leftmost = right_node
                    node = False
                    visited.append(leftmost)
                else:
                    leftmost = parent
                    visited.append(leftmost)
            else:
                temp = int((leftmost-2)/2)
                parent = int((temp-1)/2)
                leftmost = parent
                node = True
                visited.append(leftmost)
        else: # Here have reached root node, need to traverse the leftmost of the right subtree
            j = 2**height-1

            if not check:
                while j in visited:
                    j += 1
                if j >= len(s):
                    j = 2**(height-1)-1
                    while j in visited:
                        j += 1

                leftmost = j
                i += 1
                #print(leftmost)
                result[leftmost] = set[i]
                check = True
                node = True
                i += 1
                continue
            else:
                #print(i)
                if node == True:
                    parent = int((leftmost-1)/2)
                    right_node = int(2*leftmost+2)
                    if (right_node < len(s)):
                        leftmost = right_node
                        result[leftmost] = set[i]
                        node = False
                        visited.append(leftmost)
                    else:
                        leftmost = parent
                        result[leftmost] = set[i]
                        visited.append(leftmost)
                else:
                    parent = int((((leftmost-2)/2)-2)/2)
                    leftmost = parent
                    result[leftmost] = set[i]
                    node = True
                    visited.append(leftmost)

        #print(i)


        i += 1
    
    return result
         


test = buildbst({1,2,3,4,5,6,7,8})
#print(test)
print(test)




"""
ECE606, F'21, Assignment 2, Problem 4
Skeleton solution file.
"""

import math

"""
You are not allowed to import anything else. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""
result = []

def buildbst(s):

    length = len(s)
    height = math.floor(math.log2(length))
    set = sorted(s)
    
    """    
    result = [0] * len(set)
    #The position of the root node within the sorted set is 2^n-1 --> set[2^n-1], where n is the height of the tree
    #result[0] = set[2**height - 1]


    #The position of the leftmost node within the result list is 2^n-1 --> result[2^n-1], where n is the height of the tree. And the key of the node is the first in the sorted set.
    #for left child, its parent is at position (i-1)/2 where i is its index
    #for right child, its parent is at position (i-2)/2 where i is its index
    leftmost = 2**height-1
    
    result[leftmost] = set[0]

    
    print(result)
    """
    #result = []

    root_pos = 2**height-1
    root = set[root_pos]

    result.append(root)

    left_sub = set[:root_pos]
    right_sub = set[root_pos+1:]

    if len(left_sub) > 0:
        #print(left_sub)
        #result.append(buildbst(left_sub))
        buildbst(left_sub)

    if len(right_sub) > 0:
        #result.append(buildbst(right_sub))
        buildbst(right_sub)

    #print(result)
    return root
    #return result

test = (12-1)/2
print(test.is_integer())








#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def buildbst(s):

    length = len(s)
    height = math.floor(math.log2(length))
    set = sorted(s)
    leftmost = 2**height-1
    result = [0] * len(set)
    i = 0
    node = True # T for left, F for right
    root = False # False means hasn't reached root
    check = False
    visited = []
    visited.append(leftmost)
    while i < len(s):
        #print(result)
        #print(leftmost)
        
        if leftmost == 0:
            result[leftmost] = set[i]
            root = True

        if root == False:
            #print(leftmost,": ",set[i])
            result[leftmost] = set[i]
            if node == True:
                left_node = int(2*leftmost + 1)
                parent = int((leftmost-1)/2)
                right_node = int(2*leftmost+2)
                if not left_node >= len(s):
                    while left_node < len(s):
                        left_node = int(2*left_node + 1)
                    left_node = int((left_node-1)/2)
                    if (left_node < len(s) and left_node not in visited):# It has left node
                        leftmost = left_node
                        visited.append(leftmost)
                    elif (right_node < len(s)): # It has right node
                        left_node = 2*right_node + 1
                        if not left_node >= len(s):
                            while left_node < len(s):
                                left_node = int(2*left_node + 1)
                            left_node = int((left_node-1)/2)
                            if (left_node < len(s) and left_node not in visited):
                                leftmost = left_node
                                visited.append(leftmost)
                            else:
                                leftmost = right_node
                                node = False
                                visited.append(leftmost)
                        else:
                            leftmost = right_node
                            node = False
                            visited.append(leftmost)
                    else:# No children, then go back to parent node
                        leftmost = parent
                        visited.append(leftmost)
                elif (right_node < len(s)):
                    left_node = 2*right_node + 1
                    if not left_node >= len(s):
                        while left_node < len(s):
                            left_node = int(2*left_node + 1)
                        left_node = int((left_node-1)/2)
                        if (left_node < len(s) and left_node not in visited):
                            leftmost = left_node
                            visited.append(leftmost)
                        else:
                            leftmost = right_node
                            node = False
                            visited.append(leftmost)
                    else:
                        leftmost = right_node
                        node = False
                        visited.append(leftmost)
                else:
                    leftmost = parent
                    visited.append(leftmost)
            else:
                left_node = int(2*leftmost + 1)
                if not left_node >= len(s):
                    while left_node < len(s):
                        left_node = int(2*left_node + 1)
                    left_node = int((left_node-1)/2)
                    if (left_node < len(s) and left_node not in visited):
                        leftmost = left_node
                        node = True
                        visited.append(leftmost)
                    else:
                        temp = (leftmost-2)/2
                        while temp in visited:
                            temp = (temp-2)/2
                            #print("df",temp)
                        temp = 2*temp + 2
                        parent = int((temp-1)/2)# Find the parent of the parent
                        leftmost = parent
                        node = True
                        visited.append(leftmost)
                else:#If it doesn't have left child, then it definitely doesn't have right child
                    temp = (leftmost-2)/2
                    while temp in visited:
                        temp = (temp-2)/2
                        #print("df",temp)
                    temp = 2*temp + 2
                    parent = int((temp-1)/2)# Find the parent of the parent
                    leftmost = parent
                    node = True
                    visited.append(leftmost)
        else: # Here have reached root node, need to traverse the leftmost of the right subtree
            j = 2**height-1

            if not check:
                while j in visited:
                    j += 1
                if j >= len(s):
                    j = 2**(height-1)-1
                    while j in visited:
                        j += 1

                leftmost = j
                i += 1
                #print(i,leftmost)
                #print(leftmost,": ",set[i])
                result[leftmost] = set[i]
                visited.append(leftmost)
                check = True
                node = True
                #i += 1
                continue
            else:
                result[leftmost] = set[i]
                #print(leftmost,": ",set[i])
                if not(((leftmost-1)/2).is_integer()):
                    node = False
                else:
                    node = True
                #print(node)
                if node == True:
                    left_node = int(2*leftmost + 1)
                    parent = int((leftmost-1)/2)
                    right_node = int(2*leftmost+2)
                    if not left_node >= len(s):
                        while left_node < len(s):
                            left_node = int(2*left_node + 1)
                        left_node = int((left_node-1)/2)
                        if (left_node < len(s) and left_node not in visited):
                            leftmost = left_node
                            visited.append(leftmost)
                        elif (right_node < len(s)):
                            left_node = 2*right_node + 1
                            if not left_node >= len(s):
                                while left_node < len(s):
                                    left_node = int(2*left_node + 1)
                                left_node = int((left_node-1)/2)
                                if (left_node < len(s) and left_node not in visited):
                                    leftmost = left_node
                                    visited.append(leftmost)
                                else:
                                    leftmost = right_node
                                    node = False
                                    visited.append(leftmost)
                            else:
                                leftmost = right_node
                                node = False
                                visited.append(leftmost)
                        else:
                            leftmost = parent
                            visited.append(leftmost)
                    elif (right_node < len(s)):
                        left_node = 2*right_node + 1
                        if not left_node >= len(s):
                            while left_node < len(s):
                                left_node = int(2*left_node + 1)
                            left_node = int((left_node-1)/2)
                            if (left_node < len(s) and left_node not in visited):
                                leftmost = left_node
                                visited.append(leftmost)
                            else:
                                leftmost = right_node
                                node = False
                                visited.append(leftmost)
                        else:
                            leftmost = right_node
                            node = False
                            visited.append(leftmost)
                    else:
                        #print("leftmost is from {} to {}".format(leftmost, parent))
                        leftmost = parent
                        visited.append(leftmost)
                else:
                    #print(leftmost,": ",set[i])
                    left_node = int(2*leftmost + 1)
                    if not left_node >= len(s):
                        while left_node < len(s):
                            left_node = int(2*left_node + 1)
                        left_node = int((left_node-1)/2)
                        if (left_node < len(s) and left_node not in visited):
                            leftmost = left_node
                            node = True
                            visited.append(leftmost)
                        else:
                            temp = (leftmost-2)/2
                            while temp in visited:
                                temp = (temp-2)/2
                                #print("df",temp)
                            temp = 2*temp + 2
                            parent = int((temp-1)/2)# Find the parent of the parent
                            if parent in visited:
                                right_node = 2*leftmost+2
                                if right_node < len(s):
                                    left_node = 2*right_node + 1
                                    if not left_node >= len(s):
                                        while left_node < len(s):
                                            left_node = int(2*left_node + 1)
                                        left_node = int((left_node-1)/2)
                                        if (left_node < len(s) and left_node not in visited):
                                            leftmost = left_node
                                            visited.append(leftmost)
                                        else:
                                            leftmost = right_node
                                            node = False
                                            visited.append(leftmost)
                                    else:
                                        leftmost = right_node
                                        node = False
                                        visited.append(leftmost)
                                else:
                                    #print("leftmost is from {} to {}".format(leftmost, parent))
                                    leftmost = parent
                                    visited.append(leftmost)
                            else:
                                leftmost = parent
                                node = True
                                visited.append(leftmost)
                    else:#If it doesn't have left child, then it definitely doesn't have right child
                        temp = (leftmost-2)/2
                        while temp in visited:
                            temp = (temp-2)/2
                            #print("df",temp)
                        temp = 2*temp + 2
                        parent = int((temp-1)/2)# Find the parent of the parent
                        if parent in visited:
                            right_node = 2*leftmost+2
                            if right_node < len(s):
                                left_node = 2*right_node + 1
                                if not left_node >= len(s):
                                    while left_node < len(s):
                                        left_node = int(2*left_node + 1)
                                    left_node = int((left_node-1)/2)
                                    if (left_node < len(s) and left_node not in visited):
                                        leftmost = left_node
                                        visited.append(leftmost)
                                    else:
                                        leftmost = right_node
                                        node = False
                                        visited.append(leftmost)
                                else:
                                    leftmost = right_node
                                    node = False
                                    visited.append(leftmost)
                            else:
                                #print("leftmost is from {} to {}".format(leftmost, parent))
                                leftmost = parent
                                visited.append(leftmost)
                        else:
                            leftmost = parent
                            node = True
                            visited.append(leftmost)

        #print(i)

        #print(leftmost)
        i += 1
    
    return result



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
ECE606, F'21, Assignment 2, Problem 4
Skeleton solution file.
"""

import math

"""
You are not allowed to import anything else. You are, however,
allowed to use any built-in Python 3 language feature and
data structures you like. You are allowed to define any subroutines
you like to structure your code.
"""

def buildbst(s):

    length = len(s)
    height = math.floor(math.log2(length))
    set = sorted(s)
    leftmost = 2**height-1
    result = [0] * len(set)
    i = 0
    node = True # T for left, F for right
    root = False # False means hasn't reached root
    check = False
    visited = []
    visited.append(leftmost)
    while i < len(s):
        #print(result)
        #print(leftmost)
        
        if leftmost == 0:
            result[leftmost] = set[i]
            root = True

        if root == False:
            #print(leftmost,": ",set[i])
            result[leftmost] = set[i]
            if node == True:
                left_node = int(2*leftmost + 1)
                parent = int((leftmost-1)/2)
                right_node = int(2*leftmost+2)
                if not left_node >= len(s):
                    while left_node < len(s):
                        left_node = int(2*left_node + 1)
                    left_node = int((left_node-1)/2)
                    if (left_node < len(s) and left_node not in visited):
                        leftmost = left_node
                        visited.append(leftmost)
                    elif (right_node < len(s)):
                        left_node = 2*right_node + 1
                        if not left_node >= len(s):
                            while left_node < len(s):
                                left_node = int(2*left_node + 1)
                            left_node = int((left_node-1)/2)
                            if (left_node < len(s) and left_node not in visited):
                                leftmost = left_node
                                visited.append(leftmost)
                            else:
                                leftmost = right_node
                                node = False
                                visited.append(leftmost)
                        else:
                            leftmost = right_node
                            node = False
                            visited.append(leftmost)
                    else:
                        leftmost = parent
                        visited.append(leftmost)
                elif (right_node < len(s)):
                    left_node = 2*right_node + 1
                    if not left_node >= len(s):
                        while left_node < len(s):
                            left_node = int(2*left_node + 1)
                        left_node = int((left_node-1)/2)
                        if (left_node < len(s) and left_node not in visited):
                            leftmost = left_node
                            visited.append(leftmost)
                        else:
                            leftmost = right_node
                            node = False
                            visited.append(leftmost)
                    else:
                        leftmost = right_node
                        node = False
                        visited.append(leftmost)
                else:
                    leftmost = parent
                    visited.append(leftmost)
            else:
                left_node = int(2*leftmost + 1)
                if not left_node >= len(s):
                    while left_node < len(s):
                        left_node = int(2*left_node + 1)
                    left_node = int((left_node-1)/2)
                    if (left_node < len(s) and left_node not in visited):
                        leftmost = left_node
                        node = True
                        visited.append(leftmost)
                    else:
                        temp = (leftmost-2)/2
                        while temp in visited:
                            temp = (temp-2)/2
                            #print("df",temp)
                        temp = 2*temp + 2
                        parent = int((temp-1)/2)# Find the parent of the parent
                        leftmost = parent
                        node = True
                        visited.append(leftmost)
                else:#If it doesn't have left child, then it definitely doesn't have right child
                    temp = (leftmost-2)/2
                    while temp in visited:
                        temp = (temp-2)/2
                        #print("df",temp)
                    temp = 2*temp + 2
                    parent = int((temp-1)/2)# Find the parent of the parent
                    leftmost = parent
                    node = True
                    visited.append(leftmost)
        else: # Here have reached root node, need to traverse the leftmost of the right subtree
            j = 2**height-1

            if not check:
                while j in visited:
                    j += 1
                if j >= len(s):
                    j = 2**(height-1)-1
                    while j in visited:
                        j += 1

                leftmost = j
                i += 1
                #print(i,leftmost)
                #print(leftmost,": ",set[i])
                result[leftmost] = set[i]
                visited.append(leftmost)
                check = True
                node = True
                #i += 1
                continue
            else:
                result[leftmost] = set[i]
                #print(leftmost,": ",set[i])
                if node == True:
                    left_node = int(2*leftmost + 1)
                    parent = int((leftmost-1)/2)
                    right_node = int(2*leftmost+2)
                    if not left_node >= len(s):
                        while left_node < len(s):
                            left_node = int(2*left_node + 1)
                        left_node = int((left_node-1)/2)
                        if (left_node < len(s) and left_node not in visited):
                            leftmost = left_node
                            visited.append(leftmost)
                        elif (right_node < len(s)):
                            left_node = 2*right_node + 1
                            if not left_node >= len(s):
                                while left_node < len(s):
                                    left_node = int(2*left_node + 1)
                                left_node = int((left_node-1)/2)
                                if (left_node < len(s) and left_node not in visited):
                                    leftmost = left_node
                                    visited.append(leftmost)
                                else:
                                    leftmost = right_node
                                    node = False
                                    visited.append(leftmost)
                            else:
                                leftmost = right_node
                                node = False
                                visited.append(leftmost)
                        else:
                            leftmost = parent
                            visited.append(leftmost)
                    elif (right_node < len(s)):
                        left_node = 2*right_node + 1
                        if not left_node >= len(s):
                            while left_node < len(s):
                                left_node = int(2*left_node + 1)
                            left_node = int((left_node-1)/2)
                            if (left_node < len(s) and left_node not in visited):
                                leftmost = left_node
                                visited.append(leftmost)
                            else:
                                leftmost = right_node
                                node = False
                                visited.append(leftmost)
                        else:
                            leftmost = right_node
                            node = False
                            visited.append(leftmost)
                    else:
                        leftmost = parent
                        visited.append(leftmost)
                else:
                    left_node = int(2*leftmost + 1)
                    if not left_node >= len(s):
                        while left_node < len(s):
                            left_node = int(2*left_node + 1)
                        left_node = int((left_node-1)/2)
                        if (left_node < len(s) and left_node not in visited):
                            leftmost = left_node
                            node = True
                            visited.append(leftmost)
                        else:
                            temp = (leftmost-2)/2
                            while temp in visited:
                                temp = (temp-2)/2
                                #print("df",temp)
                            temp = 2*temp + 2
                            parent = int((temp-1)/2)# Find the parent of the parent
                            leftmost = parent
                            node = True
                            visited.append(leftmost)
                    else:#If it doesn't have left child, then it definitely doesn't have right child
                        temp = (leftmost-2)/2
                        while temp in visited:
                            temp = (temp-2)/2
                            #print("df",temp)
                        temp = 2*temp + 2
                        parent = int((temp-1)/2)# Find the parent of the parent
                        leftmost = parent
                        node = True
                        visited.append(leftmost)

        #print(i)

        #print(leftmost)
        i += 1
    
    return result

ss = {345 ,3455, 2346, 456, 12345, 567, 5678, 2456,5624, 45623,3466, 34562,3452, 72732, 616, 12, 24525, 2345, 23562, 25325, 456745,5675,3543, 3453, 34564, 3452, 567567}
#print(ss)
test = buildbst(ss)
#print(len(test))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("This is right")
                left_node = int(2*leftmost + 1)
                right_node = int(2*leftmost + 2)
                if not left_node >= len(s):
                    while left_node < len(s):
                        left_node = int(2*left_node + 1)
                    left_node = int((left_node-1)/2)
                    if (left_node < len(s) and left_node not in visited):
                        leftmost = left_node
                        #node = True
                        visited.append(leftmost)
                    elif right_node < len(s):
                        left_node = 2*right_node + 1
                        if not left_node >= len(s):
                            while left_node < len(s):
                                left_node = int(2*left_node + 1)
                            left_node = int((left_node-1)/2)
                            if (left_node < len(s) and left_node not in visited):
                                leftmost = left_node
                                visited.append(leftmost)
                            else:
                                leftmost = right_node
                                #node = False
                                visited.append(leftmost)
                        else:
                            leftmost = right_node
                            #node = False
                            visited.append(leftmost)
                    else:
                        temp = (leftmost-2)/2
                        while temp in visited:
                            temp = (temp-2)/2
                            #print("df",temp)
                        temp = 2*temp + 2
                        parent = int((temp-1)/2)# Find the parent of the parent
                        leftmost = parent
                        #node = True
                        visited.append(leftmost)
                else:#If it doesn't have left child, then it definitely doesn't have right child
                    temp = (leftmost-2)/2
                    while temp in visited:
                        temp = (temp-2)/2
                        #print("df",temp)
                    temp = 2*temp + 2
                    parent = int((temp-1)/2)# Find the parent of the parent
                    leftmost = parent
                    #node = True
                    visited.append(leftmost)
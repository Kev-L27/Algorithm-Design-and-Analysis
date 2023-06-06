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
    height = math.floor(math.log2(length))#This is the height
    set = sorted(s)
    leftmost = 2**height-1#This is the leftmost node
    result = [0] * len(set)#This is the result that will be returned
    i = 0
    node = True # T represent the node is left node, F represent the node is left node
    root = False # False means hasn't reached root
    check = False
    visited = []
    visited.append(leftmost)
    while i < len(s):
        
        #This means it has reached the root node
        if leftmost == 0:
            result[leftmost] = set[i]
            root = True

        if root == False:
            result[leftmost] = set[i]

            #Use this to determine if a node is left or right
            if not(((leftmost-1)/2).is_integer()):
                node = False
            else:
                node = True

            if node == True:#If it's left node
                left_node = int(2*leftmost + 1)
                parent = int((leftmost-1)/2)
                right_node = int(2*leftmost+2)
                #First check the left side, see if there's a left child that hasn't visited yet
                if not left_node >= len(s):
                    while left_node < len(s):
                        left_node = int(2*left_node + 1)
                    left_node = int((left_node-1)/2)
                    if (left_node < len(s) and left_node not in visited):
                        leftmost = left_node
                        visited.append(leftmost)

                    #Check the right side
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
                                visited.append(leftmost)
                        else:
                            leftmost = right_node
                            visited.append(leftmost)
                    #If no left and right child, then go to parent
                    else:
                        leftmost = parent
                        visited.append(leftmost)
                #No left child, then check the right child
                elif (right_node < len(s)):
                    left_node = 2*right_node + 1
                    if not left_node >= len(s): # For thie right side, check its left child first
                        while left_node < len(s):
                            left_node = int(2*left_node + 1)
                        left_node = int((left_node-1)/2)
                        if (left_node < len(s) and left_node not in visited):
                            leftmost = left_node
                            visited.append(leftmost)
                        else:
                            leftmost = right_node
                            visited.append(leftmost)
                    else:
                        leftmost = right_node
                        visited.append(leftmost)
                #If right doesn't work either, then go to parent
                else:
                    leftmost = parent
                    visited.append(leftmost)
            #If it's the right node
            else:
                left_node = int(2*leftmost + 1)
                right_node = int(2*leftmost + 2)
                #First check its left side
                if not left_node >= len(s):
                    while left_node < len(s):
                        left_node = int(2*left_node + 1)
                    left_node = int((left_node-1)/2)
                    if (left_node < len(s) and left_node not in visited):
                        leftmost = left_node
                        visited.append(leftmost)
                    #Then check its right side
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
                                visited.append(leftmost)
                        else:
                            leftmost = right_node
                            visited.append(leftmost)
                    #If neigher left or right works, go to parent
                    else:
                        temp = (leftmost-2)/2
                        while temp in visited:
                            temp = (temp-2)/2
                        temp = 2*temp + 2
                        parent = int((temp-1)/2)# Find the parent of the parent
                        leftmost = parent
                        visited.append(leftmost)
                else:#If it doesn't have left child, then it definitely doesn't have right child
                    temp = (leftmost-2)/2
                    while temp in visited:
                        temp = (temp-2)/2
                    temp = 2*temp + 2
                    parent = int((temp-1)/2)# Find the parent of the parent
                    leftmost = parent
                    visited.append(leftmost)
        else: # Here have reached root node, need to traverse from the leftmost node of the right subtree
            j = 2**height-1

            #Use this if to find the leftmost node of right subtree
            if not check:
                while j in visited:
                    j += 1
                if j >= len(s):
                    j = 2**(height-1)-1
                    while j in visited:
                        j += 1

                leftmost = j
                i += 1
                result[leftmost] = set[i]
                visited.append(leftmost)
                check = True
                continue


            else:
                #Use this to determine if a node is left or right
                if not(((leftmost-1)/2).is_integer()):
                    node = False
                else:
                    node = True

                result[leftmost] = set[i]
                if node == True:#For the left node
                    #First check the left side
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
                        #Then the right side
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
                                    visited.append(leftmost)
                            else:
                                leftmost = right_node
                                visited.append(leftmost)
                        #If neither works, then go to parent
                        else:
                            leftmost = parent
                            visited.append(leftmost)
                    #Check the right child
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
                                visited.append(leftmost)
                        else:
                            leftmost = right_node
                            visited.append(leftmost)
                    else:
                        leftmost = parent
                        visited.append(leftmost)
                else:#For the right node
                    left_node = int(2*leftmost + 1)
                    right_node = int(2*leftmost + 2)
                    #Check its left side first
                    if not left_node >= len(s):
                        while left_node < len(s):
                            left_node = int(2*left_node + 1)
                        left_node = int((left_node-1)/2)
                        if (left_node < len(s) and left_node not in visited):
                            leftmost = left_node
                            visited.append(leftmost)
                        #Check its right side
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
                                    visited.append(leftmost)
                            else:
                                leftmost = right_node
                                visited.append(leftmost)
                        #If neither works, then traverse back the tree
                        else:
                            temp = (leftmost-2)/2
                            while temp in visited:
                                temp = (temp-2)/2
                            temp = 2*temp + 2
                            parent = int((temp-1)/2)# Find the parent of the parent
                            leftmost = parent
                            visited.append(leftmost)
                    else:#If it doesn't have left child, then it definitely doesn't have right child
                        temp = (leftmost-2)/2
                        while temp in visited:
                            temp = (temp-2)/2
                        temp = 2*temp + 2
                        parent = int((temp-1)/2)# Find the parent of the parent
                        leftmost = parent
                        visited.append(leftmost)

        i += 1
    
    return result
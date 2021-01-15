# -*- coding: utf-8 -*-
"""
Taylor Maurer
Final
8/27/2020
"""



class node():
	def __init__(self, value):
	     self.val = value
	     self.next = None
    
def add(listHead, x, y):
    ptr = listHead 
    
    while ptr.next is not None and ptr.val != x:
        ptr = ptr.next
    if ptr.next is None:
        #add to back of list
        newNode = node(y)
        ptr.next = newNode
    else:
        #otherwie the ptr.val is equal to x
        newNode = node(y)
        #point newNode's next at the next value (what comes after
        #x)
        newNode.next = ptr.next
        #point current node (the node where x is) to the newNode
        ptr.next = newNode
    return listHead
        
def printList(listHead):
    ptr = listHead
    while ptr is not None:
        print(ptr.val, end = '->')
        ptr = ptr.next
    print()
    
    
def lastIndexCount(inputString):
    #define empty set:
    myDict = {}
    #on first pass identify last index of appearance by adding to dictionary
    for i, item in enumerate(inputString):
        myDict[item] = i
    #on second pass print
    for dictItem in myDict:
        print(dictItem, end = " ")
        print(myDict[dictItem])
def unionFn(A, B):
    aIndex = 0
    bIndex = 0
    #empty list
    S = []
    
    while aIndex < len(A) and bIndex < len(B):
        if A[aIndex] == B[bIndex]:
            #if elements are equal only add one to S
            S.append(A[aIndex])
            aIndex = aIndex + 1
            bIndex = bIndex + 1
        elif A[aIndex] < B[bIndex]:
            #if a is smaller add it to S
            S.append(A[aIndex])
            aIndex = aIndex + 1
        else:
            #if b is smaller add it to S
            S.append(B[bIndex])
            bIndex = bIndex + 1
            
    #verify no remaining elements in B or A
    while aIndex < len(A):
        S.append(A[aIndex])
        aIndex = aIndex + 1
    while bIndex < len(B):
        S.append(B[bIndex])
        bIndex = bIndex + 1
        
    return S
    
    
def main():
    #Number 6:
    print("-"*50)
    print("Final Number 6")
    
    myList = node(3)
    myList = add(myList, 100,4)
    myList = add(myList, 100,41)
    myList = add(myList, 100,410)
    printList(myList)
    myList = add(myList, 41,100)
    myList5 = add(myList, 4,100)
    printList(myList5)
    
    #Number 9:
    print("-"*50)
    print("Final Number 9")
    s = 'SJSU'
    lastIndexCount(s)
    
    
    #Number 10:
    print("-"*50)
    print("Final Number 10")
    A = [1 ,2 ,3,6,7,9,10]
    B = [3,4,6,7,8]
    print("list a:", A)
    print("list b:", B)
    C = unionFn(A,B)
    
    print("A union B", C)
    
    
main()



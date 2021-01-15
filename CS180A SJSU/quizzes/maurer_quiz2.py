# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:13:32 2020

Quiz 2
Taylor Maurer

"""
#Applicable for number 1
class singlyLinkedList:
    class _Node:
        def __init__(self, e, next = None):
            self._e = e
            self._next = next
            
    def __init__(self):
        self._head = None
        self._size= 0
        
    def add_front(self, e):
        newNode = self._Node(e, self._head)
        self._head = newNode
        self._size += 1
    def is_empty(self):
        return self._size == 0
    
    def remove_first(self):
        if self.is_empty():
            print("linked list empty")
            return -1
        removedNode = self._head
        self._head = self._head._next
        self._size -= 1
        return removedNode
    def printList(self):
        if not self.is_empty():
            ptr = self._head
            for i in range(self._size-1):
                print(ptr._e, end = "->")
                ptr = ptr._next
            print(ptr._e)
    #THIS FUNCTION IS FOR NUMBER 1 SPECIFICALLY (The others help test)
    def printSecondToLast(self):
        if not self.is_empty():
            ptr = self._head
            #use - 2 instead of -1 because I want to stop at second to last
            for i in range(self._size - 2):
                ptr = ptr._next
            print(ptr._e)
            
            
#Applicable for number 2
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def printPostOrder(self):
        #check if leaf
        if self.left is None and self.right is None:
            print(self.val, end=" ")

        else:
            self.left.printPostOrder()
            self.right.printPostOrder()
            print(self.val, end= " ")

#Applicable for number 3
def minOccurenceNumber(inArray):
    #define empty set:
    myDict = {}

    minCount = 10000000000 #Should really be infinity, but hopefully this works
    minItem = 0
    for i, item in enumerate(inArray):
        myDict[item] = myDict.get(item, 0) + 1
        
        #continue to keep track of minimum counted item
        if myDict.get(minItem,minCount) > myDict[item]:
            minItem = item

            minCount = myDict[item]
    
    return minItem
        

def main():
    #Number 1:
    print("-"*50)
    print("Quiz 2 Number 1")
    myList = singlyLinkedList()
    print('Test list looks like:')
    myList.add_front(1)
    myList.add_front(2)
    myList.add_front(3)
    myList.add_front(4)
    myList.add_front(5)
    myList.printList()
    print('Second to last element looks like')
    myList.printSecondToLast()
    #Number 2:
    print()
    print("-"*50)
    print("Quiz 2 Number 2")
    #Create tree
    root = TreeNode("+")
    root.left = TreeNode("*")
    root.right = TreeNode("*")
    root.left.left = TreeNode("2")
    root.left.right = TreeNode("-")
    root.left.right.left = TreeNode("5")
    root.left.right.right = TreeNode("1")
    root.right.left = TreeNode("3")
    root.right.right = TreeNode("2")
    print("Tree in post order looks like:")
    root.printPostOrder()
    #Number 3:
    print()
    print("-"*50)
    print("Quiz 2 Number 3")
    inArray = [3, 1, 1, 3, 3, 5, 1, 5]
    print(minOccurenceNumber(inArray))
    
    
    
main()
    

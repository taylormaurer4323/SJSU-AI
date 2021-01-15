# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:11:42 2020

@author: taylo

Notes! Hashes, Maps, and something else I forgot!

"""

#This is kind of a generic tree structure, however I haven't come up 
#with a mechanism to decide when to create a new level
class Node:
    def __init__(self, data):
        self._children = []
        self._data = data
    
    
    def printTree(self):

        print(self._data)
        if self._children is not None:
            for child in self._children:
                child.printTree()
    def insert(self, data):
        self._children.append(Node(data))
                    
    def getData(self):
        return self._data
'''
print('Tree')
testTree = Node(10)
testTree.printTree()
print('Tree')
testTree.insert(11)
testTree.printTree()
print('Tree')
testTree.insert(12)
testTree.insert(13)
testTree.insert(14)
testTree.printTree()
'''

class NodeB:
    def __init__(self,data = None):
        self._left = None
        self._right = None
        self._data = data
    def insert(self, data):
        if self._data is not None:
            if self._left is None:
                self._left = NodeB(data)
            elif self._right is None:
                self._right = NodeB(data)
            elif not self._left.isFull():
                self._left.insert(data)
            elif not self._right.isFull():
                self._right.insert(data)
            else:
                self._left.insert(data)
        else:
            self._data = data
            
            
    def isFull(self):
        if self._left is None:
            return False
        if self._right is None:
            return False
        return True
    def addExp(self, stringExpArray):
        #stringExpArray needs to be array that seperates values by spaces
        #tringEXP shopuld be an array of sorts
        firstChar= stringExp[0]
        if len(stringExpArray) == 1:
            return stringExpArray[0]
        else:
            
            if firstChar == '(':
                self._left = NodeB()
                self._right = NodeB()
                self._left.addExp(stringExpArray(1:len(stringExpArray)))#????
                else:
            
                    if self._left._data = None:
                        self._left._data = self._left.addExp(stringExpArray(1:len(stringExpArray)))
                
            
    def printTreeInorder(self):
        #Note: this should be an example of inorder traversal
        if self._left is not None:
            self._left.printTreeInorder()
        print(self._data)
        if self._right is not None:
            self._right.printTreeInorder()
            
class Exp:
    def __init__(self, strExp):
        self._expTree = NodeB(strExp[0])
        for chars in strExp[1:len(strExp)]:
            self._expTree.insert(chars)
            
    def printExp(self):
        self._expTree.printTreeInorder()
            
            
myExpression = Exp('(2 x 1)')

myExpression.printExp()


'''First question of lab assignment asks to do inorder traversal
to print the expression. Then we evaluate the expression using post-order
traversal'''




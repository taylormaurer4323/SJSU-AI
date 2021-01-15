# -*- coding: utf-8 -*-
"""

@author: taylor maurer
lab 7
August 6th
"""


"""The below is for number 1 and 2"""

from copy import deepcopy
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
    def replace(self, replaceWhat, replaceWith):
        if self.is_empty():
            print("linked list empty")
            return -1
        found = False
        ptr = self._head
        
        while ptr is not None and found is False:
            if ptr._e == replaceWhat:
                ptr._e = replaceWith
                found = True
            else:
                ptr = ptr._next
        if found is False:
            self.add_front(replaceWith)
    
    def printFirstThirdFifth(self):
        if not self.is_empty():
            ptr = self._head
            for i in range(2):
                
                print(ptr._e,end="")
                if ptr._next is not None and ptr._next._next is not None:
                    print("->", end = "")
                    ptr = ptr._next._next
                else:
                    #break loop
                    i = 100
            #print final fifth one without the arrow
            if ptr._next is not None and ptr._next._next is not None:
                print(ptr._e)
            else:
                print()
    def printList(self):
        if not self.is_empty():
            ptr = self._head
            for i in range(self._size-1):
                print(ptr._e, end = "->")
                ptr = ptr._next
            print(ptr._e)
            
"""The below goes with number 3."""
class queueStack():
    def __init__(self):
        #implementing stacks using lists
        self._stack1 = []
        self._stack2 = []
        self._size = 0
        
    def enqueue(self, item):

        if self.is_empty():
            self._stack1.append(item)
            
            
        else:
            
            #erase stack2
            self._stack2 = []
            self._stack2.append(item)
            self._stack1 = self._stack2 + self._stack1

        self._size += 1
            
           
    def dequeuer(self):
        if self.is_empty():
            print("Queue is empty")
            return -1
        else:
            #assuming the add went correctly, all you need to do is pop an element
            #and decrease size
            self._size -= 1
            return self._stack1.pop()
            
    def is_empty(self):
        return self._size == 0
    def printQueue(self):
        
        if not self.is_empty():
            print("[",end = "")
            self._stack2 = deepcopy(self._stack1)
            for i in range(self._size-1):    
                print(self._stack2.pop(), end = ", ")
                
            
            print(self._stack2.pop(), end = "]\n")
            self._stack2 = []
            


def main():
    #Number 1:
    print("-"*50)
    print("LAB7 Number 1.")
    sL = singlyLinkedList()
    sL.add_front(100)
    sL.add_front(200)
    sL.add_front(300)
    sL.add_front(400)
    sL.add_front(500)
    print("My test list")
    sL.printList()
    sL.remove_first()
    sL.remove_first()
    print("Now after two removals list looks like:")
    sL.printList()
    print("Now using function, replace. Replacing 100 with 1000.")
    sL.replace(100, 1000)
    sL.printList()
    print("Now using function, replace. Replacing 1001 with 3.")
    sL.replace(1001, 3)
    sL.printList()
    
    #Number 2:
    print("-"*50)
    print("LAB7 Number 2.")
    #using same list from number 1, add elements:
    sL.add_front(600)
    sL.add_front(700)
    sL.add_front(900)
    sL.add_front(1000)
    print("List now looks like:")
    sL.printList()
    print("The first, third, and fifth elements are:")
    sL.printFirstThirdFifth()
    #remove elements to verify boundary conditions work
    sL.remove_first()
    sL.remove_first()
    sL.remove_first()
    sL.remove_first()
    print("Removed elements. Now list is:")
    sL.printList()
    print("First, thid and fifth elements are:")
    sL.printFirstThirdFifth()
        
    #Number 3:

    print("-"*50)
    print("LAB7 Number 3.")
    qS= queueStack()
    #add items to queue
    qS.enqueue(1)
    qS.enqueue(2)
    qS.enqueue(3)
    qS.enqueue(4)
    qS.enqueue(5)
    qS.enqueue(6)
    qS.enqueue(7)
    print("Queue looks like")
    qS.printQueue()
    print("Removing 3x items")
    qS.dequeuer()
    qS.dequeuer()
    qS.dequeuer()
    print("Now queue looks like")
    qS.printQueue()
    
main()
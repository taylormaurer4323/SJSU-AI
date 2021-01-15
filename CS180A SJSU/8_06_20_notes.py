# -*- coding: utf-8 -*-
"""
Created on Thu Aug 6 17:06:44 2020

@author: taylo
"""







"""
QUEUE
"""

class arrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__ (self):
        self._front = 0
        self._size = 0
        self._data = [None] * arrayQueue.DEFAULT_CAPACITY
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
        

    def first(self):
        if self.is_empty():
            raise('Queue is empty')
        return self._data[self._front]
    
    def deque(self):
        
        if self.is_empty():
            raise('queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size = self._size - 1
        return answer
    def enque(self, e):
        if self._size == len(self._data):
            #queue full
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size = self._size + 1
    
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0

""" Double ended queue, dequeue:
    """
    
""" Singly linked list"""
class sLink:
    class _Node:
        def __init__(self, element, nextNode = None):
            self._element = element
            self._nextNode = nextNode
        
        def getData(self):
            return self._element
        
        def getNext(self):
            return self._nextNode
        
        def setNext(self, newNext):
            self._nextNode = newNext
            
    def __init__(self):
        self._head = None
    def add_first(self, element):
        newNode = self._Node(element)
        #self.head is still pointing at previous first node
        newNode.nextNode = self.head
        self.head = newNode
        
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.element)
            current = current.nextNode
    def search(self, target):
        #current is reference that references self.head. This is a reference
        #in itself, that if items were added to the list references the first node
        #(see add_first)
        current = self.head
        while current is not None:
            if current.element == target:
                return True
            current = current.nextNode
        return False


print('DEQUEU------------')
#dequeue test:
from collections import deque
q = deque()
q.append(10) #default adds to right
print(q)
print("length: ", len(q))
q.appendleft(100)
q.appendleft(10)
print(q)
print("popped left",q.popleft())

    

    
    
#test your queue!
test = arrayQueue()

test.enque(5)
test.enque(5)
test.enque(5)
test.enque(5)
test.enque(5)
test.enque(5)
test.enque(5)
test.enque(5)
test.enque(5)
test.enque(5)
test.enque(5)
test.enque(5)
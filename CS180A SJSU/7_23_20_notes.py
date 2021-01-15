# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:40:49 2020

@author: taylo
"""


import array

def HW1test(n):
    
    runningSum = 0
    for i in range(1,2*n+1):
        #print(i)
        if i % 2 == 0:
            runningSum = runningSum + i
            
    return runningSum


def HW1soln(n):
    return n*(n+1)

def findLargestTen(sequence):
    #create empty sorted sequence
    sortedSequence= []
    #add first element of incomign sequence
    sortedSequence.append(sequence[0])
    
    #if length of incoming sequence is less than ten then all
    #that needs to be done is to return the incoming sequence
    #as those by definintion will be the largest ten elements
    if len(sequence) <= 10:
        return sequence
    else:
        sortLength = 10    
    
    #perform sorting of first 10 items
    for i in range(1,sortLength):
        j = 0
        #while sequence[i] is less than the sortedSequence[j]
        #we increment j. This will allow us to find the indices where
        #sequence[i] < sortedSequence[j] and 
        #sequence[i] > sortedSequence[j-1]
        while j < len(sequence) and sequence[i] < sortedSequence[j]:
            j = j+1
        #when we find the point where sequence[i] > sortedSequence[j]
        #insert the incoming sequence element, sequence[i] at this location
        #the insert operation will maintain the sorted nature of the list
        sortedSequence.insert(j,sequence[i])
    #go through the remaining items within the incoming sequence
    for i in range(sortLength,len(sequence)):    
        j = 0
        #as long as sequence[i] < sortedSequence[j], j continues to increase
        #again, this finds where the following is true:
        #sequence[i] < sortedSequence[j] and 
        #sequence[i] > sortedSequence[j-1]
        while j < 10 and sequence[i] < sortedSequence[j]:
            j = j+1
        #as long as j < 10, this means that we can pop off the last element
        #and add the new element. IF we didn't pop the last element the sorted
        #sequence would have more than 10 elements. 
        #By performing insert the list also stays sorted and allows the algorithm
        #to proceed.
        if j < 10:
            sortedSequence.pop(9)
            sortedSequence.insert(j, sequence[i])
    return sortedSequence

    










d = [1,2,3,4,5,3,6,3,8,100,4,2,6,4,44,76,55,34, 34, 1001, 54, 33, 2, 2, 33, 400, 54, 32, 678, 5434]

print("Test of algorithm")
print(d)
print(findLargestTen(d))



print("My answer:")
#HW1test(1)
print("Test:", HW1test(101))
print("Soln:", HW1soln(101))
    
    



myList = [1,5,4,3];
#Create a slice:
newList = myList[1:3]
#now the newlist cells reference the same items as mylsit does. Integers are immutable
#so changing the reference, within the new copied list. There won't be a change
#in the original list. Python takes care of ya!
myList[1] = 100
print()
print(newList)


#Compact array
#primes = array('i', [2,3,5,7,11,13,17])
#print(primes)



#multi d lists:
md = [[1,2,3],[4,5,6],[7,8,9]]
#now access like
print(md[1][1])

#Issue with multi-d lists:
data = [0]*5
print("data:", data)
data = [[0]*5]*3
print("data:", data)
#the follwoing changes element 1,2 to 5. However, all points within the list are 
#referecing the same list. We dont' have three different lists, we have one list
#of five zeros, and all five elements in each row point to the same list
data[1][2] = 5
print("data:", data)

#so what you do:
data = [[0] * 5 for j in range(5)]
print(data)
data[1][2]= 5
print("data:", data)


# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 19:46:24 2020

Taylor Maurer
Data Structures and Algorithms (Python)
"""
from random import randint

def main():
    #Function definitions are down below:
    
    #Number 1:
    print("-"*50)
    print("LAB2 Number 1.")
    reply = input("Enter a string to see all substrings: ")
    printAllSubstring(reply)

    #Number 2:
    print("-"*50)
    print("LAB2 Number 2.")
    reply = input("Enter a string. If it has leading white space it will be removed.\n")
    outString = removeLeadingSpaces(reply)
    print(outString)
    
    #Number 3
    print("-"*50)
    print("LAB2 Number 3.")
    print("Random Permutation from 1-10:")
    randomNumbers = randomPermutation()
    print(randomNumbers)
    
    
    
    
    
    
#The following is used for problem 1
def printAllSubstring(inString):
    for subStringLength in range(1,len(inString)+1):
        for i in range(0,len(inString)):
            if i+subStringLength <= len(inString):
                print(inString[i:i+subStringLength])

        
#The following is used for problem 2 (numbered as 1 on sheet though)
def removeLeadingSpaces(inString):
    
    leadingSpace = True
    stringIndex = 0
    outString = ""
    
    while leadingSpace == True:
        if stringIndex > len(inString):
            leadingSpace = False
        else:
            #if blank space is found don't add it to the output
            #if it is not found, then exit this loop and save the
            #string as outString from the current location (string
            #indexe) to the end of the input string
            if inString[stringIndex] != " ":
                outString = inString[stringIndex:]
                leadingSpace = False
            else:
                stringIndex = stringIndex + 1
        
    return outString
#The following is used for problem 3 (numbered as 2 though)
def randomPermutation():
    permutationList = []
    secondList = []
    
    #Define second list with values 1 through 10
    for i in range(0,10):
        secondList.append(i+1)
    
    for i in range(0,10):
        #Create random indexor from 0 to length of secondList
        randomIndexer = randint(0, len(secondList)-1)
        #Append to permutationList
        permutationList.append(secondList[randomIndexer])
        #remove the item that was added to permuation list
        secondList.pop(randomIndexer)
    
    return permutationList



main()
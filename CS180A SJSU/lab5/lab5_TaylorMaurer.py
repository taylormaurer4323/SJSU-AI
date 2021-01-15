# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:00:19 2020

Taylor Maurer
Data Structures and Algorithms (Python)
LAB5
"""
import time
#Goes with number 1
def minMax(inSequence):
    
    #len = 2 or 1 are the base cases
    if len(inSequence) == 2:
        #simply identify min and max and return (at end)
        if inSequence[0] > inSequence[1]:
            
            maximum = inSequence[0];
            minimum = inSequence[1];
        elif inSequence[0] < inSequence[1]:
            maximum = inSequence[1];
            minimum = inSequence[0];
        else:
            maximum = inSequence[0];
            minimum = inSequence[0];
    elif len(inSequence) == 1:
        #both are min and max
        maximum = inSequence[0];
        minimum = inSequence[0];
    else:    
        #split up the array and call recursion until you only have two elements
        #return the min and max from there. Then with the results of the recursion
        #compare those mins and maxes and return
        median = len(inSequence)//2 
        firstHalfResult = minMax(inSequence[0:median]);
        secondHalfResult = minMax(inSequence[median:len(inSequence)]);
        if firstHalfResult[0] < secondHalfResult[0]:
            minimum = firstHalfResult[0];
        else:
            minimum = secondHalfResult[0];
        if firstHalfResult[1] > secondHalfResult[1]:
            maximum = firstHalfResult[1];
        else:
            maximum = secondHalfResult[1];

    return minimum, maximum;
    
#Goes with number 2
def stringReverse(inputString):
    
    #base cases are len = 1 and 2
    if len(inputString) == 1:
        return inputString
    elif len(inputString) == 2:
        #return simple reverse
        return inputString[1] + inputString[0];
    else:
        #put first and last characters on the end and front (respectively)
        #of the recursion result
        return inputString[len(inputString)-1]+stringReverse(inputString[1:len(inputString)-1])+inputString[0]
    

def isPalindrome(inputString):
    
    #base cases are when len is 1 and 2
    if len(inputString) == 1:
        #len of 1 indicates a palindrome
        return True;
    elif len(inputString) ==2:
        #if len is 2, simply check that the two chars
        #equal each other
        if inputString[0] == inputString[1]:
            return True;
        else:
            return False;
    elif inputString[len(inputString)-1] == inputString[0]:
        #check that the characters we're looking at are indeed palindromes
        
        #call recursion, if at any point there's a false (in sub-recursions)
        #then return false. Otherwise, 
        if stringReverse(inputString[1:len(inputString)-1]):
            return True;
        else:
            return False;
    else:
        return False;
    




def main():
    #Number 1:
    print("-"*50)
    print("LAB5 Number 1.");
    A = [7, 10, 8, 3, 2, 4, 3, 5, 7, 2, 7, 9, 3, 2, 1, 6, 4, 2, 5, 7, 89, 10, 54, -1001];
    results = minMax(A)
    print("Minimum found:", results[0])
    print("Maximum found:", results[1])


    #Number 2:
    print("-"*50)
    print("LAB5 Number 2.")
    testWord = "pots&pans"
    reversedString = stringReverse(testWord)
    print("Word", testWord, "reversed is", reversedString)

                   

    #Number 3:
    print("-"*50)
    print("LAB5 Number 3.")
    word = "gohangasalamiimalasagnahog"
    if isPalindrome(word):
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")
 

main()


# -*- coding: utf-8 -*-
"""
Quiz #1
Taylor Maurer
"""
#Function for question 1
def productIsOdd(inSequence):
    for i in range(0, len(inSequence)-1):
        element1 = inSequence[i]
        for j in range(i, len(inSequence)-1):
            element2 = inSequence[j]
            tmpProduct = element1*element2
            if tmpProduct % 2 != 0:
                return True
    
    return False


#Function for question 2
def numberOfDigits(intNumber, divideByTenCount = 0):
    
    
    if intNumber/10 <= 1:
        return divideByTenCount + 1
    else:
        divideByTenCount = divideByTenCount + 1
        return numberOfDigits(intNumber/10, divideByTenCount)

def main():
    print("-"*50)
    print("Quiz1 Number 1.");
    sequence = [3,4,6,11]

    print("Sequence is: ", sequence)
    
   
    #Call function in if statement
    if productIsOdd(sequence):
        print("The sequence CONTAINS a distinct pair of numbers  who's product is odd")
    else:
        print("The sequence DOES NOT CONTAIN a distinct pair of numbers who's product is odd")




    print("-"*50)
    print("Quiz1 Number 2.");
    testInt = 123456789
    digitNum = numberOfDigits(123456789)
    
    print("number of digits in integer,",testInt,"is", digitNum)
    




main()



"""
Quiz1 Number 3:
Time Complexity:
    For the first question, the function in focus is productIsOdd.
    The time complexity is O(n^2) where n is the number of elements within the 
    sequence. This is due to the fact that there are two for loops. For each element
    within the sequence I loop through all elements within the sequence behind
    it. So if the sequence is 5, 3, 2, 4, then the first element is multiplied
    by 3, 2, and then 4. Then I jump to element 3, and it's multiplied by
    2 and 4, and then the outer for loop is on 2. At that point I multiply
    it by 4. 
    Although, the inner for loop iterations decreases with each iteration of the outer
    for loop. The upper bound is still O(n^2) as in the event n approaches infinity
    the inner for loop and outer for loop both are run approximately n times. 
    Thus O(n^2)
    
    
    
    
    
    For the second question, the function in focus is numberOfDigits. 
    The time complexity for this is O(n), where n is the number of digits 
    in the integer. This is because for each recursion I am dividing by ten
    and thus reducing the amount of digits in the integer by 1. So to finish
    the recursion I need to divide by ten for each digit in the integer, which is n.
    
    
    """
    
    
 
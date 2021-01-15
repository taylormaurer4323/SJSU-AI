# -*- coding: utf-8 -*-
"""
Notes for 6/25
"""

balance = 10000; #this we want to be a global variable
#Notes for 6/25
#LOOPS!
#Functions!
def cubeVolume(sideLength): #<- this is the header
    volume = sideLength ** 3; #** is exponent
    return volume;






def main():
    #while loop in python, interest rate calculator
    initialBalance = 10000; #dollars
    interestRate = 0.05; #percent
    yearValue = 0;
    
    balance = initialBalance;
    
    while balance < 20000:
        balance = balance * (1+interestRate);
        yearValue = yearValue + 1;
        
        
        
    print("Number of years to get to $20000 is", yearValue)
    
    
    #the for loop:
    # we can use this to loop over contents of any container
    stateName = "virgina";
    print("For loop version");
    for letter in stateName:
        print(letter);
    #A while loop alternative could be:
    i = 0
    print("While loop version: ")
    while i < len(stateName):
        letter = stateName[i];
        print(letter);
        i= i+1;
        
        
    #common function to use
    for i in range(1,30,10):
        print(i)
    #to do this with a while loop you'd need a counter variable. The important 
    #part here is the range function
        
        
        
    #counting numbers of uppercase letters in string
    uppercase = 0;
    string = "MyButts"
    for char in string:
        if char.isupper():
            uppercase = uppercase + 1;
    print("there are", uppercase, "uppercase letters in", string)
    
    
    #Now count vowels, this is utilizing the keyword 'in' learned in previous 
    #lecture
    vowels = 0;
    for char in string:
        if char.lower() in "aeiou":
            vowels = vowels + 1
    print("There are", vowels, "vowels in", string);
    
    
    #Random numbers and simulations...
    ## Starting with random numbers!
    from random import random
    myRandom = random();
    print("Pseudo-random number is", myRandom);
    #get a random int
    from random import randint
    print("Random number between 1 and 6:", randint(1,6))
    
    #NOTE the following means don't print to the next line (which is the default
    #of pythong):
    print("end", end="") 
    print("start")
    
    
    
    
    
    result1 = cubeVolume(2);
    print("After calling function cubeVolume the returned cube volume of cube with sides of 2 is", result1);
    print("Cube with side size of 10 has volume of", cubeVolume(10))


    boxString("Test");

    balance = 10000;
    withdraw(5000);
    #Note this doesn't really work, as something horrible is happening
    print("After withdrawing 5000 from 10000 balance is now", balance);
    
    
    """ Now we are going into lists: In Python this is actually similar
    to an array """
    #list of vals
    print()
    print("-"*50)
    print("CREATING LISTS")
    myFirstList = [1,2,3,4];
    #empty list:
    myFirstEmptyList = [];
    #to index
    print("First value of list:", myFirstList[0])
    myFirstList[0] = 100
    print("Now it's",myFirstList[0])
    stringList = "SJSU";
    
    
    for element in myFirstList:
        print(element, end = ", ")
    print();
    for i in range(len(myFirstList)):
        print(i,":", myFirstList[i]);
    
    
    listPtr1 = [5, 7, 8];
    #doing the following references both listPtrs to the same list (so this is
    #also said to be an alias for the list [5,7,8])
    listPtr2 = listPtr1;
    listPtr1[0] = 4;
    #both listPtrs change because they reference the same list
    print("listPtr1 has value", listPtr1[0], "at location 0")
    print("listPtr2 has value", listPtr2[0], "at location 0")
    #You can use negative indexing!
    print("listPtr1[-1]:", listPtr1[-1]);
    print("listPtr1[len(listPtr1)]:", listPtr1[-1]);
    
    #Appending an element:
    print("current list looks like")
    print(listPtr1)
    listPtr1.append("Butts");
    print("Now it looks like:")
    print(listPtr1)
    listPtr1.insert(2,"Are cool");
    print("After insert after location 2 it now looks like")
    print(listPtr1)
    buttIndex = listPtr1.index("Butts")
    print("Note: 'Butts' occurs at index", buttIndex)
    listPtr1.pop(4);
    print("We removed butts")
    print(listPtr1)
    
    
    #Creating a new list as a copy of another list
    listPtr2 = list(listPtr1);
    print("List 1:", listPtr1)
    print("list 2:", listPtr2)
    listPtr2.pop();
    print("Poped item from list 2:", listPtr2)
    print("And list 1:", listPtr1)
    #make same list
    listPtr = listPtr1;
    #Slice operator
    print("Items 2 up to 3 of list 1 are:", listPtr1[2:3])
    print("Items up to 3 of list 1 are:", listPtr1[:3])
    print("Items of 3 up to end of list are:",listPtr1[3:]);
    print("All items in list1 are:", listPtr1[:])
    #Creates new instantiation of list (not new reference)
    newList = listPtr1[2:4];
    
    #Tuple:
    triple = (5,10,9)
    tripl2 = 5 , 10, 8
    
    
    
    #Set:
    myFirstSet = {"Luigi", "Gumby", "Spiny"}
    print("SET:", myFirstSet)
    listToSet = set(listPtr)
    print("List to set:", listToSet)
    
    
    
    
    
    
    
#The following creates a box around the input variable
def boxString(contents):
    n = len(contents)
    print("-" * (n+2))
    print("|"+ contents + "|")
    print("-" * (n+2))
    #No return needed here


def withdraw(amount):\
    #Declare global value using the 'global' keyword. This gives you access to 
    #the variable in the calling function (main)
    global balance;
    if balance >= amount:
        balance = balance- amount;
        


#did a main type thing. Defining a main function and then calling as the following
#is common practice. This keeps the idea of "main"
main();


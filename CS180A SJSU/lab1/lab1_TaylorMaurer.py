# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:56:01 2020

@author: Taylor Maurer
"""


#Question #1
print("Lab 1, #1","-"*50)

integer1 = int(input("Enter first integer value then hit enter\n"))
integer2 = int(input("Enter second integer value then hit enter\n"))

print("The sum of",integer1, "and", integer2, "is", integer1+integer2)
print("The average of",integer1, "and", integer2, "is", (integer1+integer2)/2)
print("The distance of",integer1, "and", integer2, "is", abs(integer1+integer2))


#Question #2
print("Lab 1, #2","-"*50)
name = input("Enter a name\n")
print(name.upper())


#Question #3
print("Lab 1, #3","-"*50)
numberString = input("Enter three numbers seperated by commas\n")
#Assume user enters only three numbers
splitNumString = numberString.split(",")
num1 = float(splitNumString[0])
num2 = float(splitNumString[1])
num3 = float(splitNumString[2])


if num1 > num2 and num2 > num3:
    print('Decreasing')
elif num1 < num2 and num2 < num3:
    print('Increasing')
else:
    print('Neither')

#Question #4
print("Lab 1, #4","-"*50)  
numInput = int(input("Enter a positive integer that is less than 100000\n"))
numDigits = 0

if numInput < 10:
    print("Entered integer has 1 digit")
elif numInput < 100:
    print("Entered integer has 2 digits")
elif numInput < 1000:
    print("Entered integer has 3 digits")
elif numInput < 10000:
    print("Entered integer has 4 digits")
elif numInput < 100000:
    print("Entered integer has 5 digits")
else:
    print("You did not follow the instructions correctly")
    




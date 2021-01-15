# -*- coding: utf-8 -*-

from math import sqrt


"""
Program notes from first lecture 6/18 - Intro to Python 
"""

print("test")


#Operator:
"""
+, -, *, / are prety straight forward
// is integer division (which is interesting)
** performs exponentiation (which is also interesting)


"""


#type function gives you the type of a variable
floatVar = 42.385783921378458
print(type(floatVar))



#using print
print("This is a cool number", 100*8, "am I right?\n")

# For this chapter we'll use float, int, and strings
# Note: the type of value in python is not fixed (like it is in C++)
# this is how MATLAB works...
cansPerPack = 6
print("My variable type is", type(cansPerPack))
cansPerPack = cansPerPack * 3.14
print("Now my type is", type(cansPerPack))

#Arithmetic division:
print("Regular division when doing 7/2 gives", 7/2)
print("Integer division when doing 7/2 gives", 7//2)
print("Note this would be the same as doing floor(7/2) in other languages", (7/2))
print("modulous works as expected (7%2)", 7%2)


#module import
print("Squareroot test", sqrt(3))

#casting:
A = 4.56
B = int(A)
print("4.56 as an int is", B)    

#Strings:
print('The man said "Ah"')
print("The man went 'Ah'")
print("Who is the real"+"Harry Morgan")
#* is overloaded to mean repetiion
print("-"*50)
#this prints ---------------------------
#type cast!
print("My number to string", str(5))
#indexing
a = "Harry"
print("First letter of var a is", a[0])






#Excersise! Extract a string containing the middle character from a given string
string = "crates"
#Branching condition (even vs odd)
if len(string) % 2 == 0:
    #even - extract middle two
    position = len(string)//2
    result = string[position - 1] + string[position]
elif len(string > 1000):
    
    #odd - extract single
    position = len(string)//2
    result = string[position]
else:
    #odd - extract single
    position = len(string)//2
    result = string[position]
    
    
#Changed the above to show what else if is...
    
print("Middle chars of '", string, "' are", result)



#in operator
if "cra" in string:
    print("That's cra cra")
    
if "cray" not in string:
    print("that's not cra cra")
    
    
myfile = "butts.xml"

if myfile.endswith("xml"):
    print("This is an xml file - cool!")
    
    
randoString = "huighfghjabfyhdahtrrebtaz"
zINdex = randoString.find("z")
print("z occurs at index ", zINdex)
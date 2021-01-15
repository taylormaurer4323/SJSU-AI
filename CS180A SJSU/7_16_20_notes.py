# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:05:11 2020

@author: taylo
Notes from 7/16/2020 - lecture #5
"""

#Topics for today
#-finishing inheritance
#-Algorithm run-times
#-recursive algorithms




"""
INHERITANCE CONTINUED:
-always can use a subclass object in place of superclass object
-subclass inherits all methods that it doesn't overrid
-subclass can override a superclass
-class child(Parent):
-keyword 'super' allows to call superclass method or constructor
    """


"""
ALGORITHMS (Analysises)
"""
def find_max(data):
    #initial value to beat
    biggest = data[0]; #2 primitives, 1x for data access, and 1x for setting data
    #We call this c1 # of primitives
    
    
    #for each value:
    
    
    for val in data:#this loop runs through 'n' times
        #if it is greater than the best so far, then we know
        #we've found a new best
        if val > biggest: #primitive for comparison
            biggest = val; #primitive for two numbers
            #these are represented by c2 # of primitives
    #at loop end, biggest value is the max
    return biggest 

#runs in c1 + c2*n -> O(n)
""" Since the loop runs through the entire data array (n), with a constant
number of primitives being executed per each iteration. This will be O(n)
"""

"""
RECURSION
"""
def factorial(n):
    #this follows the piece wise function defined in lecture slides
    if n == 0:
        return 1;
    else:
        #this will then call factorial(n-1)
        return n * factorial(n-1);
    
#English ruler tick length type function:
#input: number of dashes to place at 1" mark
#output: program outputs a picture of a ruler that's consistent with
#as size of interval decreases by half, the tick length decreases by one
# drawTicks(length)
        
    """
def drawTicks(length):
    drawTicks(length - 1);
    #drawTick for given length:
    
    drawTicks(length - 1);

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1,1+num_inches):
        #Draws all minor points
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1);
        draw_line(center_length);
        draw_interval(center_length - 1);
"""






# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:06:44 2020

@author: taylo
"""


#LET'S LOOK AT OOP
## Note: _value is technically a member variable, however it is never explicitly 
#stated
class Counter:
    
    def getValue(self):
        return self._value
    
    def click(self):
        self._value = self._value + 1
    def reset(self):
        self._value= 0
        
      
class cashRegister:
    def __init__(self, defaultValue = 0):
        print("YOU CALLED THE REG. CONSTRUCTOR")
        print("Value is", defaultValue)
    def addItem(self, price):
        #METHOD BODY
        self._value = price
    def getItem(self):
        #Method body
        return self._value
class bankAccount:
    
    #This is static, meaning it belongs to all bankAccount objects.
    _lastAssignedNumber = 1000
    def __init__(self, initBalance = 0.0):
        self._balance = initBalance
        bankAccount._lastAssignedNumber= bankAccount._lastAssignedNumber+1
        self._accountNumber = bankAccount._lastAssignedNumber
        
    def deposit(self, depositAmount):
        self._balance = self._balance + depositAmount
        
    def getBalance(self):
        return self._balance
    def getNumber(self):
        return self._accountNumber
    
class Vehicle:
    def __init__(self, numberOfTires):
        self._numberOfTires = numberOfTires
    def getTires(self):
        return self._numberOfTires
    def printTireCount(self):
        print("Vehicle has", self._numberOfTires,"tires")
    
class Car(Vehicle):
    def __init__(self):
        #call superclass constructor, adds instance variable _numberOfTires
        super().__init__(4)
        self._plateNumber = "??????"
    def printTireCount(self):
        #Call the super class' version:
        print("SUPER CLASS VERSION:")
        super().printTireCount()
        #call the subclass' version:
        print("SUB CLASS VERSION:")
        print("Car has", self._numberOfTires,"tires")
        
        
#class fraction:
    #NOTE: we assume a negative number has numerator as negative. And positive
    # number has no negatives in the expression. Also we assume the fraction
    # will be stored in the most reduced form (eg. 1/4 is stored if 4/16 is
    #entered )
    #def __init__(self, numerator = 0, denominator = 1):
    #    self._numerator = numerator
        
    #    if denominator == 0:
    #        raise ZeroDivisionError("denominator cannot be zero")
    #    if numerator == 0:
    # to be continued one day far off in the future...       
    
    #Overloading the == operator
    #def __eq__(self, rhsValue):
    #    return(self._numerator == rhsValue.numerator and self._deonminator == rhsValue.denominator)       
        
        
def main():
    #create object
    tally = Counter()
    #reset
    tally.reset()
    tally.click()
    tally.click()
    
    
    result = tally.getValue()
    print("Value: ", result)
    tally.click()
    result= tally.getValue()
    print("Value:", result)
    
    register1 = cashRegister()
    
    print("-"*50)
    print("STATIC VAR/CLASS VAR EXAMPLE")
    myAccount = bankAccount()
    myAccount.deposit(100023)
    print("Balance of account:", myAccount.getBalance())
    print("Account number:", myAccount.getNumber())
    newAccount = bankAccount()
    print("New account's number:", newAccount.getNumber())
    
    
    #NewnewAccount will reference the same object...
    newNewAccount = myAccount;
    print("newnewAccount balance:", newNewAccount.getBalance())
    
    #Note: upon re-assigning reg1, the first object created is garbage 
    #collected or deleted from memory
    reg1 = cashRegister()
    reg1 = cashRegister()
    
    
    print("-"*50)
    print("INHERITANCE")
    myCar = Car()
    print("My car has", myCar.getTires(),"wheels")
    myCar.printTireCount()
    
    
#Call main
main()
    
    


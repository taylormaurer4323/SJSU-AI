# -*- coding: utf-8 -*-
"""
Python code to go with midterm submittal.
Taylor Maurer
7/30/2020

"""


#number 3:
def numberOfDivideByTwos(inputInteger, divideByTwoCount = 0):

    if inputInteger//2 < 2:
        return divideByTwoCount + 1
    else:
        divideByTwoCount = divideByTwoCount + 1
        return numberOfDivideByTwos(inputInteger//2, divideByTwoCount)
#number 4
def addSparseArray(dArray1, dArray2):
    #empty dictionary
    summedArray = {}
    
    #check if there are any similar indices between 
    #the two arrays
    for key in dArray1:
        arrayValue1 = dArray1.get(key)
        if key in dArray2:
            arrayValue2 = dArray2.get(key)
            summedArray[key] = arrayValue2 + arrayValue1
        else:
            arrayValue1
            summedArray[key] = arrayValue1
    #now check if any elements within dArray2 haven't been added to the output
    #array yet
    for key in dArray2:
        if key not in summedArray:
            arrayValue2 = dArray2.get(key)
            summedArray[key] = arrayValue2
    return summedArray


#number 5:
class person:
    def __init__(self, name = 'na', birthYear = 1900):
        self._name = name
        self._birthYear = birthYear
    
    def getName(self):
        return self._name
    def getBirthYear(self):
        return self._birthYear
    def setName(self, name):
        self._name = name
    def setBirthYear(self, birthYear):
        self._birthYear = birthYear

class student(person):
    def __init__(self, major = 'na', name = 'na', birthYear = 1900):
        super().__init__(name, birthYear)
        self._major = major
    
    def getMajor(self):
        return self._major
    def setMajor(self, major):
        self._major = major

class instructor(person):
    def __init__(self, salary = 0, name = 'na', birthYear = 1900):
        super().__init__(name, birthYear)
        self._salary = salary
    
    def getSalary(self):
        return self._salary
    def setSalary(self, salary):
        self._salary= salary

def main():
    
    #number 3:
    print("Number 3", "-"*50)
    print("9 can be divided by 2,", numberOfDivideByTwos(9), "times")
    print("50 can be divided by 2,", numberOfDivideByTwos(50), "times")
    print("1024 can be divided by 2,", numberOfDivideByTwos(1024), "times")
    
    #number 4:
    print("\nNumber 4","-"*50)
    dictA = {5:4, 9:2, 10:7}
    dictB = {2:3, 5:1, 10:6, 20:8}
    print("Dictionary A:", dictA)
    print("Dictionary B:", dictB)
    print("Dictionary A and B added togehter (as if representing sparse arrays)")
    print(addSparseArray(dictA, dictB))
    
    #number 5:
    print("\nNumber 5","-"*50)
    print("Person Example")
    myPerson = person('Taylor')
    myPerson.setBirthYear(1992)
    print(myPerson.getName(), ":", myPerson.getBirthYear())
    
    print("\nStudent Example")
    myStudent = student()
    myStudent.setName("Taylor")
    myStudent.setMajor("Biology")
    myStudent.setBirthYear(1992)
    print("Student", myStudent.getName(),"has birth year of", myStudent.getBirthYear())
    print("and major of", myStudent.getMajor())
    
    print("\nInstructor Example")
    myIn = instructor(100000, "Prof. Taylor", 1992)
    print(myIn.getName(), "makes", myIn.getSalary(), "dollars")
    print("and was born in", myIn.getBirthYear())
    
main()
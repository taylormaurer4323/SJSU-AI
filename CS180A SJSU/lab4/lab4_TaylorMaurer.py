# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:05:50 2020

Taylor Maurer
Data Structures and Algorithms (Python)
LAB4
"""
import math
from random import randint

#For number 1
class SodaCan:
    def __init__(self, inputHeight = 1, inputRadius = 1):
        self._height = inputHeight
        self._radius = inputRadius

    def getSurfaceArea(self):
        return 2 * math.pi * self._radius*self._height + 2 * math.pi * (self._radius**2)
    
    
    def getVolume(self):
        return math.pi * (self._radius**2) * self._height
    def getRadius(self):
        return self._radius
    def getHeight(self):
        return self._height



#For number 2:
class Student:
    def __init__(self, studentName):
        self._studentName = studentName
        self._quizzesTaken = 0
        self._totalQuizScore = 0
    def getName(self):
        return self._studentName
    def getTotalScore(self):
        return self._totalQuizScore
    def getNumberOfQuizzes(self):
        return self._quizzesTaken
    def getAverageScore(self):
        return self._totalQuizScore/self._quizzesTaken
    def addQuiz(self, score):
        self._totalQuizScore = self._totalQuizScore + score
        self._quizzesTaken = self._quizzesTaken + 1
        
#For number 3:
class VotingMachine:
    def __init__(self):
        self.clearMachineState()
        
    
    def clearMachineState(self):
        self._rVotes = 0
        self._dVotes = 0
        
        
    def voteRepublican(self):
        self._rVotes = self._rVotes + 1
    def voteDemocrat(self):
        self._dVotes = self._dVotes + 1
        
    def getTotalTally(self):
        return self._dVotes + self._rVotes
    def getRepublicanVotes(self):
        return self._rVotes
    def getDemocratVotes(self):
        return self._dVotes
    

def main():
    #Number 1:
    print("-"*50)
    print("LAB4 Number 1.")
    print
    mySodaCan = SodaCan(10, 15)
    print("For soda can of height", mySodaCan.getHeight(),"and radius of", mySodaCan.getRadius())
    print("Soda Can surface area:", mySodaCan.getSurfaceArea())
    print("Soda Can Volume:", mySodaCan.getVolume())

    #Number 2:
    print("-"*50)
    print("LAB4 Number 2.")
    myself = Student("Taylor")
    myself.addQuiz(98)
    myself.addQuiz(88)
    myself.addQuiz(75)
    myself.addQuiz(99)
    myself.addQuiz(82)
    myself.addQuiz(85)
    print(myself.getName(),"has taken", myself.getNumberOfQuizzes())
    print("with a total score of", myself.getTotalScore())
    print("and an average of", myself.getAverageScore())
                   

    #Number 3:
    print("-"*50)
    print("LAB4 Number 3.")
    vM1 = VotingMachine()
    for i in range(0,500):
        randomNumber = randint(0,1)
        if randomNumber == 1:
            vM1.voteDemocrat()
        else:
            vM1.voteRepublican()
            
            
    if vM1.getDemocratVotes() > vM1.getRepublicanVotes():
        winner = "Democrats"
        loser = "Republicans"
        winningVotes = vM1.getDemocratVotes()
        losingVotes = vM1.getRepublicanVotes()
    elif vM1.getDemocratVotes() == vM1.getRepublicanVotes():
        winner = "TIE"
    else:
        winner = "Republicans"
        loser = "Democrats"
        winningVotes = vM1.getRepublicanVotes()
        losingVotes = vM1.getDemocratVotes()
    if winner != "TIE":
        print("After", vM1.getTotalTally(),"votes. The", winner, "won with", winningVotes)
        print("votes, while the", loser, "had", losingVotes, "votes")
    else:
        print("After", vM1.getTotalTally(),"votes. There was a tie.")
        print("Republicans had", vM1.getRepublicanVotes())
        print("Democrats had", vM1.getDemocratVotes())

main()


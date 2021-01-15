# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 20:23:48 2020

@author: taylo
"""

class matrix:
    def __init__(self, rows = 1, columns= 1, incomingList = [0]):
        #instantiate matrixList representation of matirx
        self._matrixList = [[0]*columns for j in range(rows)]
        self._rows = rows
        self._cols = columns
        
        
        if self._rows > 1 or self._cols > 1:
            #allow using a list to instantiate matrix
            for i in range(self._rows):
                for j in range(self._cols):
                    self._matrixList[i][j] = incomingList[i][j]
        else:
            #if small, then just make single element 1
            self._matrixList[0][0] = incomingList[0]
            
                
    #override bracket operators using tuple
    def __getitem__(self, index):
        rI = index[0]
        cI = index[1]
        return self._matrixList[rI][cI]
    def __setitem__(self, index, value ):
        self._matrixList[index[0]][index[1]] = value
        
    #print utility function
    def printMat(self):
        for i in range(self._rows):
            print("[", end = "")
            for j in range(self._cols):
                
                if j < self._cols-1:
                    print(self._matrixList[i][j], end = ",")
                else:
                    print(self._matrixList[i][j], end = "")
            print("]")
    def __add__(self, B):
        rowsB = B.getRows()
        colsB = B.getCols()

        resultMat = [[0] * colsB for j in range(self._rows)]
        
        #add along similar dimensions
        if self._rows == rowsB and self._cols == colsB:
            for r in range(self._rows):
                for c in range(colsB):
                    resultMat[r][c] = self._matrixList[r][c] + B[r,c]
                    
            mat = matrix(self._rows, colsB, resultMat)

            return mat
            
        else:
            print("incorrect dimensions. Need equal rows and columns b/t two matrices")
            return -1
        
        
    def __mul__(self, B):
        rowsB = B.getRows()
        colsB = B.getCols()
        resultMat = [[0] * colsB for j in range(self._rows)]

        if self._cols != rowsB:
            print("Error. Columns of 1st matrix needs to equal rows of 2nd matrix.")
            return -1
        else:
            #perform multiplication going through rows and columns of A, and lastly
            #switching colsumns of B
            for colsBI in range(0, colsB):
                for rowsAI in range(0,self._rows):
                    for colsAI in range(0,self._cols):  
                        #colsA = rowsB also
                        resultMat[rowsAI][colsBI] = resultMat[rowsAI][colsBI] + self._matrixList[rowsAI][colsAI] * B[colsAI,colsBI]
        
        mat = matrix(self._rows, colsB, resultMat)
        return mat
        
    def getRows(self):
        return self._rows
    def getCols(self):
        return self._cols



def palindromeTestStack(inString):
    #stack will be empty list
    stack = []
    #only go half way
    for i in range(0,len(inString)//2):
        stack.append(inString[i])
        
    #if we have an odd length string then middle character does not factor
    #into the palindrome. Thus we skip if odd.
    if len(inString) % 2 == 0:
        startIndex = len(inString)//2
    else:
        startIndex = len(inString)//2+1
    
    #now traverse second half
    for i in range(startIndex, len(inString)):
        lastAdded = stack.pop()
        if lastAdded != inString[i]:
            #not palindrome
            return False
        else:
            return True
    
    
    
    
    
    
                

def main():
    #Number 1:
    print("-"*50)
    print("LAB6 Number 1.")
    #define two matrices:
    A =  [[4,5],[3,4],[2,1],[4,5]]
    B = [[6,7],[8,9],[10,11],[12,13]]
    #matrixMult(A,B)
    
    #print("Matrix add: ", matrixAdd(A,B))
    
    matA = matrix(4,2, A)
    matB = matrix(4,2, B)
    
    matC = matA + matB
    print("Added matrix A: ")
    matA.printMat()
    print("to matrix B:")
    matB.printMat()
    print("And we get:")
    matC.printMat()
    
    D = [[1,2,4],[3,4,5]]
    matD = matrix(2,3,D)
    print("Multiplied matrix C:")
    matC.printMat()
    print("By matrix D:")
    matD.printMat()
    print("And we get:")
    matE = matC * matD
    matE.printMat()
    
    
    #Number 2:
    print("-"*50)
    print("LAB6 Number 2.")
    teststring = "abcdeffedcba"
    result  = palindromeTestStack(teststring)
    if result:
        print(teststring,"is a palindrome")
    else:
        print(teststring, "is not a palindrome")
    
    
    
main()
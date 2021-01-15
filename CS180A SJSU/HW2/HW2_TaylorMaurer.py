'''
HW 2 - Taylor Maurer
8/18/2020
'''

import operator
#For number 1
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        self.operatorTable = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
        }
        
    #1a:
    def printExpression(self):
        if self.left is not None:
            print('(', end='')
            self.left.printExpression()
        print(self.val, end = '')
        if self.right is not None:
            self.right.printExpression()
            print(')', end='')
    #1b:
    def evalExpression(self):
        #check if leaf
        if self.left is None and self.right is None:
            return self.val
        else:
            leftVal = self.left.evalExpression()
            rightVal = self.right.evalExpression()
            operator = self.val
            return self.operatorTable[operator](int(leftVal), int(rightVal))

def singleAppearance(inArray):
    #define empty set:
    myDict = {}
    #on first pass count the number of occurences of each number
    for i, item in enumerate(inArray):
        myDict[item] = myDict.get(item, 0) + 1#zero is default
    #on second pass find the number that's only seen once
    for dictItem in myDict:
        if myDict[dictItem] == 1:
            return dictItem

def number3Function(inArray,k):
    myDict = {}
    
    
    for i, item in enumerate(inArray):

        if item in myDict:
            tempDiff = i - myDict[item]
            if tempDiff <= k:
                return True
            else:
                myDict[item] = i
        else:
            myDict[item] = i
    return False

def main():
    print("-"*50)
    print("HW2 Number 1.")
    #The code from class:
    root = TreeNode("+")
    root.left = TreeNode("*")
    root.right = TreeNode("*")
    root.left.left = TreeNode("2")
    root.left.right = TreeNode("-")
    root.left.right.left = TreeNode("5")
    root.left.right.right = TreeNode("1")
    root.right.left = TreeNode("3")
    root.right.right = TreeNode("2")
    print("Printing and evaluating expression:")
    root.printExpression()
    print(" =", root.evalExpression())
    
    
    print("-"*50)
    print("HW2 Number 2.")
    testArray =  [4,1,2,1,2]
    print("For array of:", testArray)
    print("The number ", singleAppearance(testArray), "is seen once.")
    
    
    print("-"*50)
    print("HW2 Number 3.")   
    testArray = [1,2,3,1]
    k = 3
    print("For array:", testArray, "and k of", k)
    print("The function returns", number3Function(testArray, k))
    testArray = [1,2,3,1, 0, 4]
    k = 2
    print("For array:", testArray, "and k of", k)
    print("The function returns", number3Function(testArray, k))
    testArray = [1,0,1,1]
    k = 1
    print("For array:", testArray, "and k of", k)
    print("The function returns", number3Function(testArray, k))
    testArray = [1,2,3,1,2,3]
    k = 2
    print("For array:", testArray, "and k of", k)
    print("The function returns", number3Function(testArray, k))
    
    
    
    
    
main()
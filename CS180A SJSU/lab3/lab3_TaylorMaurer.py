# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:05:50 2020

Taylor Maurer
Data Structures and Algorithms (Python)
"""




#Number 1:
print("-"*50)
print("LAB3 Number 1.")
string1 = input("Enter string 1\n")
string2 = input("Enter string 2\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"
#Bring both to lower case for easier compare. (Assuming lower case numbers 
#equal upper case numbers)
string1 = string1.lower()
string2 = string2.lower()


#turn into character sets
stringSet1 = set(string1)
stringSet2 = set(string2)
alphabetSet = set(alphabet)
#Doesn't matter on order, find intersection
intersectionSet = stringSet1.intersection(stringSet2)
#find difference to first set:
firstSetDiff = stringSet1.difference(stringSet2)
secondSetDiff = stringSet2.difference(stringSet1)


totalSet = stringSet1.union(stringSet2)
neitherLetters = alphabetSet.difference(totalSet)
print("Characters that occur in both string:", intersectionSet)
print("Characters that only occur in first string entered", firstSetDiff) #difference
print("Characters that only occur in second string entered:", secondSetDiff) #difference
print("Letters that occur in neither set:", neitherLetters)
#use sets



#Number 2:
print("-"*50)
print("LAB3 Number 2.")

#read through bad word file to identify bad words. Assume bad words are seperated
#on each line of the bad words file
badWordFile = "bad_words.txt"
badWordFileObj = open(badWordFile, "r")
badWordSet = set()
for line in badWordFileObj:
    #strip any newlines, whitespace, etc. (assuming
    #no crazy characters). Also bring everything to lower case.
    #Then add to set
    badWordSet.add(line.strip().lower())
badWordFileObj.close()


#Go through arbitrary text file
textFile = "arbitrary_text_file.txt"
textFileObj= open(textFile, "r")
#While writing to a new file
outFile = "output_file_clean.txt"
outputFileObj = open(outFile, "w")

for line in textFileObj:
    #split out line into individiual words
    currentLine = line.split()
    cleanLine = line
    
    #Go through each word
    for word in currentLine:
        currentWord = word.strip(":;,.!? -")
        currentWord = currentWord.lower()      
        if currentWord in badWordSet:
            #If bad word found replace it within the line and continue to check
            cleanLine = cleanLine.replace(word, "*"*len(currentWord))
    outputFileObj.write(cleanLine)
        

outputFileObj.close()
textFileObj.close()
print("See file in current directory:", outFile)


#Number 3:
print("-"*50)
print("LAB3 Number 3.")

inFile = open("indexing_file.txt", "r")
indexDict = {}
lineCount = 1
for line in inFile:
    #split into words and go through those
    currentLine = line.split()
    for word in currentLine:
        #Remove all nonsense, and make lower case
        currentWord = word.strip(":;,.!? -")
        currentWord = currentWord.lower()
        #Check if currentWord is in the dictionary:
        if currentWord in indexDict:
            #Check if word is not already indexed on line
            if lineCount not in indexDict[currentWord]:
                #Now add it to the dictionary:
                indexDict[currentWord].append(lineCount)
        else:
            #If word is not in dictionary add it and the
            #the current line number
            indexDict[currentWord] = [lineCount]
        
    lineCount = lineCount + 1

inFile.close()

#Print out indexed dictionary:
print("Index: ")
print(indexDict)
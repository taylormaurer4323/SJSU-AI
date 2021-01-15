# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:07:09 2020

@author: taylo

Sets and dictionaries continued...
"""




#Reading and writing text files
#to access file it must first be opened
#Causes error - infile = open("nonexistent.txt", "r");


#open for reading (note write is "w")
infile = open("6_25_20_notes.py", "r")
outputString = infile.readline();

print("First line of file is: ")
print(outputString);
print("second line of file is: ")
outputString = infile.readline();
print(outputString)
while outputString != "":
    outputString = infile.readline();
    print(outputString, end = "");

#Or you can do the following
print("DIFFERENT WAY:")
infile.close()
infile = open("6_25_20_notes.py", "r")
outputString = infile.readline();
for line in infile:
    
    print(outputString, end = "");
    outputString = infile.readline();
#must be done at the end:




#To write:
outfile = open("example.txt", "w");
#Need to explicitly put \n
outfile.write("Hello Dick!\n");
outfile.close();

#Make sure write worked
infile = open("example.txt");
line = infile.readline();
print(line);





#processing on lines
#There's lstrip, rstrip, and strip to remove special chars and whitespace
#from left, right, or both sides of input string

infile = open("6_25_20_notes.py", "r")

for line in infile:
    #remove newline
    line = line.rstrip();
    #Split into wordlist
    wordList = line.split();
    for word in wordList:
        #remove special chars
        word = word.rstrip(".,?!")
        print(word)
#Note, we will need file writing and file opening for lab. We will
#Also use dictionaries in combo with file reading
#SETS AND DICTIONARIES!!!!!!
print("-"*50)
print("NOW WE ARE TALKING SETS AND DICTIONARIES")
print("-"*50)
createdSet = {"test", "butts", "100"}
print("created Set: ", createdSet)
listy = ["test", "butts", "buttman", "test", 100];


castedSet = set(listy);

print("Casted Set: ", castedSet)
print("It has length of", len(castedSet),"items" )

print("individual items:")
for setItems in castedSet:
    print("-",setItems);
    
    
#Sort the set, (Note doesn't work because how do you sort 100 with words)
#sortedList = sorted(castedSet);
#print("Sorted set (now list) is: ", sortedList)
sortedList = sorted(createdSet);
print("Sorted created list is:", sortedList)   

#To add items
createdSet.add("Buttman")
print("Added item to list now looks like:", createdSet)
#To remove items
itemToRemove = "100";
createdSet.discard(itemToRemove);
print("Now we've removed '100':", createdSet)
#No error seen after we've already removed this
createdSet.discard(itemToRemove);
#Will be an error if remove is used:
#createdSet.remove(itemToRemove);


#Dictionaries:
print("-"*50)
print("DICTIONARIES")
print("-"*50)
aDict = {"Romeo": "Green", "Adam": "Red"}
print("Dictionary looks like:", aDict)
#People example:
contacts = {"fred":7235591, "Mary": 384234, "Bob": 3842343, "Sarah":2213278}
print("Contacts dictionary looks like:", contacts)

#Duplicate:
oldContacts = dict(contacts)
print("Duplicated dictionary:", oldContacts)
#Indexing dictionary via key
print("Fred's phone number is", contacts["fred"])
#Check if member:
if "Taylor" in contacts:
    print("Taylors number is", contacts["Taylor"])
else:
    print("No key for Taylor")
    
#Demo of the get method:
number = contacts.get("Taylor", 411)
print("Dial "+ str(number))
number = contacts.get("fred", 411)
print("Dial", number)


myName="Taylor";
contacts[myName] = 7202715607;
print("Now contacts is", contacts)


#Empty dict:
emptyDict = {}
print("empty dict", emptyDict)
emptyDict["Height"] = 6 * 12
print("Non empty dict:", emptyDict)

#So now remove my name off contacts list
myNumber = contacts.pop(myName)
print("With my name off:", contacts, end = "")
#If ran again (see below) you get a keyError as "Taylor" is no longer on the 
#Dictionary
#contacts.pop(myName)
print(", however my number is", myNumber)
#Traversal
print("\nMy contacts:")
for elements in contacts:
    print(elements,":",contacts[elements])
#Key doesn't have to be string
contacts[1] = 5
print(contacts)
contacts.pop(1)

#sorted sorts the keys and returns a list instead of a dict5
sortedDict = sorted(contacts)
print("Sorted dict:", sortedDict)

#Complex dictionaries and sets:
print("\nDictionary of sets...")
#Dictionary of sets
#Make an index (as in a book), the terms come from a text file:
entries= {}
#Key value 1 gets a set
entries["python"] = {7, 11}
entries["SJSU"] = {20}
entries["example"] = {5, 50}
print("Dictionary of sets looks like:", entries)
#Creates empty set
entries["C++"] = set()
#Now add some things to the page number set associated w/C++ key
entries["C++"].add(100)
entries["C++"].add(101)
print("Dictionary of sets now looks like:", entries)



#Now we're looking at dictionary of lists:
entries["python"] = [5,3,7]
entries["SJSU"] = [4]
entries["example"] = [6,2]
print("Entries, the dictionary of list is now:", entries)

#Create blank list for C++ key
entries["C++"] = []
entries["C++"].append(8)
#LIST DOESN'T USE ADD, IT USES APPEND
entries["C++"].append(9)
print("Entries, the dictionary has C++ items:", entries)
#Create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Sets can contain different data types
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False and 0 is considered the same value
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Get the number of items in a set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#String, int and boolean data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#What is the data type of a set
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Using the set() constructor to make a set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
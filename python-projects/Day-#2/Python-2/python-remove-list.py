# Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Output: ['apple', 'cherry']
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Output: ['apple', 'cherry', 'banana', 'kiwi']
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Output: ['apple', 'cherry']
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Output: ['apple', 'banana']
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
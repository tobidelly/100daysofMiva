# Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# One item tuple, remember the comma
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# String, int and boolean data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

Using the tuple() method to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
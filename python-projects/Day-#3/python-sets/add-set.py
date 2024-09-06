#Add item to a set using add() method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add multiple items to a set using update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add any iterable to a set using update() method
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
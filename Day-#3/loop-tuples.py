#Iterate through items and print values
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
#Print all items by referring to their index number  
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
#using a while loop to go through all the index numbers
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 
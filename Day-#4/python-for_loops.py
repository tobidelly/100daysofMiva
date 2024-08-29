#Print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Print each letter in the word "banana"
for x in "banana":
  print(x)
 
#Exit the loop when x is "banana" 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Do not print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Using the range() function
for x in range(6):
  print(x)

#Using the start parameter
for x in range(2, 6):
  print(x)
  
#Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
  print(x)
  
#Else in For Loop
for x in range(6):
  print(x)
else:
    print("Finally finished!")

#Break the loop when x is 3, and see what happens with the else block
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
#Print each adjective for every fruit
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# having an empty for loop like this, would raise an error without the pass statement
for x in [0, 1, 2]:
  pass

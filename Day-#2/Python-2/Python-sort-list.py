# Sort list in alphabetical order:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort list in descending order:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Sort list numerically in descending order:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Sort the list based on how close the number is to 50:
def myfunc(n):
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case-insensitive sort:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
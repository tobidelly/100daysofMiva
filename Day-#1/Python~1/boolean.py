# Python - Boolean
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
# Evaluate Values and Variables  
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

# Example
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
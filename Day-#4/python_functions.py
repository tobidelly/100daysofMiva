#defining function with def keyword
def my_function():
  print("Hello from a function")
  
#calling function
def my_function():
    print("Hello from a function")
my_function()

#Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#This function expects 2 arguments, and gets 2 arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#If the number of arguments is unknown, add a * before the parameter name
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#To let a function return a value, use the return statement
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# having an empty function definition like this, would raise an error without the pass statement
def myfunction():
  pass

#Positional-Only Arguments
def my_function(x, /):
  print(x)

my_function(3)

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments
def my_function(x):
  print(x)

my_function(x = 3)

#Keyword-Only Arguments
def my_function(*, x):
  print(x)

my_function(x = 3)


#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments
def my_function(x):
  print(x)

my_function(3)

#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
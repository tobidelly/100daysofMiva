#Create an array containing car names
cars = ["Ford", "Volvo", "BMW"]
#Get the value of the first array item
cars[0] = "Toyota"
#Return the number of elements in the cars array
x = len(cars)
#Print each item in the cars array
for x in cars:
  print(x)
#Add one more element to the cars array
cars.append("Honda")
#Delete the second element of the cars array
cars.pop(1)
#Delete the element that has the value "Volvo"
cars.remove("Volvo")

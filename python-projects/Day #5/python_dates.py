# Import the datetime module and display the current date
import datetime

x = datetime.datetime.now()
print(x)

# Return the year and name of weekday
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Create a date object
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# Display the name of the month
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
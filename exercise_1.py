import math #import math library to use math methods
###Functions
# Functions and methods provide useful tools
# For words (i.e. strings): Capitalize every letter or get the number of letters
# For numbers (integers, floats): Create the absolute number. selected the larger of 2 numbers
# Get input or print output
print('a value') # print is a function
input('ask for a value') # input is also a function
# <name>() is usually a function
# => This is how we call a function
# inside the () is argument 
# ex: function_name(argument)


###Methods -> functions of datatypes
print('value'.capitalize())
print('value'.replace('e', '3'))

# Test
# Create a Pythagoras theorem calculator
input_width = int(input('Enter width of triangle: '))
input_height = int(input("Enter height of triangle: "))

pythagoras_result = math.sqrt((math.pow(input_width, 2)) + (math.pow(input_height, 2)))
print(f"This is your hypotenuse result: {pythagoras_result}")

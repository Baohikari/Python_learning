# This is a comment
# Execution order (up-down)
print("Test")
print("Test2")

#datatypes
print("Words") #string
print(123) #int
print(-10) 
print(1.5) # float

#operations
print(3 + 3)
print(3 - 3)
print(3 * 3)
print(3 / 3)
print(10 * "Hello")

#variables
# #Mandatory
#only letters A-z & 0-9 + _
#cannot start with a number
#case sensitive (test123 is different from Test123)
#Cannot use names ò inbuit functions (print)
# #Beneficial
#Be clear with a variable names
#Use snake_case
greeting_phase = "Hello"
print(greeting_phase)

#input
user_input = input("Please write something: ")
print(user_input)

###Test1

user_input_name = input("What's your name?: ")
print(f"Hello {user_input_name}, have a nice day")
#or you can use this
# print("Hello", user_input_name, ", have a nice day")


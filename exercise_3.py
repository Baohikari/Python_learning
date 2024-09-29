###Control Flow
# Only run code if a value is True
# Repeat (i.e. loop) code as long as a condition is True
# Run code for every entry in a container

##Boolean values
# Can only be True or False
# Comparison operators: ==, <, <=
# Truthy, Falsy: Automatic conversion to Boolean
# Empty container, string without letters and 0 are False. Everything else is Truthy


#if statement
if 3 > 4:
    print('correct result')
elif 2 > 1 and 5 > 1:
    print('some other result')
    if len([1, 2, 3]) > 2:
        print('list is long enough')
else:
    print('incorrect result')


#while loop
counter = 0
while counter < 10:
    print(counter)
    counter += 1
    if counter == 5:
        print("counter is 5 here")
print('while loop has finished')

#for loop
test_dictionary = {1:2, 3:4, 5:6}
test_set = {1, 2, 3, 3}
test_list = [1, 2, 3, 4, 5]
for k, v in test_dictionary.items(): #More than one variable here to solve some problems
    print(k)
    print(v)
#for dictionary, it will print only the key use methods of dictionary


#truthy and falsy
if 0:  #0 is false, code is not executed, same as empty container and string without letters
    print('something')

#Functions: any(), all()


#Test
#Create a list = (1, 2, 3, 4, 5) and run code for every item
#If the value is 2 print "the value is 2"
#If it isn't print "the value is not 2"
#If the value is 5 run a while loop to print 'last items' 6 times

practice_list = [1, 2, 3, 4, 5]
for x in practice_list:
    if x == 2:
        print('The value is 2')
    else:
        print('The value is not 2')
        if x == 5:
            counter = 0
            while counter < 6:
                print('last item')
                counter += 1



###Containers
# Lists, tuples, dictionaries and sets
#Storing multiple values in a variable

## Tuple
# Ex: Tuple = ('bob', 123, 'Lisa', ('another list'))

## List
# Ex: List = ['bob', 123, 'Lisa', ('another list')]

# => A tuple cannot change (immutable) while you can change the values of a list

## Set
# Ex: Set{1, 2, 3, 'test'}
# => Every entry is unique

##Dictionary
# Ex: Dictionary = {'name':'Bob', 123:'test', 'Lisa':(1,2,3)}
# This is key:value
# key:value pairs instead of single entries

#Practice
a_tuple = (1, 2, 3, 'a string')
a_list = [1, 2, 3, 'a string']
a_list.append('another string')
print(a_list)
# Tuple does not have 'append' method

a_set = {1, 2, 3, 4, 2, 4}
print(a_set)
# Every entry is unique, duplicated ones will be removed

print(set(a_list))
# => This will change the type
print(list(set(a_list)))
# => So will this

a_dictionary = {'key':'value', 123:[1,2,3]}
print(a_dictionary)

## How to get values from a container
# Indexing
# ['Lisa', 'Bob', 'Alex', 'Anna', 'John']
# ['Lisa', 'Bob', 'Alex', 'Anna', 'John']
# This is the index (start with 0)
# Ex [1] -> will return 'Bob'

# Slicing
# ['Lisa', 'Bob', 'Alex', 'Anna', 'John']
# ['Lisa', 'Bob', 'Alex', 'Anna', 'John']
# Ex [1:4:2] -> will return ['Bob', 'Anna']
# Start with 1
# End with 4 (not include this value)
# 2 hops

#Practice

user_list = ['Lisa', 'Bob', 'Alex', 'Anna', 'John']
print(user_list[0:3:2])

print(a_dictionary[123])


#Test
#Create a list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Create a new list: 8, 6, 4, 2
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(test_list[-3:0:-2])

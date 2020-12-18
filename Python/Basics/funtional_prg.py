# Funtional programming is all bout separation of concerns
# that means each part conserns itself about one that its good at
# separate data and funtions

# Pure funtions
    # same input same output
    # should not have side effects 
        # - changes nothing but input
        # doenst care about the outside world
        # different parts of the program doesnt touch each other

# map
    # creates a new map object that we have to convert to list
    # input list is not modified
my_list = [1, 2, 3]
def multiply_by2(item):
    return item*2
# 
print(list(map(multiply_by2, my_list)))

# filter
def isOdd(item):
    return item % 2 != 0

print(list(filter(isOdd, my_list)))

# zip
    # takes any two iterables doesnt have to be a list and can be more than two
your_list = [99,87,63]
print(list(zip(your_list, my_list)))

# reduce
    # doesnt come as a built in funtion
    # return a list no need for conversion
from functools import reduce

def accumutator(acc, item):
    return acc + item

print(reduce(accumutator,list(my_list),0))



# Lambda expressions
    # onetime anonymos fuctions that you dont need more than once

print('from Lamda funtions => ',list(map(lambda item: item*2, my_list)))



# Comprehensions: list, set, dictionary
    # they are a quick way to create a list, set or dict without looping

    # instead of 
looped_list = []
for char in 'hello':
    looped_list.append(char)

comp_list = [char for char in 'hello']
print(comp_list)
print([num * 2 for num in range(0,6)])
print([num ** 2 for num in range(0, 21) if num % 2 == 0])

    # for sets just use curly branckets
comp_set = {char for char in 'hello'}
print(comp_set)
print({num * 2 for num in range(0, 6)})
print({num ** 2 for num in range(0, 21) if num % 2 == 0})

    # for dict
simple_dict = { 'a': 1, 'b': 2, 'c': 3}
print({key:value**2 for key, value in simple_dict.items()})
print({value:value**2 for value in [3,4,5]})

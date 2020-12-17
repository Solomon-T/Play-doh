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

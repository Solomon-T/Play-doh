# what are python packages?
# python 3 vs 2
# 

    # for any language you need to learn the following
# terms - statements, variables, instanciation
# data types -
# actions - built in functions such as math functions like round(3.5)..
# best practices - 

    # Developer fundamentals
# dont memorize the dictionary ie. the docs. use it as you go.
# proper comments. https://realpython.com/python-comments-guide/
# understand DS - when to use which

    # Functions vs Methods
# Methods belong to a class while functions dont. Methods use .function


# -----------------------------------------------------------------------------
#                               # Data types
# -----------------------------------------------------------------------------
# fundamental datatypes
    # int
    # float
    # str
    # bool
    # list
    # tuple
    # set
    # dict
    # complex  # maybe we will never use it
# Classes -> custom types

# Specialized Data Types

# None
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#                           Variables in python
# -----------------------------------------------------------------------------
iq = 33
# assinging a variable is also called binding 33 is bound to iq
# best practices
    # snake_case
    # should start with a letter
    # cant start with a num
    # private Variables should start with _
    # constants should be in capital
    # dont use double underscore  __hihi should not exist

# a,b,c = 1,2,3 rapid assingment

# constants
    # all capitals but can be reassigned

# Expressinon vs statement
# expression is a piece of code that produces a value => 22 / 2
# a statement is an entire line of code => result = 22 / 2
# augumented assingment operator -> a += 2, a -= 2, a *= 2
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#                               Ints and Floats
# -----------------------------------------------------------------------------
type(1 / 2)  # => float 1 / 2 => 0.5
type(1 // 2)  # => int  1 // 2 => 0.5

# operations +, -, *, / and also **, //, %
# remember operator presidence (), **, * /, + - !!!!!!!!!!!  power  !!!!!!!!!!!!

    # math functions
# round(), abs(),

# binary number and ints
print('kjhflskhjfs opiuerh faypeu fyeorljf solo solo solo solo')
print(bin(5))
print(int('0b101',2))
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#                           Str
# -----------------------------------------------------------------------------
short_1 = 'short1'
short_2 = "short2"
long_str = ''' 
    Slala
    kaka
    mama
    '''
print(long_str)

    # string concatination
print('*' * 5) # -> *****
print('Xo' + ' kala')
# print('Xo' + 5) # wont work you have to convert it first using type conversion
print('Xo' + str(5))

# type conversions str(), int(), ...

    # Escape Sequences
# Use backslash and what ever comes afer it is considered a string
weather = "It\'s \"kind of\" sunny"
print(weather)
# \t adds a tab
# \n adds a new line


    # formatted strings
# add a frkn "f" infront of the sting and you can use variables wrapped in {}
name, score = 'Jay', 97
print('Hey ' + name + ' you got' + str(score)) 
# an fstring is the way to go
print(f'You {name} you got {score}') # python 3 
# you can also use .format passing in the fillers
print('You {0} you got {1}'.format(name, score))  # python 2
# switch the values that are in the {} to mix it around or leave it empty 
print('Yoo! {new_name} you got {new_score}'.format(
    new_name=name, new_score=score)
    )


    # Str indixes 
# string slicing upto but not including stop
# [start], [start:stop], [start:stop:stepover]
# [start:] start to the end of string, 
# [:stop] begining of sring till stop point, 
# [::stepover] begining to end of the stind while skipping by stepover
# [::1] the whole string no skipping
# [-1] only the last char, 
# [::-1] reverses the string
# [::-2] reverses the string while skipping one 
# [::],
# name[0] => J

# note strings are immutable. you cant cange an index. 
# my_str += 'r' actually creates a whole new str and reassings the variable with it

    # Builtin fintions vs built in methods
# must know funtions 
# str(), int(), abs, round,   print(), len(), replace

# join
new_sentence = ' '.join(['hi', 'you', '!'])

quote = 'to cry or not to cry'
quote = quote.replace('cry', 'be')

print(quote)

# methods belong to a class and us e a dot format
# name.find('a')
# to know -> replace, lower, upper ..... 
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#                               Boolean
# -----------------------------------------------------------------------------
# True, False
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#                               Lists
# -----------------------------------------------------------------------------
# the first DS we are learning and they are just an array
# well see the difference with arrays later on

# myList[i] throws an error if out of range

# list slicing is also a thing. same as in strings
    # list slicing doesnt mutate the list but creates a new list
my_list = [1,2,3,4]
my_list[0] = 99
new_list = my_list[:]
# new_list = my_list
new_list[0] = 100
print(new_list)
print(my_list)
# are mutable - we can replace at it

# list methods 
    # append - you cant do this new_list = old_list.append(33)
    # insert - also modifies the list in place
    # extend - same thing but takes in a list
    # pop - can take index to remove is not given removes from the end
    # remove - takes the value you want to remove 
    # clear - removes everything in the list
    # index - takes in an arg and returns the index where it is found, can take start and end
    # just use in instead of index - value in list - returns boolean value
    # count - counts how many times a value exits in a list
    # sort - vs the function sorted(list) - sorted doest modify the list
    # copy - same as list[:]
    # reverse - not the same as list[::-1], reverse modifies the list

# range - myList = list(range(1,4)) or list(range(5))

# list upacking
a, b, c, *other, d = [1,2,3,4,5,6]  
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#                           Dictionary(Dict)
# -----------------------------------------------------------------------------
# Our second DS
# if key doesnt exist throws an error. 
    # use get intead
    # key in myDict 
        # this checks both keys and values
        # key in user.keys() 
# also remember it is unordered
# a key can be anything thats immutable eg, string, int, boolean, tuple 
# a key overides the value is repeated

# you can creat by new_dict = dict(word= 'meaning')

# dict methods
    # keys
    # values
    # items - gives a touple
    # clear - doesnt return anything does it in place
    # copy
    # pop(key)
    # popItem - just removes a random value
    # update({'key': 4}) - takes in a key value pair
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#                               Tuple
# -----------------------------------------------------------------------------
# are like lists but immutable 
# use brackets instead of square brackets
# if you dont need a list to change always need a touple

# you can use slicing to create new touples 
my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:4]

q, w, g, *other2, z = (1, 2, 3, 4, 5, 6)

# methods
    # count
    # index

# we alse have len(my_touple)

# -----------------------------------------------------------------------------




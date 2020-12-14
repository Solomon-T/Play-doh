    # Data types
# int
# float
# str
# bool
# list
# tuple
# set
# dict
# complex # maybe we will never use it
# Classes -> custom types
# Specialized Data Types
# None

# -----------------------------------------------------------------------------

#                           Variables in python
# -----------------------------------------------------------------------------
iq = 33
# variables should be snake case
# assinging a variable is also called binding
# best practices
# snake_case
# should start with a letter
# private Variables should start with _
# constants should be in capital
# dont use double underscore

# a,b,c = 1,2,3 rapid assingment

# Expressinon vs statement
# expression is a piece of code that priduces a value
# a statement is an entire line of code

# augumented assingment operator -> a += 2
# -----------------------------------------------------------------------------

#                               Ints and Floats
# -----------------------------------------------------------------------------
# 1 / 2 => 0.5
# 1 // 2 => 0

# operations +, -, *, / and also **, //, %
# remember operator presidence (), **, * /, + -

    # math functions
# round(), abs(),

# binary number and ints
print(bin(5))
print(int('0b101',2))
# -----------------------------------------------------------------------------


#                           Str
# -----------------------------------------------------------------------------
long_str = ''' 
Slala
kaka
mama
'''

print(long_str)

# string concatination
print('*' * 5) # -> *****
print('Xo' + ' kala')
print('Xo' + 5) # wont work you have to convert it first using type conversion
print('Xo' + str(5))

# type conversions str(), int(), ...


    # Escape Sequence 
# Use backslash and what ever comes afer it is considered a string
weather = "It\'s \"kind of\" sunny"
print(weather)

# \t adds a tab
# \n adds a new line


# formatted strings
# add a frkn "f" infront of the sting and you can use variables wrapped in {}
name, score = 'Jay', 97
print('hey' + name + ' you got' + str(score)) 
print(f'You {name} you got {score}')
# you can also use .format passing in the fillers
print('You {0} you got {1}'.format(name, score))
# you can switch the values that are in the {}


    # Str indixes 
# string slicing upto but not including stop
# [start], [start:stop], [start:stop:skip]
# [start:], [:stop], [::skip]
# [-1], [-1], [::-1]
# [::],
# name[0] => J

# note strings are immutable. you cant cange an index. 
# my_str += 'r' actually creates a whole new str and reassings the variable with it

    # Builtin fintions vs built in methods
# must know funtions 
# str(), int(), abs, round,   print(), len(), 

# methods belong to a class and us e a dot format
# name.find('a')
# to know -> replace, lower, upper ..... 
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
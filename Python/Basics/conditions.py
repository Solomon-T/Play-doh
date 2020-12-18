# you dont need brackets in your conditions
# elif instead of else if
# after contion we just add a ':'

# -----------------------------------------------------------------------------
#                           Conditional
# -----------------------------------------------------------------------------
# if, elif, else, ternary
# and istead of &&

is_old = False
is_beautiful = True
is_married = False

# if is_old and is_beautiful:
#     print('Marry her')
# elif is_married:
#     pass
# else:
#     print('You smart nyash')

# ternary 
print('Marry her now!') if is_beautiful else print('You can do better bro!')

# indentation 
# interpreter looks for spacing instead of curly braces

# Logical operators
# and, or , <, >, <=, >=, ==, != ,not ,not()

# chaining conditionals - is a big yes in python
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#               Truthy and Falsy values in python
# -----------------------------------------------------------------------------
# Falsey values -
# Truthy values - 
# is checks the  value
print(True == 1)
print('' == 1)
print('1' == 1)     # no type conversion only hapens in Truthy
print([] == 1)
print(10 == 10.0) 
print([] == [])

# is checks the memory lication therefore stings and numbers are true
print(True is 1)
print('' is 1)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#                               short circuiting
# -----------------------------------------------------------------------------
# In and & or intepreter skips second part of conditioning is its not vecessary
# -----------------------------------------------------------------------------

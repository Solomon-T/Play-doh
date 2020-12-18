def say_hello():
    '''
    Info: This functions just prints the word Hello!
    '''
    print('Hello!')
    return True

say_hello()

# Note: You cant call a function before you define it.
# parameters vs arguments
    # parameters are the names we give when defining a function
    # arguments are the actual values we use when we invoke a function

# Positional argumens vs keyword arguments- keyword is bad practice
# Default parameters are the same 

# We always need a return. Python doesnt do implicit return. Returns None

# A good rule of thumb for a function should
    # Should do one thing really well.
    # Should return something

# methods vs funtions
    # again methods are owened by objects. and called by .method()
    # funtions take in the argument 

# Docstrings
    # comments inside of a funtion that shows up when you start typing 
    # you can also use help
print(help(say_hello))
    #  you can also use __doc__
print(say_hello.__doc__)

# *args, **kwargs
def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
super_func(1,2,3,4, name= 44, avg= 2.5)

    # Rule: params, *args, default params, **kwargs

# Walrus Operator
a = 'abcdefghij'

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]



# Scope
    # global is outside a fuction
    # funtion scope is only when we define a var inside a func
    # not if statemests have global scope

a = 1
def confusion():
    a = 5 
    return a

print(confusion())      # 5 
print(a)                # 1

    #1 - start with local scope which includes parameters
    #2 - parent local
    #3 - global / nonlocal
    #4 - built in stuff above global

# global keyword
    # used inside a function to point to a global variable outside

# dependency injection
    # just nesting functions

# nonlocal keyword
    # grab from parent scope


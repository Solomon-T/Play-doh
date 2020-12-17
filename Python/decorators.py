# funtions are first class citizens. 
# Higher order function is a funtion that accepts another function

# decorator just wraps another funtion to super boost it 
def my_decorator(func):
    """
    this is my custom decorator
    """
    def wrap_func():
        print('*******')
        func()
        print('*******')
    return wrap_func

@my_decorator
def hello():
    print('helllooooo!!!!')


def normal_hello():
    print('helllooooo!!!!')

hello()
normal_hello()

# what python is doing under the hood 
super_hello = my_decorator(hello)
super_hello()

my_decorator(hello)()


# when we have an argument
def my_decorator2(func):
    def wrap_func(x):
        print('*******')
        func(x)
        print('*******')
    return wrap_func


@my_decorator2
def hello2(x):
    print(x)

hello2('argument')
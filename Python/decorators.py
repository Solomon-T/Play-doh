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


# Create an @authenticated decorator that only allows the function to run
# if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    # code here
    def wrap_func(user):
        if user['valid']:
            fn(user)
        else:
            print('Sorry, you fake!')
    return wrap_func


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)


# --------- his implementation below -------------------
def authenticated2(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        return fn(*args, **kwargs)
  return wrapper


@authenticated
def message_friends2(user):
    print('message has been sent')


message_friends2(user1)

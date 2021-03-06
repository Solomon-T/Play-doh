# ------------------------------------------------------------------------------
#                                           Numbers
# ------------------------------------------------------------------------------
type(1)  # int
type(-10)  # int
type(0)  # int
type(0.0)  # float
type(2.2)  # float
type(4E2)  # float - 4*10 to the power of 2

# Arithmetic
10 + 3  # 13
10 - 3  # 7
10 * 3  # 30
10 ** 3  # 1000
10 / 3  # 3.3333333333333335
10 // 3  # 3 --> floor division - no decimals and returns an int
10 % 3  # 1 --> modulo operator - return the reminder. Good for deciding if number is even or odd

# Basic Functions
pow(5, 2)      # 25 --> like doing 5**2
abs(-50)       # 50
round(5.46)    # 5
round(5.468, 2)  # 5.47 --> round to nth digit
bin(512)       # '0b1000000000' -->  binary format
hex(512)       # '0x200' --> hexadecimal format

# Converting Strings to Numbers
age = input("How old are you?")
age = int(age)
pi = input("What is the value of pi?")
pi = float(pi)


# ------------------------------------------------------------------------------
#                                           STRINGS
# ------------------------------------------------------------------------------

type('Hellloooooo')  # str

'I\'m thirsty'
"I'm thirsty"
"\n"  # new line.
"\t"  # adds a tab

'Hey you!'[4]  # y
name = 'Andrei Neagoie'
name[4]     # e
name[:]     # Andrei Neagoie
name[1:]    # ndrei Neagoie
name[:1]    # A
name[-1]    # e
name[::1]   # Andrei Neagoie
name[::-1]  # eiogaeN ierdnA
name[0:10:2]  # Ade e
# : is called slicing and has the format [ start : end : step ]

'Hi there ' + 'Timmy'  # 'Hi there Timmy' --> This is called string concatenation
'*'*10  # **********



# Basic Functions
len('turtle')  # 6

# Basic Methods
# 'I am alone' --> Strips all whitespace characters from both ends.
'  I am alone '.strip()
# 'On an islan' --> # Strips all passed characters from both ends.
'On an island'.strip('d')
'but life is good!'.split()           # ['but', 'life', 'is', 'good!']
# 'Help you' --> Replaces first with second param
'Help me'.replace('me', 'you')
'Need to make fire'.startswith('Need')  # True
'and cook rice'.endswith('rice')      # True
'bye bye'.index('e')                  # 2
'still there?'.upper()                # STILL THERE?
'HELLO?!'.lower()                     # hello?!
'ok, I am done.'.capitalize()         # 'Ok, I am done.'
# 4 --> returns the starting index position of the first occurence
'oh hi there'.find('i')
'oh hi there'.count('e')              # 2


# String Formatting
name1 = 'Andrei'
name2 = 'Sunny'
# Hello there Andrei and Sunny - Newer way to do things as of python 3.6
print(f'Hello there {name1} and {name2}')
# Hello there Andrei and Sunny
print('Hello there {} and {}'.format(name1, name2))
# Hello there Andrei and Sunny --> you can also use %d, %f, %r for integers, floats, string representations of objects respectively
print('Hello there %s and %s' % (name1, name2))

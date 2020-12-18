    # for loops
# iterable = (1,2,3,4)

# for item in iterable:
#     print(item)
# print('-----------')

# print(item)
#  note the item is available outside the for loop

# iterarion a dictionary
# points = {
#     'utd': 90,
#     'city': 23,
#     'liv': 57,
#     'ars': 6,
#     'tot': 79,
#     'chel': 14,
#     'lec': 41,
# }
# print('-----------')
# for item in points: # key
#     print(item) 
# print('-----------')
# for item in points.items(): # (key, val)
#     print(item)
# print('-----------')
# for key, value in points.items():  # (key, val)
#     print(key, value)
# print('-----------')
# for item in points.values(): # key 
#     print(item)
# print('-----------')
# for item in points.keys(): # Key
#     print(item)

    # range object
my_range = range(0,10)
another_range = range(4)
for i in my_range:
    print(i)
# underscore is used if we dont need the item
for _ in another_range:
    print(f'ill do this {len(list(another_range))} times')


    # enumerate - gives you an index counter over an iterable
for idx, item in enumerate('hello'):
    print(idx, item)


# while loops
i = 0
# while i < 2:
#     print(i)
#     i += 1

# # while else
# while 1 < 0:
#     pass
# else:
#     pass

while True:
    response = input('How is your day today? \n')

    if response == 'Great!':
        break

    print(f'Only {response}? lets do this again!')

# break and continue works as normal
# pass is a do nothing instruction. A code block needs to do something so pass 

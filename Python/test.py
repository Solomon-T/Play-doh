# print({num ** 2 for num in range(0, 21) if num % 2 == 0})

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

print(list({num for num in some_list if some_list.count(num) > 1}))
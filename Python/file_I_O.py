
my_file = open('test.txt')

print(my_file)
print(my_file.read())
my_file.seek(0)                 # takes the cursor back to the first line
print('----------------------')
print(my_file.readline())

my_file.seek(0)
print(my_file.readlines())

my_file.close()

# help us generate a sequence of values
# a generator is a subset of iterable
# a generator funtion is created using the range and the yeild keywords
# yield poses the funtion and returns to it when next is called 
# next can only be called as much as the length of the range  

def generator_fn(num):
    for i in range(num):
        yield i * 2

g = generator_fn(6)
# next(g)
# next(g)
print(g)
# print(next(g))

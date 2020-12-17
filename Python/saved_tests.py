#Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('first', 1)
cat2 = Cat('second', 28)
cat3 = Cat('third', 3)

# 2 Create a function that finds the oldest cat


def find_oldest(*cats):
    oldest = 0
    for cat in cats:
        if cat.age > oldest:
            oldest = cat.age

    return oldest

# dude you have max use it you nut head


def get_oldest_cat(*catAges):
    return max(catAges)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


print(f"The oldest cat is {find_oldest(cat1,cat2,cat3)} years old.")
print(
    f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age) } years old.")

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(sorted(a, key=lambda item: item[1])) # note: sorted returns a new list

print(a.sort(key=lambda item: item[1])) # note:sort modifies a and returns none.

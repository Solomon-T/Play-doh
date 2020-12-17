# basically just organising files in multiple files
# each .py file is a module
# naming modules is snakecase, everything lowercase separated by underscore
# a package is a folder contining modules
import module_utility
import module_packahe.hello_package

from module_packahe.deep_module.deep_package import deep1, deep2, deep3
# arguably the best is below
from module_packahe.deep_module_2 import deep_package_2 
# you can also import all modules from a package
from module_packahe import *

print(module_utility.hello_world())
print(module_packahe.hello_package.hello_package())

print(deep1())
print(deep2())
print(deep3())

print(deep_package_2.deep1())
print(deep_package_2.deep2())
print(deep_package_2.deep3())


# __name__
if __name__ == '__main__':
    print('I am the main man')


# python built in packages - equivalent to standart library in other languages
from random import shuffle
import random

print(random)
print(random.randint(2,16))

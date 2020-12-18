# naming is CamelCase instead of snake
# name of class is always singular
# in classes the default always when we write a method is self.
# note you dont pass in the self as you are instanciating an instance
# we can add attributes outside the class deffinition
# isinstance(instance, Class) - checks if an item is the instance of a class.

# Note the difference btn objects and dictionaries to access atrributes
    # for an object we use the dot notation 
    # for a dictionary you use square brackets

class PlayerCharacter:
    # Class Object Attribute, exists for all instances and cant be changed
    profession = 'Footballer'
    def __init__(self, name):
        self.name = name            # attributes / property 

    def shout(self):                # note how we access class and instance attr
        print(f"heeeyy I\'m {self.name} and I am a {PlayerCharacter.profession}")
        # note this function returns None

    # class method are created under decorator
    # takes in cls inplace of self
    # can be used without instanciating
    @classmethod
    def adding_things(cls,a,b):
        return a + b

    # static methods are aso created under decorator
    # doesnt takes in cls nor self
    # can be used without instanciating
    @staticmethod
    def multiplying_things(a,b):
        return a * b

player1 = PlayerCharacter('Kaka')
player2 = PlayerCharacter('Scholes')
# print(PlayerCharacter.adding_things(1,2))
# print(player1.name)
# print(player2.name)
# adding extra attributes
player1.super_powers = 'Baking'
# print(player1.super_powers)
# help gives you the blue print of an object
# print(player2.shout())



# 4 PILLARS OF OOP
    # Encapsulation - is the binding of data and funtions that munipulate it
    # Abstraction - hidding info and giving access only whats needed
    # Inheritance - 
    # Polymorphism - in python it referes to this idea that object classes can 
                #    share the same method name but act differently

# Public and Private
    # no true pravacy in python
    # we just do _name thats just agreed between programers
    # __something belongs to python and should never be overwritten


class User():
    # Note we don't have to have __init__ if we dont need attributes
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('logged_in')

# To inherit simply pass in the parent class in the brackets
# Look at how to usr super in init of the __init__ for the Wizard class
# To extend just add other methods to the class
# It is possible to overide the parrent class
class Wizard(User):
    def __init__(self, name, power, email='none'):
        User.__init__(self, email)
        # super.__init__(email)   # a better and modern way
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} attacking with the power of {self.power}')

class Archer(User):
    def __init__(self, name, number_of_arrows, email='none'):
        User.__init__(self, email)
        # super.__init__(email)
        self.name = name
        self.number_of_arrows = number_of_arrows

    def attack(self):
        print(f'{self.name} attacking with the number_of_arrows of {self.number_of_arrows}')

wiz1 = Wizard('Masenga', 'Kabwela')
wiz1.sign_in()
wiz1.attack()

archer = Archer('Xolo', 2534)
archer.sign_in()
archer.attack()


# isinstance
    # isinstance(istance, Class) => true
    # isinstance(istance, ParentClass) => true
    # isinstance(istance, Object) => true
        # everything ingerits form the python object base class
        # this is where all the dunder methods on everything come from

# Multiple inheritance
class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self,name, power)

hb = Hybrid('Xolo', 'ungo', 693)
print(hb.number_of_arrows)


# MRO - method resolution order - uses DFS under the hood
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 2

class D(B,C):
    pass

print(D.num)
print(D.mro())
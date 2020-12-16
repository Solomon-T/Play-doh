# naming is CamelCase instead of snake
# name of class is always singular
# in classes the default always when we write a method is self.
# note you dont pass in the self as you are instanciating an instance
# we can add attributes outside the class deffinition

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

print(PlayerCharacter.adding_things(1,2))

print(player1.name)
print(player2.name)

# adding extra attributes
player1.super_powers = 'Baking'
print(player1.super_powers)

# help gives you the blue print of an object
print(player2.shout())



# 4 PILLARS OF OOP
    # Encapsulation - is the binding of data and funtions that munipulate it
    # Abstraction - hidding info and giving access only whats needed

# <------------------------- __init__ method ------------------------->
'''
The __init__ method is a special, built-in Python method that automatically initializes an object's attributes when a new instance of a class is created.
It is often referred to as a constructor or initializer, and it belongs to a category of special methods known as "dunder" (double underscore) methods.
'''

class PersonOne:
    def __init__(self, name, age):  # We can also set default value such as: (age= 18)
        self.name = name
        self.age = age


person1 = PersonOne("Awais", 20)
print(person1.name)
print(person1.age)

# Using __init__() makes it easier to create objects with initial values.
# Otherwise, Without the __init__() method, you would need to set properties manually for each object.


# Multiple Parameters:
class PersonTwo:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = PersonTwo("Zain", 30, "Lahore", "Pakistan")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)




# <------------------------- self Parameter ------------------------->

# The self parameter is a reference to the current instance of the class.It is used to access properties and methods that belong to the class.
class PersonThree:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    # Without self, Python would not know which object's properties you want to access:
    def person_info(self):
        return (f"Hi, My name is {self.name} and I'm {self.age} years old.")


p1 = PersonThree("John", 34)
p2 = PersonThree("Sara", 21)

print(p1.person_info())
print(p2.person_info())




# <------------------------- Calling Methods with self ------------------------->

# You can also call other methods within the class using self:
class PersonThree:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
    
    def greet(self):
        return f"Hello, {self.name}"
    
    
    def welcome(self):
        message = self.greet()  #Call one method from another method using self.
        return f"{message}. Welcome to the {self.city} city"


p1 = PersonThree("John", "New York")

print(p1.welcome())

# <--------------------------- Inheritance --------------------------->
# Inheritance in Python is a core concept of Object-Oriented Programming (OOP) that allows a new class to adopt the attributes and methods of an existing class.

# It establishes an "is-a" relationship between classes, promoting code reusability so you don't have to rewrite the same logic multiple times.

# Key Terminology:
# Parent Class (Base or Superclass): The existing class whose features(methods and properties etc) are being inherited.

# Child Class (Derived or Subclass): The new class that inherits features(methods and properties etc) from the parent class.


class Animal:   # Parent Class
    def __init__(self, name):
        self.name = name
    
    
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):  # Child class inheriting from Animal
    def bark(self):
        return f"{self.name} says Woof!"


mydog = Dog("Buther")

# Accessing inherited method from Parent class
print(mydog.eat())

# Accessing method from Child class
print(mydog.bark())




# <--------------------------- Add __init__ Function --------------------------->
# If you want to add the __init__() function to the child class then the child class will no longer inherit the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Person:
    def __init__(self, fname):
        self.fname = fname



class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname) # That's how you can kept the inheritance of the parent class and ready to add functionality in the __init__() function.
        self.lname = lname
    
    
    def greet(self):
        return f"Hello, {self.fname} {self.lname}"


s1 = Student("Awais", "Raza")

print(s1.greet())




# <--------------------------- Use the super() Function --------------------------->
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f"Animal Name : {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def detail(self):
        print(f"{self.name} is a {self.breed}")

d = Dog("Buther", "German Shepherd")

d.info()
d.detail()
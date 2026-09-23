
# <------------------------ Oop (introduction) ------------------------>
'''
Oop stands for: Object Oriented Programming.

The coding you do earlier (Week_01, Week_02 and Week_03) is Procedural Programming (POP) which focuses on writing step-by-step functions that operate on data,
In Object-Oreinted Programming, Python allows you to structure your code using classes and objects for better organization and reusability.

'''

# <------------------------ Advantages of Oop ------------------------>
'''
1. Enhanced Code Reusability (DRY Principle) :
                OOP allows you to write code once and use it across multiple parts of your application without duplication, adhering to the "Don't Repeat Yourself" (DRY) principle.

2. Modularity and Better Organization :
                OOP changes how code is organized by bundling related data and behaviors into standalone units called classes.

3. Data Security and Integrity :
                By separating an object’s internal logic from its external interface, OOP prevents accidental or malicious data modification.

4. Code Flexibility and Extensibility :
                Python’s dynamic nature complements OOP to make expanding existing software incredibly straightforward.
'''


# <------------------------ Classes and Objects ------------------------>
'''
Classes and objects are the two core concepts in object-oriented programming.

A class defines what an object should look like, and an object is created based on that class. For example:

Class	        Objects
Fruit	        Apple, Banana, Mango
Car	            Volvo, Audi, Toyota

When you create an object from a class, it inherits all the variables and functions defined inside that class.
'''

class FristClass:   # We use "class" keyword to create a class
    greet = "Hello World!"  # "greet" is its property 


x = FristClass()    # x is now an object which inherit FirstClass().

# Now x can use every properties and methods defined in FirstClass():
print(x.greet)

del x   # Using "del" keyword your can delete an object


# Multiple Objects
# You can create multiple objects from the same class.Each object is independent and has its own copy of the class properties.

class MyClass:
    x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
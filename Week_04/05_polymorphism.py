
# <-------------------------- Introduction -------------------------->
'''
The word Polymorphism is the combination of two words:
"poly"  -> many
"morph" -> form
combined "many form" which mean same name of thing has ability to perform different tasks.

In programming it refets to methods/fucntions/operators with the same name that can be executed on mnay objects or class.

----- Advantages -----
It allows you to write more
-> flexible
-> reusable
-> readable
code by focusing on what an object can do rather than what specific type it is

'''
# Python demonstrates polymorphism in four primary ways:

# <-------------------------- 1. Function Polymorphism -------------------------->
# The same built-in function can accept different data types and process them according to their specific structures.

# ----- Example -----
# The len() function can calculate the length of a string, a list, or a dictionary, even though they store data differently.

print(len("Python"))  # Outputs 6 (counts characters)
print(len([1, 2, 3])) # Outputs 3 (counts elements)



# <-------------------------- 2. Operator Polymorphism (Operator Overloading) -------------------------->
# The same operator can perform different operations based on the types of values (operands) you provide.

# ----- Example -----
#  The + operator performs arithmetic addition on numbers but concatenates strings together.

print(5 + 5)          # Outputs 10
print("Py" + "thon")  # Outputs "Python"



# <-------------------------- 3. Method Overriding (Runtime Polymorphism) -------------------------->
# In object-oriented programming, a child class can provide its own unique implementation of a method that is already defined in its parent class.
# When you call that method, Python determines which version to run at runtime based on the object's class.

# ----- Example -----
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())



# <-------------------------- 4. Duck Typing -------------------------->
# Because Python is dynamically typed, it uses a concept called "duck typing": "If it walks like a duck and quacks like a duck, it's a duck."
# This means Python doesn't care about an object's actual class hierarchy; it only cares if the object has the required method or behavior.

# ----- Example -----
class Car:
    def move(self):
        return "Car is Moving..."

class Boat:
    def move(self):
        return "Boat is Sailing..."

class Plane:
    def move(self):
        return "Plane is Flying..."


def vehicle_moveing(vehicle):
    print(vehicle.move())


for vehicle in (Car(), Plane(), Boat()):
    vehicle_moveing(vehicle)
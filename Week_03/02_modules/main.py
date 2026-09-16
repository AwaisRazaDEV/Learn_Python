'''
A module is simply a file containing Python code (with a .py extension) that can define functions, classes, and variables.
Modules allow you to break down large, complex programs into smaller, manageable, and organized files that you can reuse across different projects
'''

# Using a module
# I have created a module named as test_module. Now we are using the module using a improt statement:
import test_module
import test_module as tm    # In this we can shorter the name of our module.

tm.greeting("World")
# In that way we can use our self made module and also any function, class or variables define inside that moduel.


from test_module import student     # In this way can import specific part of our module.

print(test_module.student["name"])
print(test_module.student["subject"])


# <---------------------- Practical ---------------------->
import calculator

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("Addition :", calculator.add(num1, num2))
print("Subtraction :", calculator.subtract(num1, num2))
print("Multiplication :", calculator.multiply(num1, num2))
print("Division :", calculator.divide(num1, num2))
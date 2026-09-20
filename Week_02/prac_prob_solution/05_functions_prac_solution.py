
# <--------------------------- Level 1 — Parameters & Arguments --------------------------->

# 1. Create a function that takes a person's name as a parameter and greets them.
# def greet(name):
#     print("Hello", name  + "!")

# name = input("Enter your name : ")
# greet(name)

# 2. Create a function that takes two numbers as parameters and returns their sum.
# def sum(num1, num2):
#     return num1 + num2

# 3. Create a function that takes two numbers and returns their difference.
# def difference(num1, num2):
#     return num1 - num2

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# print("Sum is :", sum(num1, num2))
# print("Differece is :", difference(num1, num2))

# 4. Create a function that takes three numbers and returns their product.
# def product(num1, num2, num3):
#     return num1 * num2 * num3

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))
# print("Product is :", product(num1, num2, num3))

# 5. Create a function that takes a person's name and age and displays a sentence containing both.
# def about(name, age):
#     print(f"Hi! My name is {name} and, I am {age} years old.")

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# about(name, age)

# 6. Create a function that takes the length and width of a rectangle and calculates its area.
# def area_of_rectangle(length, width):
#     return length * width

# a = int(input("Enter lenght of rectangle : "))
# b = int(input("Enter width of rectangle : "))

# print("Area of rectangle is :", area_of_rectangle(length=a, width=b))

# 7. Create a function that takes a number and determines whether it is even or odd.
# def even_or_odd(number):
#     if number % 2 == 0:
#         print(number, "is even number")
#     else:
#         print(number, "is odd number")

# num = int(input("Enter any positive number : "))
# even_or_odd(num)

# 8. Create a function that takes a student's name and marks and displays whether the student passed or failed.
# def student_info(name, marks):
#     if marks > 25:
#         print(f"{name}, You are passed.")
#     else:
#         print(f"{name}, You are failed.")

# stu_name = input("Enter your name : ")
# stu_marks = int(input("Enter your marks : "))

# student_info(name=stu_name, marks=stu_marks)

# 9. Create a function that takes three numbers and returns the largest number.
# def largest_num(a, b, c):
#     if a > b and a > c:
#         print(f"{a} is a greater number.")
#     elif b > c and b > a:
#         print(f"{b} is a greater number.")
#     elif c > a and c > b:
#         print(f"{c} is a greater number.")
#     else:
#         print("Don't enter the same numbers.")

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))
# print("Product is :", largest_num(a=num1, b=num2, c=num3))

# 10. Create a function that takes a temperature in Celsius and converts it to Fahrenheit.
# def tem_converter(celsius):
#     fahrenheit =  (celsius * 9 /5) + 32
#     return fahrenheit

# temperature = int(input("Enter temperature in celsius : "))
# print("Temperature in Fahrenheit is :", tem_converter(temperature))



# <--------------------------- Level 2 — Arguments --------------------------->

# 11. Create a function with three parameters and call it using positional arguments.
# def demo(first, second, third):
#     print("This is first positional argument :", first)
#     print("This is second positional argument :", second)
#     print("This is third positional argument :", third)

# demo("Apple", 1, True)

# 12. Create a function with three parameters and call it using keyword arguments.
# def demo(first, second, third):
#     print("This is first keyword argument :", first)
#     print("This is second keyword argument :", second)
#     print("This is third keyword argument :", third)

# demo(third="Apple", first=1, second=True)

# 13. Create a function that has a default value for one parameter. Call it once using the default value and once by providing your own value.
# def test(name = "guest"):
#     print("Hello", name)

# test()  # Default parameter
# test("Awais")   # Given value

# 14. Create a function that takes a person's name, age, and city. Call the function multiple times with different arguments.
# def person_info(name, age, city):
#     print(f"{name} is {age} years old and lives in {city}")

# person_info("Awais", 10, "Islamabad")
# person_info("Sara", 20, "Lahore")
# person_info("Zain", 30, "Karachi")

# 15. Create a function that calculates the total price of an item based on its price and quantity. Use appropriate arguments when calling it.
# def about_item(item, price, unit,  quantity= 1):
#     if unit.lower() == "kg" or unit.lower() == "litre":
#         total_price = price * quantity
#     elif unit.lower() == "dozen":
#         total_quantity = (quantity * 12)
#         total_price = price * total_quantity
#     print(f"For your {quantity}{unit} of {item}, your total price is PKR {total_price}/-")

# about_item("Sugar", 200, "kg", 2)
# about_item("Eggs", 20, "dozen", 1)
# about_item("Milk", 280, "litre", 2.5)

# 16. Create a function that calculates a student's average from five marks passed as arguments.
# def average_marks(mark1, mark2, mark3, mark4, mark5):
#     total_mark = mark1 + mark2 + mark3 + mark4 + mark5
#     return total_mark / 5

# print("Average marks are :", average_marks(1, 2, 3, 4, 5))

# 17. Create a function that accepts a person's name and country, where the country has a default value.
# def about_me(name, country = "USA"):
#     print(f"Hi! It's {name} form {country}")

# about_me("Awais", "Pakistan")
# about_me("John")

# 18. Create a function that takes two numbers and an operation choice, then performs the requested operation.
# def mini_calculator(num1, num2, operation):
#     if operation == 1:
#         operation = "Addition"
#         print(f"You choose {operation} Operation : ")
#         return num1 + num2
    
#     elif operation == 2:
#         operation = "Substraction"
#         print(f"You choose {operation} Operation : ")
#         return num1 - num2
    
#     elif operation == 3:
#         operation = "Division"
#         print(f"You choose {operation} Operation : ")
#         return num1 / num2
    
#     elif operation == 4:
#         operation = "Multiplication"
#         print(f"You choose {operation} Operation : ")
#         return num1 * num2
    
#     else:
#         print("Enter option between 1-4")
    

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# print("\n==== CHOOSE OPTION FOR OPERARION ====")
# print("1 - For Addition")
# print("2 - For Subtraction")
# print("3 - For Division")
# print("4 - For Multiplication\n")
# c = int(input("Enter your choice : "))

# result = mini_calculator(a, b, operation=c)
# print("The result is :", result)


# <--------------------------- Level 3 — Scope --------------------------->

# 19. Create a global variable representing a tax rate. Create a function that uses this variable to calculate the tax on a given price.
tax_rate = 16.5 * (1 / 100)
def calculate_tax(price):
    return price * tax_rate

print("Your tax is :", calculate_tax(50000))

# 20. Create a function with a local variable and use that variable inside the function.
def demo():
    x = 12345
    print(x)

demo()
# 21. Create two different functions where each function has its own local variable with the same name. Use both functions and observe that they maintain separate values.

# 22. Create a global variable representing a counter. Create a function that reads and displays its value without creating another variable with the same name.
# 23. Create a program with a global variable called name and a function containing a local variable with the same name. Display both values from their respective scopes.
# 24. Create two functions that each have a local variable called message, but give the variables different values.
# 25. Create a function that receives a parameter called number and also contains another local variable. Use both inside the function.



# <--------------------------- Level 4 — Mixed Challenges --------------------------->

# 26. Create a function that receives a student's name and three marks. Calculate the average and display the student's result.
# 27. Create a function that receives a product's name, price, and quantity. Calculate and display the total cost.
# 28. Create a function that receives a person's age and determines whether they are a child, teenager, adult, or senior.
# 29. Create a function that receives a number and returns the sum of all numbers from 1 up to that number.
# 30. Create a function that receives a list of numbers and returns the largest number.
# 31. Create a function that receives a list of numbers and returns how many numbers are even.
# 32. Create a function that receives a list of numbers and calculates their average.
# 33. Create a function that receives a student's name and a list of marks. Display the student's name, highest mark, lowest mark, and average.
# 34. Create a function that receives a username and password and determines whether they match predefined login information stored outside the function.
# 35. Create a program with a global variable representing a shop's discount percentage. Create a function that receives an item's price and calculates its discounted price.



# <--------------------------- Harder Mixed Challenges --------------------------->

# 36. Create a function that receives a number and returns whether it is prime.
# 37. Create a function that receives a number and calculates its factorial.
# 38. Create a function that receives a list and a value, then determines how many times that value appears in the list.
# 39. Create a function that receives two lists and returns the elements that appear in both lists.
# 40. Create a function that receives a dictionary containing student names and marks, then determines which student has the highest marks.
# 41. Create a function that receives a sentence and counts how many words it contains.
# 42. Create a function that receives a sentence and returns the number of unique words using a set.
# 43. Create a function that receives a list of numbers and returns a new list containing only the even numbers.
# 44. Create a function that receives a list of numbers and returns a new list containing only numbers greater than 50.
# 45. Create a function that receives student information through parameters and uses a global variable for the passing-mark requirement.



# <--------------------------- Final Mixed Challenges --------------------------->

# 46. Build a small student grading program using functions. Use parameters for student information, a global variable for the passing threshold, and local variables for calculations.
# 47. Build a simple shopping-bill program using separate functions for calculating subtotal, discount, and final price.
# 48. Build a simple calculator using functions for addition, subtraction, multiplication, and division. Pass the required values as arguments.
# 49. Build a number-analysis program where a function receives a number and determines whether it is positive/negative, even/odd, and prime/not prime.
# 50. Build a small student database using a dictionary and functions. Create functions for adding a student, finding a student's marks, calculating the average, and finding the highest-scoring student.
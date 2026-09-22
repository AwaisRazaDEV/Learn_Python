
# <--------------------------- Level 1 — Parameters & Arguments --------------------------->

# 1. Create a function that takes a person's name as a parameter and greets them.
def greet(name):
    print("Hello", name  + "!")


name = input("Enter your name : ")
greet(name)




# 2. Create a function that takes two numbers as parameters and returns their sum.
def sum(num1, num2):
    return num1 + num2




# 3. Create a function that takes two numbers and returns their difference.

def difference(num1, num2):
    return num1 - num2


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("Sum is :", sum(num1, num2))
print("Differece is :", difference(num1, num2))




# 4. Create a function that takes three numbers and returns their product.

def product(num1, num2, num3):
    return num1 * num2 * num3


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

print("Product is :", product(num1, num2, num3))




# 5. Create a function that takes a person's name and age and displays a sentence containing both.

def about(name, age):
    print(f"Hi! My name is {name} and, I am {age} years old.")


name = input("Enter your name : ")
age = int(input("Enter your age : "))

about(name, age)




# 6. Create a function that takes the length and width of a rectangle and calculates its area.

def area_of_rectangle(length, width):
    return length * width


a = int(input("Enter lenght of rectangle : "))
b = int(input("Enter width of rectangle : "))

print("Area of rectangle is :", area_of_rectangle(length=a, width=b))




# 7. Create a function that takes a number and determines whether it is even or odd.

def even_or_odd(number):
    if number % 2 == 0:
        print(number, "is even number")
    else:
        print(number, "is odd number")


num = int(input("Enter any positive number : "))

even_or_odd(num)




# 8. Create a function that takes a student's name and marks and displays whether the student passed or failed.

def student_info(name, marks):
    if marks > 25:
        print(f"{name}, You are passed.")
    else:
        print(f"{name}, You are failed.")


stu_name = input("Enter your name : ")
stu_marks = int(input("Enter your marks : "))

student_info(name=stu_name, marks=stu_marks)




# 9. Create a function that takes three numbers and returns the largest number.

def largest_num(a, b, c):
    if a > b and a > c:
        print(f"{a} is a greater number.")
    elif b > c and b > a:
        print(f"{b} is a greater number.")
    elif c > a and c > b:
        print(f"{c} is a greater number.")
    else:
        print("Don't enter the same numbers.")


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

print("Product is :", largest_num(a=num1, b=num2, c=num3))




# 10. Create a function that takes a temperature in Celsius and converts it to Fahrenheit.

def tem_converter(celsius):
    fahrenheit =  (celsius * 9 /5) + 32
    return fahrenheit


temperature = int(input("Enter temperature in celsius : "))

print("Temperature in Fahrenheit is :", tem_converter(temperature))



# <--------------------------- Level 2 — Arguments --------------------------->

# 11. Create a function with three parameters and call it using positional arguments.

def demo(first, second, third):
    print("This is first positional argument :", first)
    print("This is second positional argument :", second)
    print("This is third positional argument :", third)


demo("Apple", 1, True)




# 12. Create a function with three parameters and call it using keyword arguments.

def demo(first, second, third):
    print("This is first keyword argument :", first)
    print("This is second keyword argument :", second)
    print("This is third keyword argument :", third)


demo(third="Apple", first=1, second=True)




# 13. Create a function that has a default value for one parameter. Call it once using the default value and once by providing your own value.

def test(name = "guest"):
    print("Hello", name)


test()  # Default parameter
test("Awais")   # Given value




# 14. Create a function that takes a person's name, age, and city. Call the function multiple times with different arguments.

def person_info(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")


person_info("Awais", 10, "Islamabad")
person_info("Sara", 20, "Lahore")
person_info("Zain", 30, "Karachi")




# 15. Create a function that calculates the total price of an item based on its price and quantity. Use appropriate arguments when calling it.

def about_item(item, price, unit,  quantity= 1):
    if unit.lower() == "kg" or unit.lower() == "litre":
        total_price = price * quantity
    elif unit.lower() == "dozen":
        total_quantity = (quantity * 12)
        total_price = price * total_quantity

    print(f"For your {quantity}{unit} of {item}, your total price is PKR {total_price}/-")


about_item("Sugar", 200, "kg", 2)
about_item("Eggs", 20, "dozen", 1)
about_item("Milk", 280, "litre", 2.5)




# 16. Create a function that calculates a student's average from five marks passed as arguments.

def average_marks(mark1, mark2, mark3, mark4, mark5):
    total_mark = mark1 + mark2 + mark3 + mark4 + mark5
    return total_mark / 5


print("Average marks are :", average_marks(1, 2, 3, 4, 5))




# 17. Create a function that accepts a person's name and country, where the country has a default value.

def about_me(name, country = "USA"):
    print(f"Hi! It's {name} form {country}")


about_me("Awais", "Pakistan")
about_me("John")




# 18. Create a function that takes two numbers and an operation choice, then performs the requested operation.

def mini_calculator(num1, num2, operation):
    if operation == 1:
        operation = "Addition"
        print(f"You choose {operation} Operation : ")
        return num1 + num2
    
    elif operation == 2:
        operation = "Substraction"
        print(f"You choose {operation} Operation : ")
        return num1 - num2
    
    elif operation == 3:
        operation = "Division"
        print(f"You choose {operation} Operation : ")
        return num1 / num2
    
    elif operation == 4:
        operation = "Multiplication"
        print(f"You choose {operation} Operation : ")
        return num1 * num2
    
    else:
        print("Enter option between 1-4")
    


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("\n==== CHOOSE OPTION FOR OPERARION ====")
print("1 - For Addition")
print("2 - For Subtraction")
print("3 - For Division")
print("4 - For Multiplication\n")
c = int(input("Enter your choice : "))

result = mini_calculator(a, b, operation=c)
print("The result is :", result)


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

def func1():
    a = 123
    print(a)
    
def func2():
    a = 456
    print(a)


func1()
func2()




# 22. Create a global variable representing a counter. Create a function that reads and displays its value without creating another variable with the same name.

counter = 0

def test():
    print(counter)

test()




# 23. Create a program with a global variable called name and a function containing a local variable with the same name. Display both values from their respective scopes.

name = "Awais"
def demo():
    name = "John"
    print(name)


print(name)
demo()




# # 24. Create two functions that each have a local variable called message, but give the variables different values.

def fun1():
    message = "Hello world!"
    return message

def fun2():
    message = "Hello Awais!"
    return message


print(fun1())
print(fun2())




# 25. Create a function that receives a parameter called number and also contains another local variable. Use both inside the function.

def test(number):
    message = f"I pass the number {number} as argument"
    return message


print(test(12))


# <--------------------------- Level 4 — Mixed Challenges --------------------------->

# 26. Create a function that receives a student's name and three marks. Calculate the average and display the student's result.

def student_result(name, mark1, mark2, mark3):
    total_marks = mark1 + mark2 + mark3   
    average_marks = total_marks / 3
    print(f"{name} scored {average_marks} average marks")


student_result("Awais", 10, 20, 30)




# 27. Create a function that receives a product's name, price, and quantity. Calculate and display the total cost.

'''
Same as # 15
'''




# 28. Create a function that receives a person's age and determines whether they are a child, teenager, adult, or senior.

def age_meter(age):
    if age < 0:
        print("Invalid age")
    elif age <= 12:
        print("Your are : Child")
    elif age <= 19:
        print("Your are : Teenager")
    elif age <= 64:
        print("Your are : Adult")
    else:
        print("Your are : Senior")


age = int(input("Enter your age : "))

age_meter(age)




# 29. Create a function that receives a number and returns the sum of all numbers from 1 up to that number.

def sum_all(number):
    total_sum = 0
    
    for i in range(1, number + 1):
        total_sum += i

    return f"Sum of all numbers tell {number} is : {total_sum}"


number = int(input("Enter any number : "))

print(sum_all(number))




# 30. Create a function that receives a list of numbers and returns the largest number.

def find_largest(numbers):
    largest_number = numbers[0]

    for num in numbers:
        if num > largest_number:
            largest_number = num

    return largest_number


print("The largest number is :", find_largest([10, 20, 30]))




# 31. Create a function that receives a list of numbers and returns how many numbers are even.

def count_even_numbers(numbers):
    even_numbers = 0

    for num in numbers:
        if num % 2 == 0:
            even_numbers += 1

    return even_numbers


even_numbers = [1, 3, 5, 2, 70, 99]
print("There are", count_even_numbers(even_numbers), "even numbers in the list")




# 32. Create a function that receives a list of numbers and calculates their average.

def calculate_average(numbers):
    total_numbers = 0
    for num in numbers:
        total_numbers += num
    return total_numbers / len(numbers)


numbers = [1, 3, 5, 2, 70, 99]
print("The average of the list is :", calculate_average(numbers))




# 33. Create a function that receives a student's name and a list of marks. Display the student's name, highest mark, lowest mark, and average.

def student_result(name, marks):
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)
    
    print(f"Studnet : {name}")
    print(f"Highest mark : {highest}")
    print(f"Lowest mark : {lowest}")
    print(f"Average : {average}")


student_result("Awais", [50, 60, 70, 80, 90])




# 34. Create a function that receives a username and password and determines whether they match predefined login information stored outside the function.

correct_username = "admin"
correct_password = "admin123"

def auth(username, userpass):
    if username == correct_username:
        if userpass == correct_password:
            return "Login Successfull"
        else:
            return "Wrong Password"
    else:
        return "User not found"


user = input("Enter username : ")
password = input("Enter password : ")

result = auth(user, password)
print(result)




# 35. Create a program with a global variable representing a shop's discount percentage. Create a function that receives an item's price and calculates its discounted price.

shop_discount = 20
def discounted_price(prince):
    discount = prince * (shop_discount / 100)
    return prince - discount


print("Discounted Price : ", discounted_price(1000))



# <--------------------------- Harder Mixed Challenges --------------------------->

# 36. Create a function that receives a number and returns whether it is prime.

def check_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


print(check_prime(7)) 




# 37. Create a function that receives a number and calculates its factorial.

def calculate_factorial(number):
    factorial = 1
    
    if number < 0:
        return "Invalid number"

    for n in range(number, 0, -1):
        factorial *= n
    return factorial


print(calculate_factorial(10))




# 38. Create a function that receives a list and a value, then determines how many times that value appears in the list.

def count_value(number, numbers):
    count = 0

    for n in numbers:
        if n == number:
            count += 1
    return count


print(count_value(1, [1, 2, 3, 4, 1, 1, 1]))




# 39. Create a function that receives two lists and returns the elements that appear in both lists.

def same_values(list1, list2):
    common = []
    
    for i in list1:
        for j in list2:
            unique_element = i not in common
            if i == j and unique_element:
                common.append(i)
    return common


a = [1, 2, 3, 4, 5, 9, 10]
b = [4, 5, 6, 7, 10, 1, 3, 4, 2, 3, 4, 6, ]

print(same_values(a, b))




# 40. Create a function that receives a dictionary containing student names and marks, then determines which student has the highest marks.

def student_result(students):
    highest_marks = students["Ali"]
    
    for name, marks in students.items():
        if marks > highest_marks:
            highest_marks = marks
            student_name = name
            
    print(f"{student_name} obtained the highest marks : {highest_marks}")


students = {
    "Ali": 85,
    "Sara": 99,
    "Ahmed": 98,
    "Zain": 95
}

student_result(students)




# 41. Create a function that receives a sentence and counts how many words it contains.

def count_words(sentence):
    words = sentence.split()
    return len(words)


description = "python is easy and python is powerful"

print("There are", count_words(description), "words in this sentence.")




# 42. Create a function that receives a sentence and returns the number of unique words using a set.

def count_unique_words(sentence):
    count = 0
    unique_words = set(sentence.split())
    return len(unique_words)


description = "Python is good and Python is great"

print("There are", count_unique_words(description), "unique words in this sentence.")




# 43. Create a function that receives a list of numbers and returns a new list containing only the even numbers.

def even_filter(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(even_filter(numbers_list))




# 44. Create a function that receives a list of numbers and returns a new list containing only numbers greater than 50.

def larger_numbers(numbers):
    new_list = []
    for number in numbers:
        if number > 50:
            new_list.append(number)
    return new_list


numbers_list = [101, 22, 83, 74, 95, 36, 47, 18, 90]

print(larger_numbers(numbers_list))




# 45. Create a function that receives student information through parameters and uses a global variable for the passing-mark requirement.

passing_mark = 50

def student_result(name, marks):
    if marks >= passing_mark:
        print(f"{name} Passed.")
    else:
        print(f"{name} Failed!.")


student_result("Ali", 50)




# <--------------------------- Final Mixed Challenges --------------------------->

# 46. Build a small student grading program using functions. Use parameters for student information, a global variable for the passing threshold, and local variables for calculations.

passing_marks = 50

def grading_system(students):
    for name, marks in students.items():
        status = ("Passed" if marks >= passing_marks else "Failed")

        if marks >= 85:
            print(f"{name} : {status} and got A+ Grade")
        elif marks >= 80:
            print(f"{name} : {status} and got A Grade")
        elif marks >= 70:
            print(f"{name} : {status} and got B Grade")
        elif marks >= 60:
            print(f"{name} : {status} and got C Grade")
        elif marks >= 50:
            print(f"{name} : {status} and got D Grade")
        else:
            print(f"{name} : {status}!. Try Hard :)")


students = {
    "Ali" : 83,
    "Sara" : 38,
    "Zain" : 98,
    "John" : 18,
    "Bakar" : 76,
    "Fakhar" : 58

}

grading_system(students)




# 47. Build a simple shopping-bill program using separate functions for calculating subtotal, discount, and final price.

def subtotal(price, quantity):
    return  price * quantity


def discount(subtotal_price):
    discount_rate = 10 / 100
    
    if subtotal_price >= 5000:
        return subtotal_price * discount_rate
    else:
        return 0


def final_price(subtotal_price, discount_amount):
    return subtotal_price - discount_amount 


price = 2000
quantity = 3

# Subtotal
subtotal_result = subtotal(price, quantity)

# Discoumt
discount_result = discount(subtotal_result)

# Final Price
final_result = final_price(subtotal_result, discount_result)


print("Subtotal :", subtotal_result)
print("Discount :", discount_result)
print("Final Price :", final_result)




# 48. Build a simple calculator using functions for addition, subtraction, multiplication, and division. Pass the required values as arguments.

'''
Same as # 18
'''




# 49. Build a number-analysis program where a function receives a number and determines whether it is positive/negative, even/odd, and prime/not prime.

def check_positive_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_prime(number):
    if number < 2:
        return "Not Prime"

    for n in range(2, number):
        if number % n == 0:
            return "Not Prime"

    return "Prime"


number = int(input("Enter a number: "))

print(f"{number} is {check_positive_negative(number)}, {check_even_odd(number)} and {check_prime(number)} number.")




# 50. Build a small student database using a dictionary and functions. Create functions for adding a student, finding a student's marks, calculating the average, and finding the highest-scoring student.

students = {}

def add_student(name, marks):
    students[name] = marks


def find_marks(name):
    if name in students:
        return students[name]
    return "Student not found"


def calculate_average():
    if not students:
        return 0

    total = 0
    for marks in students.values():
        total += marks
    
    return total / len(students)


def highest_student():
    if not students:
        return "No student found"
    
    highest_marks = 0
    highest_name = ""
    
    for name, marks in students.items():
        if marks > highest_marks:
            highest_marks = marks
            highest_name = name
            
    return highest_name, highest_marks


# Add students
add_student("Ali", 56)
add_student("Sara", 89)
add_student("Zain", 39)
add_student("Awais", 67)

# Find marks
print("Zain's marks :", find_marks("Zain"))

# Calculate Average
print("Class average :", calculate_average())

# Highest-scoring Student
name, marks = highest_student()
print("Highest-scoring student :", name)
print("Marks :", marks)

# <--------------------------- Basic Level --------------------------->

# 1. Accessing tuple elements
colors = ("red", "green", "blue", "yellow", "black")
# Print:
# first element
print("The first element is:", colors[0])
# # last element
print("The last element is:", colors[-1])
# # third element
print("The third element is:", colors[2])
# # second-last element
print("The second-last element is:", colors[-2])


# 2. Tuple slicing
numbers = (10, 20, 30, 40, 50, 60, 70)
# Print:
# first 3 elements
print("The first 3 elements are:", numbers[0:3])
# # last 3 elements
print("The last 3 elements are:", numbers[-1:-4:-1])
# # elements from index 2 to 5
print("The elements from index 2 to 5 are:", numbers[2:6])
# # reversed tuple using slicing
print("Reversed tuple:", numbers[::-1])


# 3. Count and index
numbers = (10, 20, 30, 20, 40, 20, 50)
# Find:
# how many times 20 occurs
print("20 occurs", numbers.count(20), "times in a given tuple")
# the index of the first 40
print("The first 40 is at", numbers.index(40), "index number")



# 4. Check membership
languages = ("Python", "Java", "C++", "JavaScript")
# Check whether:
# "Python" exists
print("YES, Python exists" if "Python" in languages else "No, Python doesn't exists")
# "Ruby" exists
print("YES, Ruby exists" if "Ruby" in languages else "NO, Ruby doesn't exists")



# 5. Basic unpacking
student = ("Ali", 20, "Computer Science")
# Unpack this tuple into three variables:
# name
# age
# department
# Then print them.
(name, age, department) = student
print(name)
print(age)
print(department)


# 6. Swapping variables
# Use tuple unpacking to swap:
a = 10
b = 20
(a, b) = b, a
print(a)
print(b)
# Expected:
# a = 20
# b = 10
# Don't use a third variable.



# 7. Extended unpacking
numbers = (1, 2, 3, 4, 5, 6)
# Use unpacking to get:
# first = 1
# middle = [2, 3, 4, 5]
# last = 6
(first, *middle, last) = numbers
print(first)
print(middle)
print(last)
# Hint: * can be used during unpacking.




# <--------------------------- Challenges --------------------------->

# 8. Nested tuples
students = (
    ("Ali", 20),
    ("Sara", 19),
    ("Ahmed", 21)
)
# Print:
# Ali is 20 years old
# Sara is 19 years old
# Ahmed is 21 years old
for student in students:
    (name, year) = student
    print(name + " is", year, "years old")
# Use a loop.


# 9. Find the largest
numbers = (23, 56, 12, 89, 34, 67)
# Find the largest number without using max().
largest_number = numbers[0]
for number in numbers:
    if largest_number < number:
        largest_number = number

print("The largest number is", largest_number)


# 10. Tuple → List → Tuple
numbers = (10, 20, 30, 40)
# # Convert it to a list.
new_list = list(numbers)
# # Add 50.
new_list.append(50)
# # Convert it back to a tuple.
numbers = tuple(new_list)
# # Print the final tuple.
print(numbers)

# Expected:
# (10, 20, 30, 40, 50)


# 11. Understand immutability
# What happens when you run this?
numbers = (10, 20, 30)
# numbers[1] = 100
# Don't just tell me the error name. Explain why the error occurs.
'''
Answer: Since tuples are immutable, meaning once tuple is created we cannot add/remove/change
elements into the tuple.In above program we are trying to change the value of 1 index number element in given tuple.
But we cannot change the tuple. That's why we get an error
'''





# <--------------------------- Mini Project --------------------------->
# Create a tuple containing information about a book:
book = ("Python Basics", "John Smith", 350, 2024)

# Represent:
# title, author, pages, year

# Then unpack the tuple and print a properly formatted description.
(title, author, pages, year) = book
print(f"{title} is the ultimate introductory guide written by industry expert {author}. Published in {year}, this comprehensive {pages}-page book breaks down complex coding concepts into simple, actionable lessons perfect for beginners looking to master the fundamentals of programming.")

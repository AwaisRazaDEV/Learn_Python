
# <--------------------------- Basic Level --------------------------->

# 1. Accessing tuple elements
colors = ("red", "green", "blue", "yellow", "black")
# Print:
# first element
# last element
# third element
# second-last element


# 2. Tuple slicing
numbers = (10, 20, 30, 40, 50, 60, 70)
# Print:
# first 3 elements
# last 3 elements
# elements from index 2 to 5
# reversed tuple using slicing


# 3. Count and index
numbers = (10, 20, 30, 20, 40, 20, 50)
# Find:
# how many times 20 occurs
# the index of the first 40


# 4. Check membership
languages = ("Python", "Java", "C++", "JavaScript")
# Check whether:
# "Python" exists
# "Ruby" exists


# 5. Basic unpacking
student = ("Ali", 20, "Computer Science")
# Unpack this tuple into three variables:
# name
# age
# department
# Then print them.


# 6. Swapping variables
# Use tuple unpacking to swap:
a = 10
b = 20
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
# Use a loop.


# 9. Find the largest
numbers = (23, 56, 12, 89, 34, 67)
# Find the largest number without using max().


# 10. Tuple → List → Tuple
numbers = (10, 20, 30, 40)
# Convert it to a list.
# Add 50.
# Convert it back to a tuple.
# Print the final tuple.

# Expected:
# (10, 20, 30, 40, 50)


# 11. Understand immutability
# What happens when you run this?
numbers = (10, 20, 30)
# numbers[1] = 100
# Don't just tell me the error name. Explain why the error occurs.





# <--------------------------- Mini Project --------------------------->
# Create a tuple containing information about a book:
book = ("Python Basics", "John Smith", 350, 2024)

# Represent:
# title, author, pages, year

# Then unpack the tuple and print a properly formatted description.
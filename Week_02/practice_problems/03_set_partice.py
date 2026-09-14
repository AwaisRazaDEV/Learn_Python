
# <--------------------------- Basic Level --------------------------->

# 1. Creating a set
# Create a set containing:
# 10, 20, 30, 40, 50
# Then print the set.


# 2. Duplicates
# What will be the output?
numbers = {10, 20, 20, 30, 30, 30, 40}
print(numbers)
# Explain why.


# 3. Membership
languages = {"Python", "Java", "C++", "JavaScript"}
# Check whether:
# "Python" exists
# "Ruby" exists
# "C++" exists


# 4. Add and remove
fruits = {"apple", "banana", "mango"}
# Add "orange"
# Remove "banana"
# Add "grapes"
# Print the final set.


# 5. Union
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Find the union of A and B.

# Expected:
# {1, 2, 3, 4, 5, 6}


# 6. Intersection
# Using the same sets, find the elements that exist in both sets.

# Expected:
# {3, 4}


# 7. Difference
# Find:
# A - B
# B - A
# What is the difference between the two results?


# 8. Symmetric difference
# Using:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Find the elements that are present in one set but not both.

# Expected:
# {1, 2, 5, 6}





# <--------------------------- Challenges --------------------------->

# 9. Remove duplicates using a set
# Given:
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
# Use a set to remove duplicates.


# 10. Common elements
# Given:
students_math = {"Ali", "Ahmed", "Sara", "Usman"}
students_science = {"Sara", "Usman", "Ayesha", "Hamza"}
# Find the students who study both Math and Science.


# 11. Unique words
# Given:
sentence = "python is easy and python is powerful"
# Create a set containing all unique words.

# Expected conceptually:
# {"python", "is", "easy", "and", "powerful"}

# Hint: .split() may help.
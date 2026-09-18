
# <--------------------------- Basic Level --------------------------->

# 1. Creating a set
# Create a set containing:
# 10, 20, 30, 40, 50
# Then print the set.
numbers = {10, 20, 30, 40, 50}
print("First Set :", numbers)


# 2. Duplicates
# What will be the output?
numbers = {10, 20, 20, 30, 30, 30, 40}
print(numbers)
# Explain why.
# Ans: When we print the set, the duplicates in this set are not printed because dupliates are not allowed in sets. 


# 3. Membership
languages = {"Python", "Java", "C++", "JavaScript"}
# Check whether:
# "Python" exists
print("YES, Python exists" if "Python" in languages else "NO, Python doesn't exist")
# "Ruby" exists
print("YES, Ruby exists" if "Ruby" in languages else "NO, Ruby doesn't exist")
# "C++" exists
print("YES, C++ exists" if "C++" in languages else "NO, C++ doesn't exist")


# 4. Add and remove
fruits = {"apple", "banana", "mango"}
# Add "orange"
fruits.add("orange")
# Remove "banana"
fruits.remove("banana")
# Add "grapes"
fruits.add("grapes")
# Print the final set.
print(fruits)


# 5. Union
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Find the union of A and B.
result = A | B
# result = A.union(B)
print("Unioin is :", result)

# Expected:
# {1, 2, 3, 4, 5, 6}


# 6. Intersection
# Using the same sets, find the elements that exist in both sets.
# result = A.intersection(B)
result = A & B
print("Intersection is :", result)
# Expected:
# {3, 4}


# 7. Difference
# Find:
# A - B
# B - A
# What is the difference between the two results?
a_diff_b = A - B
b_diff_a = B - A
print("A - B is :", a_diff_b)     # We get members of A which are different from B
print("B - A is :", b_diff_a)     # We get members of B which are different from A


# 8. Symmetric difference
# Using:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Find the elements that are present in one set but not both.
result = A ^ B
print("Symmetric difference :", result)

# Expected:
# {1, 2, 5, 6}





# <--------------------------- Challenges --------------------------->

# 9. Remove duplicates using a set
# Given:
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
# Use a set to remove duplicates.
new_set = set(numbers)
print(new_set)


# 10. Common elements
# Given:
students_math = {"Ali", "Ahmed", "Sara", "Usman"}
students_science = {"Sara", "Usman", "Ayesha", "Hamza"}
# Find the students who study both Math and Science.
both_subjects = students_math & students_science
print("These students have both subjects :", both_subjects)

# 11. Unique words
# Given:
sentence = "python is easy and python is powerful"
# Create a set containing all unique words.
unique_words = set(sentence.split())
print(unique_words)

# Expected conceptually:
# {"python", "is", "easy", "and", "powerful"}

# Hint: .split() may help.
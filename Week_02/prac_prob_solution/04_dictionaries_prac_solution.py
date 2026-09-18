
# <--------------------------- Basic Level --------------------------->

# 1. Create a dictionary
# Create a dictionary representing a student:
# name → Ali
# age → 20
# department → CS
# Print the dictionary.
# student = {
#     "name"  :   "Ali",
#     "age"  :   20,
#     "deparment"  :   "CS"
# }
# print(student)

# 2. Access values
# Given:
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}
# Print:
# student's name
print(student["name"])
# student's age
print(student["age"])
# student's marks
print(student["marks"])


# 3. Modify values
# Given:
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}
# Change:
# age → 21
student["age"] = 21
# marks → 90
student.update({"marks" : 90})


# 4. Add a new key
# Add:
# "city" → "Lahore"
# to the dictionary.
student.update({"city" : "Lahore"})
print("City added :", student)


# 5. Delete a key
# Given:
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85,
    "city": "Lahore"
}
# Remove "city".
student.pop("city")
print("City Removed :", student)


# 6. Check if a key exists
# Given:
person = {
    "name": "Ahmed",
    "age": 22,
    "city": "Islamabad"
}
# Check whether:
# "name" exists
print("Yes, name exists" if "name" in person else "NO, name doesn't exists")
# "email" exists
print("Yes, email exists" if "email" in person else "NO, email doesn't exists")


# 7. Get keys and values
# Given:
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}
# Print all the keys and then all the values.
for key in car.keys():
    print("key :", key)

for value in car.values():
    print("Value :", value)


# 8. Using .items()
# Given:
student = {
    "name": "Sara",
    "age": 19,
    "marks": 92
}
# Use a loop with .items() to print:
# name : Sara
# age : 19
# marks : 92
for key, value in student.items():
    print(key + " : ", value)


# 9. Find the highest marks
# Given:
marks = {
    "Ali": 78,
    "Sara": 92,
    "Ahmed": 85,
    "Usman": 88
}
# Find the student with the highest marks.
# Don't use max().
max_number = 0
for key, mark in marks.items():
    if max_number < mark:
        max_number = mark
        student = key

print(f"{student} Obtained Highest marks : {max_number}")


# 10. Count characters
# Given:
word = "banana"
# Create a dictionary that counts how many times each character appears.

# Expected:
# {
#     "b": 1,
#     "a": 3,
#     "n": 2
# }


# 11. Count words
# Given:
sentence = "apple banana apple orange banana apple"
# Create a dictionary that counts each word.

# Expected:
# {
#     "apple": 3,
#     "banana": 2,
#     "orange": 1
# }





# <--------------------------- Challenges --------------------------->

# 12. Student database
students = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Usman": 88
}
# Write a program that:
# Prints all students
# Prints their marks
# Calculates the average marks
# Finds the highest marks
# Counts how many students scored 80+


# 13. Nested dictionary
students = {
    "Ali": {
        "age": 20,
        "marks": 85
    },
    "Sara": {
        "age": 19,
        "marks": 92
    }
}
# Print:
# Ali is 20 years old and scored 85
# Sara is 19 years old and scored 92

# Use a loop.

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
this_dict = {}

for character in word:
    if character not in this_dict:
        this_dict[character] = 1
    else:
        this_dict[character] += 1

print(this_dict)

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
words = {}

for word in sentence.split():
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

print(words)

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
total_marks = 0
highest_marks = 0
good_students = 0

print("\nStudents are :")
for name in students.keys():
    print("->", name)

print("\nMarks are :")
# Prints their marks
for marks in students.values():
    print("->", marks)
    
# Calculates the average marks
    total_marks += marks
    
    if highest_marks < marks:
        highest_marks = marks
        
    if marks > 80:
        good_students += 1

average_marks = total_marks / len(students)
print("\nAverage marks are :", average_marks)

# Finds the highest marks
print("\nHighest marks are :", highest_marks)

# Counts how many students scored 80+
print(f"\nOut of {len(students)} students, {good_students} students scored 80+ marks.\n")


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

for name, about in students.items():
    print(f"{name} is {about['age']} years old and scored {about['marks']}")

# Use a loop.

# <--------------------------- Basic Level --------------------------->

# 1. Accessing elements:
numbers = [10, 20, 30, 40, 50]
# # Print:
# # the first element
print("First element:", numbers[0])
# # the last element
print("Last element:", numbers[-1])
# # the third element
print("Third element:", numbers[2])
# # the second-last element 
print("Second-last element:", numbers[-2]) 


# 2. Slicing
fruits = ["apple", "banana", "mango", "orange", "grapes", "kiwi"]
# # Print:
# # the first 3 fruits
print(fruits[0:3])
# # the last 3 fruits
print(fruits[-1:-4:-1])
# # every second fruit
print(fruits[1::2])
# # the list in reverse order
print(fruits[::-1])
# print(fruits.reverse())   # Also


# 3. Modifying a list
numbers = [5, 10, 15, 20, 25]
# # Change 15 to 100
numbers[2] = 100
# # Change the last element to 500
numbers[-1] = 500
# # Print the final list
print(numbers)


# 4. Adding elements
students = ["Ali", "Ahmed", "Sara"]
# # Add "Usman" to the end
students.append("Usman")
# # Add "Ayesha" at index 1
students.insert(1, "Ayesha")
# # Print the list
print(students)


# # 5. Removing elements
cities = ["Lahore", "Karachi", "Islamabad", "Multan", "Peshawar"]
# # Remove:
# # "Multan"
cities.remove("Multan")
# # the first element
cities.pop(0)
# # the last element
cities.pop(-1)
# # Print the list after each operation.
print(cities)


# 6. Searching
numbers = [12, 45, 67, 23, 89, 45, 10]
# # Write a program that:
# # checks whether 67 exists
exist_67 = "YES, 67 exists" if 67 in numbers else "NO, 67 doesn't exists"
print(exist_67)
# # checks whether 100 exists
exist_100 = "YES, 100 exists" if 100 in numbers else "NO, 100 doesn't exists"
print(exist_100)
# # finds how many times 45 occurs
duplicate_45 = numbers.count(45)
print(f"45 occures {duplicate_45} times")


# 7. Sum of numbers
numbers = [10, 20, 30, 40, 50]
# # Calculate the sum using a loop, without using sum().
total_sum = 0
for number in numbers:
    total_sum += number
print("Total Sum is:", total_sum)


# 8. Find the largest number
numbers = [23, 67, 12, 89, 34, 56]
# # Find the largest number without using max().
max_num = numbers[0]
for number in numbers:
    if max_num < number:
        max_num = number

print("The maximum number in list is:", max_num)


# 9. Count even numbers
numbers = [12, 7, 9, 20, 33, 44, 51, 60]
# # Count how many even numbers are present.
even_nums = []
for number in numbers:
    if number % 2 == 0:
        # print(number)
        even_nums.append(number)
# print(even_nums)
print("There are", len(even_nums), "even numbers in a given list")


# 10. Create a new list
numbers = [1, 2, 3, 4, 5, 6]
# Create a new list containing the squares:
# [1, 4, 9, 16, 25, 36]
# Try solving it using a for loop.
squared_list = []
for number in numbers:
    squared_list.append(number ** 2)

print("Squared List:", squared_list)




# <--------------------------- Challenge --------------------------->

# 11. Remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5, 2, 6, 3]
# Create a new list without duplicates.
# Expected:
# [1, 2, 3, 4, 5, 6]
# Don't use set().
new_list = []
for number in numbers:
    if number not in new_list:
        new_list.append(number)

print("Without Duplication:", new_list)


# 12. Second largest
numbers = [10, 45, 23, 89, 67, 89, 34]
# Find the second-largest unique number.
# Expected:
# 67
largest_number = 0
second_largest = 0
for number in numbers:
    if largest_number < number:
        second_largest = largest_number
        largest_number = number
    elif second_largest < number < largest_number:
        second_largest = number
print("Second largest number is:", second_largest)


# 13. Reverse without reverse()
numbers = [1, 2, 3, 4, 5]
# Create a reversed list:
# [5, 4, 3, 2, 1]
# Don't use .reverse() or [::-1].
new_list = []
for number in numbers:
    new_list.insert(0, number)

print("Reversed List:", new_list)
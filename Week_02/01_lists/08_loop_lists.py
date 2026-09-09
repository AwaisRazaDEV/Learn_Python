
# <-------------------- Loop through the for loop -------------------->

fruits = ["apple", "banana", "mango", "peach", "grapes"]
for fruit in fruits:
    print(fruit)


# <-------------------- Loop through the index number -------------------->
# You can also loop through the list items by referring to their index number.
# with the help of range() and len()

colors = ["red", "blue", "yellow"]
for i in range(len(colors)):
    print(colors[i])


# <-------------------- Loop through the while loop -------------------->
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
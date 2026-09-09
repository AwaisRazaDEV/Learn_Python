
'''
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:
'''

# Without list Comprehension
fruits = ["apple", "banana", "grapes", "cherry", "kiwi", "banana"]
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)
        
print(new_list)

# With List Comprehension
my_list = [i for i in fruits if "a" not in i]
print(my_list)

thislist = [a if a != "banana" else "orange" for a in fruits]
print(thislist)
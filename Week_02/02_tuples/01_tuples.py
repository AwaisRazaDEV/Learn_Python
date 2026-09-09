
# Tuples are used to store multiple items of same or different data-type in a single variable.

# Tuples are written with round brackets.

fruits =  ("apple", "banana", "mango", "grapes")

# Tuples can also be created without the parentheses:
this_tuple = 1, "awais", 3.14, True
# for i in this_tuple:
#     print(i, type(i))

'''
Tuple items are ordered, unchangeable, and allow duplicate values.

(Ordered) : When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

(Unchangealbe) : Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

(Allow Duplicate) : Since tuples are indexed, they can have items with the same value.
'''

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

single_tuple = ("HTML", )
print(type(single_tuple))

# To create an empty tuple, use round brackets with no content.

empty_tuple = ()
print(type(empty_tuple))


# <-----------  Tuple Length  ----------->
# Use len() function to determine the lenght of items in tuple.

print(len(fruits))


# <----------- tuple() Constructor ----------->
# We can also create a tuple using tuple() constructor.

color = tuple(("red", "blue", "green", "yellow"))
print(color)







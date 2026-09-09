
# Lists are used to store multiple items/values of same or different data type in a single variable.Lists are created by using square brackets:

fruits = ["Mango", "Apple", "Grapes", "Cherry", "Banana"]
x = ["Awais", 999, 3.14, True]

'''
List items are ordered, changeable, and allow duplicate values.

( Ordered ) : When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
( ! There are some list methods that will change the order, but in general: the order of the items will not change.)

( Changeable ) : The list is changeable, meaning that we can change, add and remove items in a list after it have been created.

( Allow Duplicates ): Since lists are indexed, lists can have items with the same value.
'''

# <-----------  List Length  ----------->
# Use len() function to determine the lenght of items in list.

print(len(fruits))

#  <----------- list() Constructor ----------->
# We can also create a list using list() constructor.

color = list(("red", "blue", "green", "yellow"))
print(color)

# Sets are used to store multiple items of same or different data-type in a single variable.

# Sets are written with curly brackets.

fruits =  {"apple", "banana", "mango", "grapes"}

'''
Set items are unordered, unchangeable, and do not allow duplicate values.

(Unordered) : Set items do not have a defined order,they apperars in a different order everytime we use then and cannot refered to by index or key.

(Unchangealbe) : Sets items are unchangeable, meaning that we cannot change the items after the set has been created but we can add or remove the items.

(Duplicate Not Allow) : Sets cannot have two items with the same value.

'''

# The values ( True and 1 ) and ( False and 0 ) are considered the same value in sets, and are treated as duplicates:

this_set = {True, 0, 1, False, "awais", 2}
print(this_set)



# <-----------  Set Length  ----------->
# Use len() function to determine the lenght of items in Set.

print(len(this_set))



# <----------- set() Constructor ----------->
# We can also create a sest using set() constructor.

color = set(("red", "blue", "green", "yellow"))
print(color)







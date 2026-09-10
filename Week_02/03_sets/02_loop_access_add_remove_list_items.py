
# <------------------- Access Set Items(using for loop) ------------------->
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop

this_set = {"apple", "mango", True, 0}
for x in this_set:
    print(x)

# Once a set is created, you cannot change its items, but you can add new items.


# <------------------- Add items ------------------->
# To add one item to a set use the add() method.

this_set.add(3.14)
print(this_set)


# <------------------- Remove items ------------------->
# To remove an item in a set, use the remove(), or the discard() method.

this_set.remove("apple")
this_set.discard("cherry")
print(this_set)

# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will raise an error.

'''
We can also use these methods:
pop()           It removes the first item
clear()         It empties the set
del keyword     To remove the item and also use to remove the set completely(this will raise an error)
'''



# There are several ways to join two or more sets in Python.


# <-------------------- Union, Intersection, Difference, symmetric_difference -------------------->
set1 = {"apple", "bnana"}
set2 = {1, 2, 4,}
set3 = {"google", "amazon", "apple"}

# The union() methods joins all items from both sets:
result = set1.union(set2)     # Union
# result = set1 | set2     # by using | operation
print("Union:", result)


# The intersection() method keeps ONLY the duplicates:
result = set1.intersection(set3)     # Intersection
# result = set1 & set3    # by using & operation
print("Intersection:", result)


# The difference() method keeps the items from the first set that are not in the other set(s):
result = set1.difference(set3)     # Difference
# result = set1 - set3     # by using - operation
print("Difference:", result)


# The symmetric_difference() method keeps all items EXCEPT the duplicates:
result = set1.symmetric_difference(set3)     # symetric_difference
# result = set1 ^ set3     # by using ^ operation
print("Symmetic Difference:", result)



# We can also join multiple sets:
set4 = set1 | set2| set3
set4 = set1.union(set1, set2, set3)   #same as above
print(set4)
# we can do same with (& or intersection), (- or difference) and (^ or symmetric_difference)


# The  |, &, - and ^ operators only allows you to join sets with sets, and not with other data types like you can with the  union(), interserction(), difference() and symmetric_difference() methods.
x = ("red", "blue", "green", True)
# y = set2.union(x)
# y = set2.intersection(x)
# y = set2.difference(x)
y = set2.symmetric_difference(x)
print(y)



# <-------------------- Update, intersectioin_update(), difference_update(), symmetric_difference_update() -------------------->
# All of these methods will change the original set instead of returning a new set.


# The update() method inserts all items from one set into another.
set1.update(set3)
print("Update:", set1)


# The intersection_update() method will also keep ONLY the duplicates.
set1.intersection_update(set3)
print("Intersection Update:", set1)


# The difference_update() method will keep the items from the first set that are not in the other set.
set1.difference_update(set3)
print("Difference Update:", set1)


# The symmetric_difference_update() method will also keep all but the duplicates.
set1.symmetric_difference(set3)
print("Symmetric Differece Update:", set1)


# Key Points:
# The values True and 1 are considered the same value. The same goes for False and 0.
# Both union() and update() will exclude any duplicate items.

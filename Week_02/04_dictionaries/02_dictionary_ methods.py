
# <--------------------- Access Items --------------------->

# 1. We can access the items of the dictionary by referring to its key name, inside square brackets:
person1 = {
    "name" : "John",
    "age"  : 30,
    "country" : "USA"
}
print(person1["age"])
# This can also be done by using get() method which returns the value of the specified key:
x = person1.get("name")
print(x)


# 2. The keys() method will return a list of all the keys in the dictionary.
keys = person1.keys()
print(keys)


# 3. The values() method will return a list of all the values in the dictionary.
values = person1.values()
print(values)


# 4. The items() method will return each item in a dictionary, as tuples in a list.
items = person1.items()
print(items)



# <--------------------- Update Items --------------------->

# 1. You can change the value of a specific item by referring to its key name:
person1["age"] = 31
print("Updage Age:", person1)

# 2. update() method Updates the dictionary with the specific key-value pairs:
person1.update({"country": "Canada"})
print("Update country:", person1)
# The argument must be a dictionary, or an iterable object with key:value pairs.


# <--------------------- Add Items --------------------->

# 1. Adding an item to the dictionary is done by using a new index key and assigning a value to it:
person1["subject"] = "physics"
print("Add Subject:", person1)

# 2. We can also use update() method:
person1.update({"grades" : 75})
print("Add Grades:", person1)


# <--------------------- Remove Items --------------------->
# There are several way to remove items from a dictionary

# 1. The pop() method removes the item with the specified key name:
person1.pop("country")
person1.popitem()       # Removes the last inserted item
print("Remove Country:", person1)

# 2. The del keyword removes the item with the specified key name:
del person1["subject"]
# del person1     # this will delete list completey(which raise an error)
print(person1)

# 3. The clear() method empties the dictionary:
person1.clear()
print(person1)


# <--------------------- Copy Items --------------------->
# Make a copy of a dictionary with the copy() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# Another way to make a copy is to use the built-in function dict().
newdict = dict(person1)
person1.update({"name" : "James"})
print(newdict)
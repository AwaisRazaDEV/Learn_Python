
# Dictionaries are used to store data value in key:value pairs.

# Dictionaries are written wity curly brackets, and have key and values:

thisdict = {
    "brand" : "apple",
    "model" : "17 pro max",
    "year"  : 2025,
    "year"  : 2026
}

print(thisdict)

# Dictionary items are ordered, changeable, and do not allow duplicates.


# To determine how any items a dictionary has, use len() function:
print(len(thisdict))


# The values in dictionary items can be of any data type:

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}


# <------------- The dict() constructor ------------->
# It is also possible to use the dict() constructor to make a dictionary.

person1 = dict(name = "John", age = 25, country = "USA")
print(person1)



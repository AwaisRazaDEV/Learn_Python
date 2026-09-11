
# You can loop through a dictionary by using a for loop.

# Print all key names in the dictionary, one by one:
thisdict = {
    "name" : "John",
    "age"  : 20,
    "subject" : "math"
}
for key in thisdict:
    print(key)
# You can use the keys() method to return the keys of a dictionary:
for a in thisdict.values():
    print("By Using key() method:", a)



# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])
# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print("By Using vlaue() method:", x)



# Loop through both keys and values, by using the items() method:
for key, value in thisdict.items():
    print(key, ":", value)



# <------------------- Nested Dictionaries ------------------->
# A dictionary can contain dictionaries, this is called nested dictionaries.
members = {
    "person1" : {
    "name" : "zain",
    "year" : 2001
    },
    "person2" : {
        "name" : "ali",
        "year" : 2002
    },
    "person3" : {
        "name" : "waqas",
        "year" : 2003
    }
}
# You can loop through a dictionary by using the items() method like this:
for p, obj in members.items():
    print(p)
    for y in obj:
        print(y, ":", obj[y])
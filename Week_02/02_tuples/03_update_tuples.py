
'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround.You can convert:

    tuple --> list --> change the list(Update/add/remove) --> tuple
    
'''

# Change Tuple Value
this_tuple = ("apple", "mango", "banana", "grapes")
x = list(this_tuple)
x[3] = "cherry"
this_tuple = tuple(x)
print(this_tuple)

# Add Item
y = list(this_tuple)
y.append("pineapple")
new_tuple = tuple(y)
print(y)

# Remove Item
z = list(this_tuple)
z.remove("apple")
my_tuple = tuple(z)
print(my_tuple)


# <------------------ Copy Lists ------------------>
# You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2

this_list = ["Apple", "Banana", "Peach", "Grapes",]
# my_list = this_list
# this_list[2] = "Kiwi"
# print(this_list)
# print(my_list)      # This is wrong way to copy list

my_list = this_list.copy()
this_list[2] = "Kiwi"
print(this_list)
print(my_list)        # This is right way to copy list


# Another way to make a copy is to use the built-in method list().
my_list = list(this_list) 
this_list[2] = "Pineapple"
print(this_list)
print(my_list)  

# You can also make a copy of a list by using the : (slice) operator.
colors = ["red", "green", "yellow"]
my_colors = colors[:]
colors[0] = "black"
print(my_colors)
print(colors)


# <------------------ Join Two Lists ------------------>
# There are several ways to join, or concatenate, two or more lists in python.

# One of the easiest way are by useing the + operator.

numbers = [1, 2, 3, 4, 5]
new_list = colors + numbers
print(new_list)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
for x in colors:
    numbers.append(x)
    
print(numbers)

# We can also use the extend() method to join two lists
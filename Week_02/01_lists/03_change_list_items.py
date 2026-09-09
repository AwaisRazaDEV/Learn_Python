
# To change the value of specific item, we need to refer the index number.

fruits = ["Apple", "Mango", "Grapes", "Banana", "Peach", "Orange", "Kiwi"]
fruits[6] = "Cherry"
print(fruits)

# <------------------ Change a Range of Item Value ------------------>
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

fruits[1:3] = ["Watermelon", "Pineapple"]
print(fruits)


# Insert more items than you replace(i.e it will change the length of the list).

this_list = ["Apple", "Mango", "Banana"]
this_list[1:2] = ["Cherry", "Grapes"]
print(this_list)


# Insert less items than you replace(i.e it will change the length of the list).

new_list = ["Apple", "Cherry", "Grapes"]
new_list[0:2] = ["Mango"]
print(new_list)
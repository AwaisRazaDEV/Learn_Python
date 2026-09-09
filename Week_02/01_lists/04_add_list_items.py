
'''

There are three methods to add items in a list:
1. append()
2. insert()
3. extend()

'''

# <--------------- Append Items --------------->
# To add an items to the end of the list, we use the append() method:

fruits = ["Apple", "Mango", "Banana"]
fruits.append("Grapes")
print(fruits)


# <--------------- Insert Items --------------->
# To add an item at specifeid index, we use insert() method:

new_fruits = ["Cherry", "Pineapple", "Peach"]
new_fruits.insert(0, "Kiwi")
print(new_fruits)


# <--------------- Extend List Items --------------->
# To append elements from other list to the current list, we use the extend() mentho:

fruits.extend(new_fruits)
print(fruits)       # The element will be added at the end of the list


#       You can add any iterable object(turples, sets, dictonaries etc.)
this_list = ["red", "blue", "green"]
this_tuple = ("Apple", "berry", "Gavava")
this_list.extend(this_list)
print(this_list)
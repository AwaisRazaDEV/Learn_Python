
'''
There are three methods to remove list items:

1.remove()      Removes the items with specified value
2.pop()         Removes the element at the specified position
3.clear()       Removes all the elements form the list(i.e empties the list)

we also use del keyword to remove the specific index or delete the list completely(it will raise an error!)

'''

# <---------------- Remove Specific item ---------------->
fruits = ["apple", "kiwi", "mango", "grapes", "banana", "kiwi"] # Two time "kiwi"
fruits.remove("kiwi")  # remove the first occurence of "kiwi"
print(fruits)


# <---------------- Remove Specific Index ---------------->
fruits.pop(0)
fruits.pop()    # Empty pop() removes the last item in the list
print(fruits)


# <---------------- Clear the list ---------------->
new_list = ["red", "blue", "green", "black"]
new_list.clear()
print(new_list)


# <---------------- del Keyword ---------------->
colors = ["black", "white", "purple"]
del colors[0]
# del colors      # deletes the list completely
print(colors)
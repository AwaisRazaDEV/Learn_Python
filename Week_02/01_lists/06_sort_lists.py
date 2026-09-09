
# Using sort() method, we can sort the ilst alphanumerically and it will be ascending, by default:

alpha_list = ["A", "Z", "D", "K", "J", "T", "O"]
num_list = [50, 1, 99, 66, 34, 67, 22]

alpha_list.sort()   # Alphabetically
num_list.sort()     # Numberically

print(alpha_list)
print(num_list)


# <--------------- Sort Descending --------------->
# To sort descending, use the keyword argument reverse = True:

print("Sort Descending: ")

alpha_list.sort(reverse = True)
num_list.sort(reverse = True)

print(alpha_list)
print(num_list)


# <--------------- Case Insensitive Sort --------------->
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

new_list = ["a", "c", "B", "x", "Z", "s", "S"]
new_list.sort()
print(new_list)

'''
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:
'''
print("after case-Insensitive: ")
new_list.sort(key=str.lower)
print(new_list)

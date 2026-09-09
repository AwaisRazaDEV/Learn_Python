'''
Tuple items are indexed, you can access them through their index number:

The 1st item has index [0]
The 2nd item has index [1]
The 3rd item has index [2]
and so on .......
'''

fruits = ("Apple", "Mango", "Grapes", "Banana", "Peach")
print(fruits[3])

# <--------------  Negative Indexing  -------------->

'''
The negative indexing means start from the end

[-1] refers to the last item
[-2] refers to the second last item
and so on ......
'''

print(fruits[-3])

# <--------------  Range of Indexes  -------------->
# We can specify a range of indexes by specifying were to start and where to end the range.Also, it will give a new tuple

new_tuple = fruits[1:4]
print(new_tuple)

#    !       start:end:step  -->  (include)1:4(not include)

# By leaving out the start value, the range will start from the first item.

print(fruits[:4])

# By leaving out the end value, the range will go on to the last item.

print(fruits[2:])


# <--------------  Range of Negative Indexes  -------------->

print(fruits[-1:-4:-1])

# It inverse all the items on the tuple
print(fruits[::-1])

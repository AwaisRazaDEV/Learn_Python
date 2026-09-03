a = 10
x = 10

c = [1, 2, 3]
d = [1, 2, 3]

# IS Operator: "Returns Ture if both variables point to the same object"
print(c is d)

# IS NOT Operator: "Returns Ture if both variables point to the different object"
print(c is not d)

# <----- c is d (False) b/c, since variables are stored in temporary memory, each varaibles are stored in different memory location that's why it give False in output ----->

# ! ! ! ! But if two variales have same single value then python will shared their memory and it returns True as shown in example below: ! ! ! !

print( a is x)
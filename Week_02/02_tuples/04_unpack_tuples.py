
# When we create a turple, we normally assign values to it. This is called "packing" a tupel:

clothes = ("shirt", "pant", "cap")

# But, in python we are also allowed to extract the values back into variables. This is called "Unpacking":

(black, blue, grey) = clothes

print(black)
print(blue)
print(grey)


# <--------------- Using Asterik* --------------->

this_fruits = ("apple", "mango", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = this_fruits
print(green)
print(yellow)
print(red)
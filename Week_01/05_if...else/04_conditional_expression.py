
# <------------- Short Hand if ------------->

# If you have only one statement to execute, you can put it on the same line as the if statement

a = 10
b = 20

if a < b : print("a is smaller number")


# <------------- Short Hand if...else ------------->

# If you have one statement for if and one for else, you can put the in same line using conditional expression.

username = input("Enter username: ")

print(f"Hello {username}") if username else print("Guest")

# Another Example

x = input("Enter first number: ")
y = input("Enter second number: ")

x, y = int(x), int(y)
# print(type(x), type(y))

bigger = x if x > y else y
print("Bigger is", bigger)


#         (Conditional Expression also know as Ternary Operator)



# <------------- Elif Statement ------------->

# When you use elif, python evalutates the conditions from top to bottom as soon as it find a condition that is true, it execute that block and skips all reamaining conditions

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")

#           ( Use Elif when you have multiple condition to check )
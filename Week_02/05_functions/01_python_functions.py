
# A function is a resuable block or code that performs a specific task -- defined once and used as many times as you need

# In Python, a function is defined using the def keyword, followed by a function name and parentheses:
def greeting():
    print("Hello World!")
    
greeting()


# With functions - reusable code:
# Functions can send data back to the code that called them using the return statement.
def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
# When a function reaches a return statement, it stops executing and sends the result back:

temp = int(input("Enter temperature for F to C: "))
print(fahrenheit_to_celcius(temp))


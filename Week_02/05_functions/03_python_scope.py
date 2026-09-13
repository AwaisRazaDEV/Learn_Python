
# A variable is only available from inside the region it is created. This is called scope.


# <---------------- 1. Local Scope ---------------->
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def local_test():
    x = 10
    print(x)

local_test()
# print(x)    # Raise error b/c variable not defined



# <---------------- 2. Global Scope ---------------->
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
y = "Awais"
def global_test():
    print(y)

global_test()
print("Hi", y)



# <---------------- Nameing Varibles ---------------->
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
number = 5
def test_function():
    number = 10
    print("Local Varaible:", number)

test_function()
print("Global Variable:", number)



# <---------------- Global Keyword ---------------->
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
def myfunc():
    global x
    x = 300

myfunc()
print(x)
# Also, use the global keyword if you want to make a change to a global variable inside a function.




# <---------------- Nonlocal Keyword ---------------->
# The nonlocal keyword is used to work with variables inside nested functions.The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())
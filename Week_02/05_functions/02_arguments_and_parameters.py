
# <--------------------- Arguments vs Parameters --------------------->

# Parameters:
#            Variables defined inside the function are parameters. They act as placeholder waiting to receive a value.
def greet(name):
    # name is a parameter
    print("Hello, " + name)


# Argument:
#          The actual value you pass into the function when you call it.They fill in the parameter placeholder.
greet("awais")
# awais is the argument



# <--------------------- Working with arguments --------------------->

# 1. Default Arguments:
#                      Pre-set values used when the caller provides no arugument at all.
def my_country(country = "Pakistan"):
    print("I am from", country)

my_country("USA")
my_country()    #No Argument Passed 
my_country("Canada")


# 2. Keyword Arguments:
#                      You can send arguments with the key = value syntax.Arguments matched by the keys so order doesn't matter.
def student_detail(id, name, age, subject):
    student = {
        "id" : id,
        "name" : name,
        "age" : age,
        "subject" : subject
    }
    print(student)

student_detail(age= 23, name="Awais", subject="physics", id=1234)


# 3. Positional Arguments:
#                         When you call a function with arguments without using keywords, they are called positional arguments.
# Values matched by their position in the functon call. Order matters!
def full_name(fname, lname):
    print(f"Hi! My name is {fname} {lname}")

full_name("Awais", "Raza")




# <--------------------- return value --------------------->
# Functions can return values using the return statement:
def add(a, b):
    return a + b

result = add(2, 5)
print(result)




# <--------------------- positional-only and keyword-only --------------------->
# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)




# <--------------------- Python *args and **kwargs --------------------->
'''
By default, a function must be called with the correct number of arguments.

However, sometimes you may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept a unknown number of arguments.
'''

# Arbitrary Arguments - *args:
#                             If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly:
def greeting(greeting, *names):
    for name in names:
        print(greeting, name)

greeting("Hello", "Awais", "Ahmed", "Faisal", "Zain")



# Arbitrary Keyword Arguments - **kwargs:
#                                        If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly:
def user_detail(username, **detail):
    print("Username:", username)
    print("Additional Detail")
    for key, value in detail.items():
        print(key, ":", value)


user_detail("user123", age= 25, city= "ABC", hobby= "Programming")





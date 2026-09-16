'''
isalnum()       :   Returns True if all characters in the string are alphanumeric
isalpha()       :   Returns True if all characters in the string are in the alphabet
isdigit()       :   Returns True if all characters in the string are digits
islower()       :   Returns True if all characters in the string are lower case
isupper()       :   Returns True if all characters in the string are upper case
isspace()       :   Returns True if all characters in the string are whitespaces
center()        :   Returns a centered string
ljust()         :   Returns a left justified version of the string
rjust()         :   Returns a right justified version of the string
zfill()         :   Fills the string with a specified number of 0 values at the beginning
format()        :   Formats specified values in a string
format_map()    :   Formats specified values from a dictionary in a string
'''

# <---------------------- Practical ---------------------->

demo = "Python123"
print("isalnum method: ", demo.isalnum())

demo = "Python"
print("isalpha method: ", demo.isalpha())

demo = "123"
print("isdigit method: ", demo.isdigit())

demo = "admin"
print("islower method: ", demo.islower())

demo = "ADMIN"
print("isupper method: ", demo.isupper())

print("center method:", demo.center(30, "*"))    # 30 - words in string, then remaining number it divides the space in equal sides of the string

demo = "ADMIN"
print("ljust method: ", demo.ljust(20, "-"))

demo = "ADMIN"
print("rjust method: ", demo.rjust(20))

number = "99"
print("zfill method:", number.zfill(4))     # Can use for ID, invoice etc

name = "Zain"
age = 15
print("Name : {}, Age : {}".format(name, age))
print("Name : {1}, Age : {0}".format(name, age))
print("|{:^10}|".format("Python"))
print("|{:<10}|".format("Python"))
print("|{:>10}|".format("Python"))


student = {
    "name" : "zain",
    "age" : 10,
    "country" : "cananda"
}

result = "{name} is {age} years old and lived in {country}"
print(result.format_map(student))

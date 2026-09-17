'''
                        Common Build-in Exception
    ZeroDivisionError       ValueError                TypeError
    NameError               IndexError                KeyError
    AttributeError          FileNotFoundError         PermissionError
    ImportError             ModuleNotFoundError       RuntimeError
    AssertionError          MemoryError               RecursionError
    TimeoutError            NotImplementedError       UnicodeEncodeError
                            UnicodeDecodeError          
'''

# try:
#     num = int(input("Enter any number : "))
#     print(30 / num)

# except ZeroDivisionError:
#     print("Cannot divide by Zero")

# except ValueError:
#     print("Invalid Value")

# except Exception as e:
#     print("Error :", e)


# <------------------- Real Usage ------------------->
from pathlib import Path
file_path = Path(__file__).parent / "demofile.txt"

try:
    # The try block lets you test a block of code for errors.
    file =  open(file_path)

except Exception as e:
    # The except block lets you handle the error.
    print(e)

else:
    # The else block lets you execute code when there is no error.
    print(file.read())
    file.close()

finally:
    # The finally block lets you execute code, regardless of the result of the try- and except blocks.
    print("\nProgram Finished")




# <------------------- Raise an exception ------------------->
# As a Python developer you can choose to throw an exception if a condition occurs.
# The raise keyword is used to raise an exception.
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")


# You can define what kind of error to raise, and the text to print to the user.
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
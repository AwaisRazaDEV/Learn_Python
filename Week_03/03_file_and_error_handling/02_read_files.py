
# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file.
# It is a good practice to always close the file when you are done with it.By using close() method.

# By default at read mode -- If you do not pass "mode" in a open() function.Then its modes will be read only. Make sure the file exists, or else you will get an error.



# <----- To check current working directory

# import os
# print("Current folder:", os.getcwd())
# print("Files here:", os.listdir())

# ----->

# 1st Way:
# f = open("demofile.txt", "r")   # Since i'm currently working form python folder it could not finding this folder.

# 2nd Way:
file = open(r"E:\python\Week_03\03_file_and_error_handling\demofile.txt", "r")
# The r before the string is important on Windows because it treats \ as a normal character.

content = file.read()
print(content,"\n")

file.close()



# <------------------------ Using with statement ------------------------>
# By using with statement you do not have to worry about closing your files, the with statement takes care of that.


# 3rd Way:  Recomended + more Reliable
from pathlib import Path

file_path = Path(__file__).parent / "students.txt"
# Path(__file__) means your Python file: 02_read_files.py
# and Path(__file__).parent means: 03_file_and_error_handling

# So Python constructs: 03_file_and_error_handling/students.txt
with open(file_path) as f:
    # print(f.read())


# Read Only Parts of the File:
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
    # print("Read-Only Part : ", f.read(10),"\n")


# Read Lines:
# You can return one line by using the readline() method:
    # print(f.readline())
    # print(f.readline())     #By calling readline() two times, you can read the two first lines:

# Using readlines() method you can read all lines of your file, In the form of linst:
    # print(f.readlines())


# Using loop:
    for x in f:
        print(x.strip())

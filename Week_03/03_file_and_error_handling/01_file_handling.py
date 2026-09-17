'''
File handling in Python refers to the process of performing operations on a file, such as creating, opening, reading, writing, and closing it through code.

Unlike data stored in variables (RAM), which disappears when your program stops running, files allow you to store data permanently on a secondary storage device (like your hard disk).
'''

# The key function for working with files in Python is the open() function.The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists



In addition you can specify if the file should be handled as binary or text mode.

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''

# for example

# file = open("demofile.txt", "rt")
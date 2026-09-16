'''
lower()         :   Converts a string into lower case
upper()         :   Converts a string into upper case
title()         :   Converts the first character of each word to upper case
capitaliza()    :   Converts the first character to upper case
find()          :   Searches the string for a specified value and returns the position of where it was found
count()         :   Returns the number of times a specified value occurs in a string
startswith()    :   Returns true if the string starts with the specified value
endswith()      :   Returns true if the string ends with the specified value
strip()         :   Returns a trimmed version of the string
split()         :   Splits the string at the specified separator, and returns a list
join()          :   Joins the elements of an iterable to the end of the string
replace()       :   Returns a string where a specified value is replaced with a specified value
'''

# <---------------------- Practical ---------------------->

demo = "admin@gmail.com"
print("Lower method:", demo.lower())
print("Upper method:", demo.upper())
print("Title method:", demo.title())
print("Capitalize method:", demo.capitalize())
print("Find method:", demo.find("o", 3, 10))    # (str, start, stop).It is case-sensitive. -1 mean nothing found.
print("rFind method:", demo.rfind("i"))     # It start finding from right to left.
print("Count method:", demo.count("m"))    # (str, start, end) Also
print("Startswith method:", demo.startswith("admin"))    # (str, start, stop).It is case-sensitive.
print("Endswith method:", demo.endswith(".com"))    # (str, start, stop).It is case-sensitive.

# Real world use of startswith() and endswith() methods:
url = "https://google.com"
if url.startswith(("https://", "http://")):
    print("Valid URL")
else:
    print("Invalid URL")

media = "audio.mp3"         # Also for other media files (.png, .jpeg, .jpg etc)
if media.endswith(".mp3"):
    print("Valid mp3 file")
else:
    print("Invalid mp3 file")


text = "\n\tThis is a demo text\t"
print(text)
print("Strip method:", text.strip())    # It not only remove spaces, It also remove the characters that we put into it
# lstrip()  -> Trimmed the string from the left side only
# rstrip()  -> Trimmed the string from the right side only
x = "I love Programming Programming"
y = "I-love-to-write-codes"
print("Split method:", x.split())
print("Split method:", y.split("-", 3))
print("Replace method:", x.replace("Programming", "Python", 1))

colors = ["red", "blue", "yellow", "green"]
print("Join method:", "-".join(colors))

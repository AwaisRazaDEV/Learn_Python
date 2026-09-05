
# while loop is used when you want to repeat the block of code until a condition becomes false.

i = 0

while i < 6:
    if i == 4:
        break
    print(i)
    i += 1
else:
    print("i is now less than 6")
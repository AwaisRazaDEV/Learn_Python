
#         (Some Complex Patterns)

# <----------- Pattern-I ----------->
print("Hollow box:")

rows = 7
for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            if j == 1 or j == rows or i == 1 or i == rows:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print()

# <----------- Pattern-II ----------->
print("Pyramid:")

for i in range(rows):
    for a in range(rows - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
print()

# <----------- Pattern-III ----------->
print("Hollow Pyramid:")

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i or i == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# <----------- Pattern-IV ----------->
print("Cross:")

for i in range(rows):
    for j in range(rows):
        if j == i or rows - i -1 == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
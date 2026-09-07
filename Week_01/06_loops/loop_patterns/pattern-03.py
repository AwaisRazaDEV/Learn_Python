
#     <--- ( Left Angle Triangle ) --->

# <---------------- Pattern-I ---------------->

rows = 5

for a in range(1, rows + 1):
    for b in range(rows - a):   #for Space
        print(" ", end=" ")
    for c in range(a):          #for Stars
        print("*", end= " ")
        
    print()

# <---------------- Pattern-II ---------------->

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
        
    print()

# <---------------- Pattern-III ---------------->

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(i, end=" ")
        
    print()


#     <--- ( Down Left Angle Triangle ) --->

# <---------------- Pattern-IV ---------------->

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

# <---------------- Pattern-V ---------------->

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

# <---------------- Pattern-VI ---------------->

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ",end=" ")
    for k in range(i):
        print(i, end=" ")
    print()

# <---------------- Pattern-VII ---------------->

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()

#     <--- (Down Right Angle Triangle) --->

# <----------- Pattern-I ----------->

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# <----------- Pattern-II ----------->

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# <----------- Pattern-III ----------->

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# <----------- Pattern-IV ----------->

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# <----------- Pattern-V ----------->

num = 1

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(num, end=" ")
    print()
    num += 1
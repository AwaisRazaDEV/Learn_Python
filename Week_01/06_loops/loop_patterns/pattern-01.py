
#     <--- (Right Angle Triangle) --->

# <---------- Pattern-I ---------->

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# <---------- Pattern-II ---------->

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# <---------- Pattern-III ---------->

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()


# <---------- Pattern-IV ---------->

num = 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

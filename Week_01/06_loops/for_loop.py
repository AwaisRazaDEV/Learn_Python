

# For loop is used when you know how many times to repeat the same block of code or iterating over the sequence.

# for x in "Awais":
#     print(x)


# for loop with range() function
# for i in range(2, 11, 2):  #range(start, stop, gap)
#     print(i)


# <------------- loop controll statements ------------->

# break -> Use to stop the loop.
# continue ->  Use to skip the current iteration and move to next one.

for n in range(11):
    # if n == 5:
    #     continue
    # print(n)
    #       ( comment break when you use continue statement and vice versa )
        if n == 5:
            break
        print(n)
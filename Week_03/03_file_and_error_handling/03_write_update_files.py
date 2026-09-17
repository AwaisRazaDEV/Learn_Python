# <------------------ "x" - Create ------------------> 
# It will create a file, returns an error if the file exists

# file = open("data.txt", "x")



# <------------------ "w" - Write ------------------>
# It will overwrite the file. And also if file is new created it also creates the file:

from pathlib import Path
file_path = Path(__file__).parent / "data.txt"

# with open(r"E:\python\Week_03\03_file_and_error_handling\data.txt", "w") as file:
# with open(file_path, "w") as file:
#     file.write("For test purpose only")



# <------------------ "a" - Append ------------------>
# It will will append to the end of the file

# with open(file_path, "a") as file:
#     file.write("\nGood Luck!")

# with open(file_path) as file:
#     print(file.read())



# <------------------ "r+" - Read first then Write ------------------>
# It will first read the data then write the data

# with open(file_path, "r+") as file:
#     print(file.read())
#     file.write("This is new statement")



# <------------------ "w+" - Write first then Read ------------------>
# It will first write the data then read the data

with open(file_path, "w+") as file:
    file.write("This is new statement")
    file.seek(5)
    print(file.read())



# <------------------ "a+" - Append first then Read ------------------>
# It will will first append the data then read the data

with open(file_path, "a+") as file:
    file.write("\nGood Luck!")
    file.seek(0)
    print(file.read())
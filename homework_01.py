# 1. Take two numbers as input
Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))

# 2. Print there sum, difference, product and division
print("Addition :", Num1 + Num2)
print("Subtraction :", Num1 - Num2)
print("Multiplication :", Num1 * Num2)
print("Division :", Num1 / Num2)

# 3. Check if the first number is greater than the second 
if Num1 > Num2:
    print("First Number is greater than the Second!")
else:
    print("Secnod Number is greater than the First!")

# 4. Check if both number are positive (use 'and')
if Num1 >= 0 and Num2 >= 0 :
    print("Both numbers are Positive")
else:
    print("NO! Numbers are not Positive")

# 5. IF/Elif/Else Practice:
Marks = int(input("Enter your Marks: "))

if Marks >= 90:
    print("Grade A+: Excellent!")
elif Marks >= 80:
    print("Grade A: Geat!") 
elif Marks >= 70:
    print("Grade B: Good!") 
elif Marks >= 60:
    print("Grade C: Better!")
else:
    print("Grade D: Need Improvment!")

# 6. Nestest If Practice:

Age = int(input("Enter your Age: "))
has_ticket = input("Your have a ticket (yes/no): ").lower() == 'yes'

if has_ticket:
    if Age <= 15:
        print("Kid : Free Entry")
    elif Age <= 20:
        print("Junior : Half Entry Fee")
    else:
        print("Adult : Full Entry Fee")
else:
    print("Please! Buy a ticket first")





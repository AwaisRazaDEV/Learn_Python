

# <------------- Else Statement ------------->

# The Else steatement provides a defualt action when none of the previous conditions are true.The else statement must come last, you cannot have an elif after an else.

score = int(input("Enter your score: "))
# score = int(score)

if score >= 90:
    print("Your Grade is A")
elif score >= 80:
    print("Your Grade is B")
elif score >= 70:
    print("Your Grade is C")
elif score >= 60:
    print("Your Grade is D")
elif score >= 50:
    print("Your Grade is E")
else:
    print("Fail! Your grade is F")

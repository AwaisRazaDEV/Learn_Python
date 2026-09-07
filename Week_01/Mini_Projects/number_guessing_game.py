import random

print("Wellcome to the Number Guessing Game 🎯")

name = input("Enter your name: ")
print(f"Hi {name}! Let's start 😊")

random_number = random.randint(1, 10)
attempts = 0

while True:
    guess = input("Guess a number b/w 1-10 (or 'q' to quit): ")
    
    if guess.lower() == "q":
        print("By! You quit the game 👋")
        break
    
    guessed_number = int(guess)
    attempts += 1
    
    if ( guessed_number > 10 or guessed_number <= 0):
        print("Please select a number between 1 to 10")
    elif ( guessed_number > random_number):
        print("TOO HIGH ❌")
    elif (guessed_number < random_number):
        print("TOO LOW ❌")
    else:
        print(f"🎊 Congratulation {name} 👏! You guessed the correct answer in {attempts} attempts")
        break
    

import random

#This is a simple number guessing game where computer generates a random number, and you try to guess it.

random_number = int(random.randint(1, 10))
guess = int(input("Guess a number between 1 and 10:"))

while guess != random_number:
    if guess < 1 or guess > 10:
        print("Please guess within the range.")
        guess = int(input("Guess again:"))
    elif guess > random_number:
        print("You guessed too high.")
        guess = int(input("Guess again:"))
    elif guess < random_number:
        print("You guessed too low.")
        guess = int(input("Guess again:"))

if guess == random_number:
    print(f"You guessed right! The number was {random_number}")
    input("Press Enter to exit...")
    



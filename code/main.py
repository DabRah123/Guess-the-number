import random
from asciiart import ascii_art

number = random.randint(1, 100)

print(ascii_art)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def guess_number():
    attempts = 0
    difficulty = input("Enter the difficulty, Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
        print("You have 10 attempts to guess the number.")
    elif difficulty == "hard":
        attempts = 5
        print("You have 5 attempts to guess the number.")
    else:
        print("You have entered an invalid choice.")
        return

    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The number was {number}.")
            print("You won!")
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
        
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print("You've run out of attempts. You lose.")
            print(f"The correct number was {number}.")

guess_number()

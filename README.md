# Guess-the-number

## Number Guessing Game
This project is a fun, interactive Number Guessing Game implemented in Python. The game randomly selects a number between 1 and 100, and the player must guess the number within a limited number of attempts based on the chosen difficulty level.

## Features
Two difficulty levels:
Easy: 10 attempts to guess the number.
Hard: 5 attempts to guess the number.
Provides feedback on each guess:
"Too high" if the guess is greater than the number.
"Too low" if the guess is less than the number.
Displays ASCII art for an engaging start to the game.

## Project Structure
The project is split into two files for modularity:

asciiart.py: Contains the ASCII art used to welcome the player.
main.py: Contains the main game logic and imports the ASCII art.

## Example Gameplay
The game starts by displaying the ASCII art and a welcome message.
The player selects a difficulty level (easy or hard).
The player makes guesses, and the game provides feedback until the number is guessed or attempts run out.
Enjoy playing and feel free to contribute to improve the project! 😊

## Algorithm: Number Guessing Game

1. Initialize Game-
Import the necessary modules (random for generating random numbers and ASCII art from asciiart.py).
Display the ASCII art and a welcome message.

2. Generate Random Number-
Generate a random integer number between 1 and 100.

3. Choose Difficulty-
Prompt the user to select the difficulty level:
If easy, set attempts = 10.
If hard, set attempts = 5.
If the input is invalid, display an error message and terminate.

4. Start Guessing Loop-
While the number of attempts is greater than 0:
Prompt the user to input a guess.
Compare the guess with the number:
If guess == number, display a success message and terminate.
If guess > number, display "Too high."
If guess < number, display "Too low."
Decrease the attempts counter by 1.
If attempts > 0, inform the user of the remaining attempts.
If attempts == 0, display a failure message with the correct number.

5. End Game-
Exit after the player wins or loses.

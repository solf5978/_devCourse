"""
Author: Jesse Warner
Date: August 1, 2023

In this challenge, you will create a guess the number game! The game requires 
importing the `random` module and generating a random integer, which has not 
been covered yet, so the code has been provided. Your challenge is creating the 
game's logic using variables, loops, and conditional statements.
"""

# Import the random module to generate random numbers
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Create a variable to hold the number of times a player guessed a number
guess_times = 0
# Create a variable to set the maximum number of guesses before the game ends
max_guess_times = 10
# Output a message that welcomes the player and tells them how to play
print("Bu Bu Bu\n\r")
"""
Create the game logic in a loop that executes while the player has remaining 
attempts. The player should be able to input a guess and receive output whether 
the guess is correct, too low, or too high. Should the player reach the maximum 
number of attempts without guessing correctly, a message should be displayed 
indicating the game is over and what the number is, and the game (program) ends.

HINT: `input()` always returns a string, but you will be comparing numeric 
values.
"""
while guess_times < max_guess_times:
    print("Remaining Times To Try : ", max_guess_times - guess_times)
    cur_guess = int(input("Your Guess Is : "))
    if cur_guess < secret_number: 
        print("Too Low, try again")
    elif cur_guess > secret_number:
        print("too high, try again")
    else:
        print("you got it right, the number is ", secret_number)
        break
    guess_times += 1

    if guess_times == max_guess_times:
        print("no more try you have, let it be")
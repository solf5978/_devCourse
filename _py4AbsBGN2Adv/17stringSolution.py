"""
Author: Jesse Warner
Date: August 1, 2023

In this challenge, you are going to create a mad lib generator! You should 
start by printing a welcome message to the console. Then, get user input for a 
noun, verb, adjective, and adverb and store the values in variables. After 
that, format a string to tell a short story using the user's inputs and store 
it in a variable. Finally, output the story to the console.
"""

# Print a welcome message to the console
print("Welcome to the Mad Libs Game!")

# Get inputs for a noun, verb, adjective, and adverb and store them in variables
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

# Format a string be a story with the 4 user inputs and store in in a variable
story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} \
{adverb}."

# Print the formatted story string to the console
print("\nHere's your Mad Libs story:")
print(story)

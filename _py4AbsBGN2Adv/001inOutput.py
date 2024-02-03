"""
Author: Jesse Warner
Creation Date: August 1, 2023

The `print()` function is used to display output on the console or terminal. It 
takes one or more arguments and prints them to the standard output. The 
`print()` function is versatile and can also print to files, change the line 
endings, and change the separator between arguments. The `print()` function is 
a useful tool for debugging, displaying information, and monitoring the 
execution of your Python programs.

The `input()` function in Python is used to prompt the user for input. It 
allows you to interactively take input from the user during the execution of a 
program. The `input()` function takes a string argument, which is displayed as 
a prompt to the user.

When the `input()` function is called, it waits for the user to enter input 
from the keyboard. The user can type a string and press the Enter key. The 
`input()` function then returns the entered string as the result.

It's important to note that the `input()` function always returns a string, 
even if the user enters a different type of value (such as a number). If you 
need to convert the input to a specific type (like an integer or float), you 
can use type casting.
"""

# Invoke the `print()` function by typing its name with a pair of parentheses 
# and providing it an argument to output.
print("Hello, World!") # Output: Hello, World!

# Perform operations as arguments
print(5 + 3) # Output: 8

# Pass multiple arguments separated by commas into the `print()` function
print("Hi", 2, "how", 4, "are you?") # Output: Hi 2 how 4 are you?

# Pass a dash (-) as the `sep` argument to separate the values by a dash 
# instead of an empty space.
print("Hi", 2, "how", 4, "are you?", sep='-') # Output: Hi-2-how-4-are you?

# Pass an empty string as the argument for the `sep` parameter, so no space is 
# added between values. Pass the value '!!!\n' as the `end` argument to change 
# the line ending for the output created by the `print()` function.
print("Hi", 2, "how", 4, "are you?", sep='', end='!!!\n') 
# Output: Hi2how4are you?!!!

# Get input from a user using the `input()` function and assign the value to 
# the variable `name`. The `input()` function takes a single argument, which is 
# output to the console for the user to see.
name = input("Enter your name: ")
print("Hello,", name) # Output: Hello, (value of `name`)
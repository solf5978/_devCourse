"""
Author: Jesse Warner
Date: August 1, 2023
"""

# Define a function that adds 2 snowman Unicode characters on either side of a 
# string
def snowmanify(string):
    return "\N{SNOWMAN}\N{SNOWMAN} " + string + " \N{SNOWMAN}\N{SNOWMAN}"

# Define a function that removes spaces and snowman Unicode characters from the 
# left and right side of a string
def desnowmanify(string):
    return string.strip(' \N{SNOWMAN}')
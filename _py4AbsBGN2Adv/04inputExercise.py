"""
Author: Jesse Warner
Date: August 1, 2023

In this challenge, you will create two variables that take user input, one for 
your first name and one for your last name. Then, print a greeting that outputs 
"Hello, [your first and last name]"
"""

# Create a variable for your first name
input_username = input("Please Enter Your First Name")
# Create a variable for your last name
input_lastname = input("Please Enter Your Last Name")
# Print a greeting to the console
print("Hello " + input_lastname + input_username)
# Expected Output: "Hello, [your name here]"
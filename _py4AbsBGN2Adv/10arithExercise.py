"""
Author: Jesse Warner
Date: August 1, 2023

For this challenge, you are going to practice performing arithmetic operations 
in Python. Two variables have been provided for you to perform operations on, 
and you should put the result in the variable named `result` to be printed to 
the console. 
"""
import math
# x, y, and result variables for you to perform operations and store the values
x = 25
y = 3
result = None

# Add the variables x and y together
print("X + Y =", x + y)

# Subtract y from x
print("X - Y =", x - y)

# Multiply y and x together
print("X * Y =", x * y)

# Use regular division to divide x by y
print("X / Y =", x / y)

# Use floor division to divide x by y
print("X / Y (floor)=", math.floor(x / y))

# Use the modulo operator to get the remainder of x divided by y
print("X % Y =", x % y)

# Use exponentiation to raise y to the power of x
print("Y^X =", pow(y, x))

# Use multiple operators to perform complex operations to understand the order 
# of precedence 
example: result = x + y / (x - y) ** y

# Print the result to the console
print(result)
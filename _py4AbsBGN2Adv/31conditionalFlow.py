"""
Author: Jesse Warner
Creation Date: August 1, 2023

Conditionals in Python are used to execute different blocks of code based on 
specific conditions. They allow you to control the flow of your program and 
make decisions based on certain criteria. The main conditional statements in 
Python are `if`, `elif` (short for "else if"), and `else`.

The basic syntax of a conditional statement is as follows:
    if condition:
        Code to be executed if the condition is True

    elif condition:
        Code to be executed if the preceding condition(s) is False and this 
        condition is True

    else:
        Code to be executed if all preceding conditions are False

Key concepts of conditional statements:
    - `if` Statement: It starts with the keyword `if`, followed by a condition. 
      If the condition evaluates to `True`, the code block indented under the 
      `if` statement is executed. If the condition is `False`, the code block 
      is skipped.

    - `elif` Statement: It stands for "else if" and is used to check additional 
      conditions after the `if` statement. It can be used multiple times to 
      check multiple conditions. If the preceding condition(s) in the `if` or 
      `elif` statements are False, and this condition evaluates to `True`, the 
      code block indented under the `elif` statement is executed.

    - `else` Statement: It is used as a fallback option when all preceding 
      conditions are `False`. If none of the preceding conditions in the `if` 
      or `elif` statements evaluate to `True`, the code block indented under 
      the `else` statement is executed.

    - Nested Conditional Statements: You can use conditional statements inside
      of other conditional statements. This allows you to perform more complex 
      decision-making based on multiple conditions.

    - Ternary Operator: It is a concise way to write conditional statements in 
      Python. It allows you to make decisions and assign values based on a 
      condition in a single line of code.
          Syntax:
              value_if_true if condition else value_if_false
"""

# Create variables to perform conditional operations on
w = -5
x = 5
y = 10
z = 0

# Conditional using an `if` statement where the `if` condition is `True`
if x < y:
    print(f"{x} is less than {y}")
# Output: 5 is less than 10

# Conditional using an `if` statement where the `if` condition is `False` (code 
# does not run)
if y < x:
    print(f"{y} is less than {x}")
# Output: No output

# Conditional using the `if` and `elif` statements where the `elif` condition 
# is `True`
if y < x:
    print(f"{y} is less than {x}")
elif y > x:
    print(f"{y} is greater than {x}")
# Output: 10 is greater than 5

# Conditional using the `if` and `elif` statements where no condition is `True`
if y < 10:
    print(f"{y} is less than {x}")
elif y > 10:
    print(f"{y} is greater than {x}")
# Output: No output

# Conditional using the `if`, `elif`, and `else` statements where no condition 
# is `True`
if z > 0:
    print(f"{z} is positive")
elif z < 0:
    print(f"{z} is negative")
else:
    print(f"{z} is zero")
# Output: 0 is zero

# Conditional using multiple `elif` statements where the third `elif` statement 
# is `True`
if x < 0:
    print(f"{x} is negative")
elif y < 0:
    print(f"{y} is negative")
elif z < 0:
    print(f"{z} is negative")
elif w < 0:
    print(f"{w} is negative")
else:
    print("No negative numbers found")
# Output: -5 is negative

# Conditional with a nested conditional
if x > 0:
    if x % 2 == 0:
        print(f"{x} is positive and even")
    else:
        print(f"{x} is positive and odd")
else:
    print(f"{x} is not positive")
# Output: 5 is positive and odd

# Conditional using the `and` logical operator, so both evaluations must be 
# `True`
if x > 0 and y > 0:
    print(f"Both {x} and {y} are positive")
# Output: Both 5 and 10 are positive
# This conditional evaluates to (True and True), which evaluates to True

# Conditional using the `or` logical operator, so one evaluation must be `True`
if x > 0 or w > 0:
    print(f"Either {w} or {x} is positive")
# Output: Either -5 or 5 is positive
# This conditional evaluates to (True or False), which evaluates to True

# Conditional using the `not` logical operator, so the evaluation immediately 
# after the `not` keyword must be false for the entire evaluation to be `True`
if not w > 0:
    print(f"{w} is negative")
# Output: -5 is negative
# This conditional evaluates to (not False), which evaluates to True

# Conditional using the `not`, `and`, and `or` logical operators
if not (x < 0 and w > 0) or (x < 0 and w < 0):
    print(f"Either {x} is not negative and {w} is not positive, or {x} is "
          f"negative and {w} is negative")
# Output: Either 5 is not negative and -5 is not positive, or 5 is negative and 
# -5 is negative
# This `if` statement evaluates in the following ways:
# (not (False and False)) or (False and True)
# (not False) or False
# True or False
# True

# Create two variables to use with a ternary operator
a = 10
b = 20

# Set max_value to a if a is greater than b else set max_value to b
max_value = a if a > b else b

print(f"Max value of {a} and {b}: {max_value}")  
# Output: Max value of 10 and 20: 20

"""
Author: Jesse Warner
Date: August 1, 2023

For loops are used to iterate over a sequence (list, tuple, string, or range) 
or any iterable object. The for loop executes a block of code for each item in 
the sequence or iterable.

Syntax of a while statement:
    for item in sequence:   
        code to execute for each iteration
    else: (optional)
        code to execute after the for loop completes

Loop control statements:
    - break: Terminates the loop prematurely, regardless of the loop condition. 
      It is used to exit the loop and continue executing the code after the 
      loop.
      
    - continue: Skips the rest of the current iteration and moves on to the 
      next iteration. It is used to skip specific iterations of the loop.
"""

#****************************** Basic for Loops ********************************

# For loop that iterates through the numbers in range(1, 4) and prints the 
# current number
for number in range(1, 4):
    print(f"Current number: {number}")
    # Output:
    # Current number: 1
    # Current number: 2
    # Current number: 3

# For loop that iterates over a string and prints each character
for character in "Cat":
    print(f"Current Character: {character}")
    # Output: 
    # Current Character: C
    # Current Character: a
    # Current Character: t

#********************* For Loop Using The Break Statement **********************

# For loop that iterates through the numbers in range(1, 4) and prints the 
# current number. The loop breaks if number is equal to 2.
for number in range(1, 4):
    print(f"Current number: {number}")
    if number == 2:
        break
    # Output:
    # Current number: 1
    # Current number: 2
# Since the loop ended when the value of `number` was 2, the loop did not make 
# it to the final number in the range.

#******************** For Loop Using The Continue Statement ********************

# List of car makes.
cars = ["Toyota", "Ford", "Chevrolet"]

# For loop that iterates over the `cars` list and prints each element. If `car` 
# is equal to `Ford`, the continue statement forces the loop to stop its 
# current iteration and go to the next one.
for car in cars:
    if car == "Ford":
        continue
    print(car)
    # Output:
    # Toyota
    # Chevrolet
# Since the loop skipped the rest of the iteration when the value of `car` was 
# "Ford", the print statement was skipped.

#********************* For Loops Using The Else Statement **********************

# List of car makes.
cars = ["Toyota", "Ford", "Chevrolet"]

# A for loop with an optional `else` statement that iterates over the `cars` 
# list and prints each element. 
for car in cars:
    print(car)
else:
    print("Done printing cars!")
    # Output:
    # Toyota
    # Ford
    # Chevrolet
    # Done printing cars!


# For loop with optional `else` statement that iterates through the numbers in 
# range(1, 4) and prints the current number. The loop breaks if number is equal 
# to 2. If the `break` statement executes, the `else` statement will not.
for number in range(1, 4):
    print(f"Current number: {number}")
    if number == 2:
        break
    # Output:
    # Current number: 1
    # Current number: 2
else:
    # This code is never called because of the break statement
    pass

#******************************* Nested For Loop *******************************

# Two lists of numbers
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

# For loop that iterates over the numbers1 list
for num1 in numbers1:
    # For loop that iterates over the numbers2 list and prints the product of 
    # num1 and num2 at their current values in iteration.
    for num2 in numbers2:
        product = num1 * num2
        print(f"The product of {num1} and {num2} is {product}")
        # Output:
        # The product of 1 and 4 is 4
        # The product of 1 and 5 is 5
        # The product of 1 and 6 is 6
        # The product of 2 and 4 is 8
        # The product of 2 and 5 is 10
        # The product of 2 and 6 is 12
        # The product of 3 and 4 is 12
        # The product of 3 and 5 is 15
        # The product of 3 and 6 is 18
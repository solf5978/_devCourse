"""
Author: Jesse Warner
Date: August 1, 2023

A while loop is a control flow statement that allows the program to repeatedly 
execute a block of code as long as a condition remains true. The while loop 
evaluates the condition before each iteration and continues looping if the 
condition remains true.

Syntax of a while statement:
    while condition:   
        code to execute during each iteration
    else: (optional)
        code to execute if the condition is False

Loop control statements:
    - break: Terminates the loop prematurely, regardless of the loop condition. 
      It is used to exit the loop and continue executing the code after the 
      loop.
      
    - continue: Skips the rest of the current iteration and moves on to the 
      next iteration. It is used to skip specific iterations of the loop.
"""

#****************************** Basic While Loop *******************************

# A while loop that prints the counter while it is less than 4
count = 1
while count < 4:
    print(f"Counter: {count}")
    count += 1
    # Output:
    # Counter: 1
    # Counter: 2
    # Counter: 3

#******************* While Loop With an Continue Statement *********************

# A while loop that uses the continue statement if counter is equal to 2.
count = 1
while count < 4:
    if count == 2:
        count += 1
        continue
    print(f"Counter: {count}")
    count += 1
    # Output:
    # Counter: 1
    # Counter: 3

#********************* While Loops With a Break Statement **********************

# A while loop that prints the counter until it is greater than or equal to 4
count = 1
while True:
    print(f"Counter: {count}")
    count += 1
    if count >= 4:
        break
    # Output:
    # Counter: 1
    # Counter: 2
    # Counter: 3

#********************** While Loop With an Else Statement **********************

# A while loop with an optional else statement that prints the counter while it 
# is less than 4
count = 1
while count < 4:
    print(f"Counter: {count}")
    count += 1
else:
    print("The while loop finished!")
# Output:
# Counter: 1
# Counter: 2
# Counter: 3
# The while loop finished!

# While loop with a break and else statement that runs until the user types 'q'
while True:
    response = input("Type q to exit the loop: ")
    if response.lower() == 'q':
        break
else:
    # This code is never called because of the break statement
    pass

#****************************** Nested While Loop ******************************

# A matrix (2D list) with 3 rows by 3 columns of numbers.
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# A nested while loop
row = 0
while row < len(matrix):
    col = 0
    while col < len(matrix[row]):
        print(f"Matrix Element: {matrix[row][col]}")
        col += 1
    row += 1
# Output:
# Matrix Element: 1
# Matrix Element: 2
# Matrix Element: 3
# Matrix Element: 4
# Matrix Element: 5
# Matrix Element: 6
# Matrix Element: 7
# Matrix Element: 8
# Matrix Element: 9

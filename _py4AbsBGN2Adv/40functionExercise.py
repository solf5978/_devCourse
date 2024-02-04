"""
Author: Jesse Warner
Date: August 1, 2023

In this challenge, you are going to create a simple calculator! The calculator 
should have functions to do addition, subtraction, multiplication, and 
division. Each function will take two integer arguments and perform the 
operation on the integers passed into it. You will create an options menu for 
the user with an option for each operation and to quit the program. If the user 
chooses an operation, the user will be prompted to enter two numbers for the 
operation to work with. The calculator should continue to run until the user 
decides to quit.
"""

# Create a function to perform addition
def addition(first , second):
    return first + second
# Create a function to perform subtraction
def subtraction(first , second):
    return first - second
# Create a function to perform multiplication
def multiplication(first , second):
    return first * second
# Create a function to perform division
def division(first , second):
    return first / second
# Create the loop that will prompt the user for an option and run until the 
# user decides to quit

while True:
    print("Press 'q' to exit current program")
    first = (input("Enter your first argument with number or q: "))
    second = (input("Enter your second argument with number or q: "))
    opCode = (input("Enter your desired operation +-*/ or q to exit: "))

    first = int(first)
    second = int(second)

    if opCode == "q":
        break    
    elif opCode == "+":
        print(addition(first, second))
        break
    elif opCode =="-":
        print(subtraction(first, second))
        break
    elif opCode == "*":
        print(multiplication(first, second))
        break
    elif opCode == "/":
        print(division(first, second))
        break
    else:
        print("your input can't be parsed, please try again")
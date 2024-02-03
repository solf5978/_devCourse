"""
Author: Jesse Warner
Creation Date: August 1, 2023

Integers are a fundamental data type in Python used to represent whole numbers. 
They encompass positive, negative, and zero values without decimals or 
fractional parts. They are utilized in various computational tasks, ranging 
from simple counting to complex mathematical calculations. Python's integer 
data type can accommodate a wide range of whole numbers from small to very 
large values.

To create an integer, you can assign a whole number without a decimal point to 
a variable. You can also use the `int()` function to explicitly convert other 
data types into an integer.

Common uses for integers:
    Counting and Indexing: Integers are pivotal in counting iterations and 
    indexing elements within data structures like lists, tuples, and strings.

    Mathematical Calculations: Integers are foundational for performing 
    mathematical computations, constructing algorithms, and solving numeric 
    problems.

    Control Structures: Integers play a key role in conditionals, loops, and 
    decision-making, allowing programs to respond dynamically based on 
    numerical values.
"""

#******************************* Create Integers *******************************
# Create a variable and assign it an integer value
my_int1 = 1

# Create an integer using the `int()` function and passing in a float value
my_int2 = int(5.3)
print(my_int2) # Output: 5

# Create an integer using the `int()` function and passing in a string value
my_int3 = int("127")
print(my_int3) # Output: 127

#************************** Arithmetics With Integers **************************
# Using the additional operator on two integers
my_int4 = 10 + 35
print(my_int4) # Output: 45

# Using the subtraction operator on two integers
my_int5 = 25 - 24
print(my_int5) # Output: 1

# Using the multiplication operator on two integers
my_int6 = 8 * 8
print(my_int6) # Output: 64

#************************** Very Large Integer Values **************************
# Create two very large integer values
x = 50938475038475029348509348750934750342570394875093487503487500348950
y = 98470659873405987430985743098570324870293845098324509873240957832409

# Arithmetic operations on very large numbers
result = x + y
print(result)
# Output: 149409134911881016779495091849505075212864239973417997376728458181359

result = x * y
print(result)
# Output: 
# 501594524998365558419995873891928260042471036013122981830871018252125069907862
# 8875424245425214479694307793791792497897095458623119120550

#******************* Using Built-In Functions With Integers ********************
# Using the `abs()` function to get the absolute value of an integer
result = abs(-12)
print(result) # Output: 12

# Using the `divmod()` function to get the quotient rounded down to the nearest 
# whole number and remainder of two integers. 26 divided by 7 is 3 with a 
# remainder of 5. The result is a tuple containing the values.
result = divmod(26, 7)
print(result) # Output: (3, 5)

# Using the `min()` function to get the lowest value from a variable number of 
# integer arguments. 
result = min(12, 27, 84, 90, 1, -27)
print(result) # Output: -27

# Using the `min()` function to get the lowest value from a list of integers. 
result = min([4, 17, 1, 9])
print(result) # Output: 1

# Using the `max()` function to get the highest value from a variable number of 
# integer arguments. 
result = max(12, 27, 84, 90, 1, -27)
print(result) # Output: 90

# Using the `max()` function to get the highest value from a tuple of integers. 
result = max((4, 17, 1, 9))
print(result) # Output: 17

# Using the `pow()` function to raise 5 to the power of 3.
result = pow(5, 3)
print(result) # Output: 125

# Using the `pow()` function to raise 5 to the power of 3 and getting the 
# remainder of that value divided by 17. 125 / 17 is 7 with a remainder of 6.
result = pow(5, 3, 17)
print(result) # Output: 6

# Using the 'sum()' function to get the sum of a list of integers.
result = sum([20, 12, 4])
print(result) # Output: 36

# Using the 'sum()' function to get the sum of a list of integers added to a 
# starting value of 10.
result = sum([20, 12, 4], 10)
print(result) # Output: 46

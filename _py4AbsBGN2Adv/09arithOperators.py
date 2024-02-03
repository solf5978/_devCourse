"""
Author: Jesse Warner
Creation Date: August 1, 2023

Arithmetic operators in Python are used to perform mathematical computations on 
numerical values. They follow the typical mathematical precedence rules of 
PEMDAS: Parentheses, Exponents, Multiplication and Division (from left to 
right), and Addition and Subtraction (from left to right).

Commonly used arithmetic operators:
    Addition `+`:
        When applied to numeric operands (integers and floats), the addition 
        operator adds the values together. When applied to sequence types such 
        as lists, strings, and tuples, they are concatenated together.

    Subtraction `-`:
        The subtraction operator is used to perform subtraction between numeric 
        operands. It can also be used to negate a single operand and make a 
        positive value negative or a negative value positive.

    Multiplication `*`:
        The multiplication operator performs multiplication on two operands and 
        produces a product. It can also be used for repetition when used with a 
        sequence type, such as strings, lists, tuples, etc. 

    Division `/`:
        The division operator performs floating-point division between two 
        operands. The resulting quotient is always a floating-point number 
        regardless of the operand type.

    Floor Division `//`:
        The floor division operator performs division and returns the integer 
        quotient rounded down to the nearest whole number (floor value). The 
        result is always an integer, truncating any decimal part. It is 
        important to remember that with negative numbers, it still rounds down.

    Modulus `%`:
        The modulo operator divides the left operand by the right operand and 
        returns the remainder. This operator is useful in various ways, 
        including determining if a number is odd or even, and it is used on 
        very large numbers to perform encryption and decryption.

    Exponentiation `**`:
        The exponentiation operator is used to raise a number to a power. It 
        raises the operand on the left to the power of the operand on the right.
"""

#********************** Basic Operator Use In Arithmetics **********************

# Create two variables to perform arithmetic operations on
x = 10
y = 3

# Use each operator on the operands `x` and `y`
addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
floor_division = x // y
modulo = x % y
exponentiation = x ** y

# Print the results of the operations
print(f"{x} + {y} = {addition}")           # Output: 10 + 3 = 13
print(f"{x} - {y} = {subtraction}")        # Output: 10 - 3 = 7
print(f"{x} * {y} = {multiplication}")     # Output: 10 * 3 = 30
print(f"{x} / {y} = {division}")           # Output: 10 / 3 = 3.3333333333333335
print(f"{x} // {y} = {floor_division}")    # Output: 10 // 3 = 3
print(f"{x} % {y} = {modulo}")             # Output: 10 % 3 = 1
print(f"{x} ** {y} = {exponentiation}")    # Output: 10 ** 3 = 1000

#********************* Order Of Operations In Arithmetics **********************

# 2 * 4 evaluates to 8, then 5 + 3 evaluates to 8, then 8 - 8 evaluates to 0
result = 5 + 3 - 2 * 4
print(result) # Output: 0

# 2 ** 3 (2 to the third power) evaluates to 8, then 10 / 8 evaluates to 1.25
result = 10 / 2 ** 3
print(result) # Output: 1.25

# First (10 % 3) evaluates to 1, then 4 ** 3 evaluates to 64, then 10 * 3 
# evaluates to 30, 64 // 6 evaluates to 10, then 30 + 10 evaluates to 40, 
# finally, 40 - 1 evaluates to 39
result = 10 * 3 + 4 ** 3 // 6 - (10 % 3)
print(result) # Output: 39

#***************** Using The `+` Operator With Sequence Types ******************

# Create two strings to concatenate
greeting = "Hello,"
name = "World!"
# Concatenate three strings using the `+` operator
concatenated_message = greeting + " " + name
print(f"Concatenated message: {concatenated_message}") 
# Output: Concatenated message: Hello, World!

# Create two lists to concatenate
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Concatenate two list using the `+` operator
concatenated_list = list1 + list2
print(f"Concatenated list: {concatenated_list}") 
# Output: Concatenated list: [1, 2, 3, 4, 5, 6]

# Create two tuples to concatenate
tuple1 = (7, 8, 9)
tuple2 = (10, 11, 12)
# Concatenate two tuples using the `+` operator
concatenated_tuple = tuple1 + tuple2
print(f"Concatenated tuple: {concatenated_tuple}") 
# Output: Concatenated tuple: (7, 8, 9, 10, 11, 12)

#******************** Negating Values With The `-` Operator ********************

# Create some variables to perform negation on
a = 10
b = 12
# Use the `-` operator to negate the value of `a` + `b` (22 to -22)
c = -(a + b)
print(f"-(a + b) = {c}") # Output: -(a + b) = -22

# Use the `-` operator to negate the value of `a` (10 to -10), multiply that 
# by `b`, and assign the result to `d`
d = -a * b
print(f"-a * b = {d}") # Output: -a * b = -120

# Negate the value of `d` (-120 to 120)
print(f"-d = {-d}") # Output: -d = 120

#****************** Repeating Sequences With The `*` Operator ******************

# Create a string to repeat using the `*` operator
greeting = "Hello!"
# Repeat `greeting` 10 times
multiple_greeting = greeting * 10
print(multiple_greeting) 
# Output: Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!

# Create a list to repeat using the `*` operator
list3 = [1, 'hi', 3.14, []]
# Repeat the list 3 times
multiple_list = list3 * 3
print(multiple_list)
# Output: [1, 'hi', 3.14, [], 1, 'hi', 3.14, [], 1, 'hi', 3.14, []]
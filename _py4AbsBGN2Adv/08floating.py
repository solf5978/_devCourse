"""
Author: Jesse Warner
Creation Date: August 1, 2023

Floats are a type of data that represents real numbers. They are stored as 
64-bit double-precision floating point numbers. This means the float data type 
can represent numbers of up to 17 significant digits. However, it is important 
to note that the actual number of decimal places displayed may be less than 17.
This is because Python rounds the number to the nearest representable value 
when it is displayed.

Due to how floating-point numbers are represented in computers, performing 
calculations with floats can sometimes lead to unexpected results. It's 
important to be aware of floating-point precision limitations and consider 
using the decimal module or other techniques for precise calculations involving 
decimal numbers.

    0.123456789123456789 is shown as 0.12345678912345678. The 18th digit after 
    the decimal point (9) is removed. The insignificant digit 0 before the decimal is shown, which gives us 17 significant digits.

    123456789.12345678999 is shown as 123456789.12345679. The 18th to 20th significant digits are removed, and the 17th digit is rounded up, which again leaves us with 17 significant digits.

To create a float variable, assign a number with a decimal point to it. You can
also use the float() function, which can convert integers and strings to a
float or any function that returns a float value. Mathematical operations that 
contain at least one float or result in a float value will return a float value.
"""

# Create and initialize `my_float` to a float value
my_float1 = 1.0

# Create and initialize `my_float2` using the `float()` function with an integer
my_float2 = float(99)
print(my_float2) # Output: 99.0

# Create and initialize `my_float3` using the `float()` function with a string
my_float3 = float("25.123")
print(my_float3) # Output: 25.123

# Create and initialize `my_float4` using a mathematical operation (division
# always returns a float)
my_float4 = 4 / 2
print(my_float4) # Output 2.0

# Create and initialize `my_float5` with the sum of the float 2.0 and the 
# integer 1. The result will be a float because a float was used in the 
# operation.
my_float5 = 2.0 + 1
print(my_float5) # Output: 3.0

# Create a float with the whole number 0 and a precision of 20. The 18th
# through 20th digits after the decimal are removed, and the 17th is rounded up.
x = 0.12345678912345675999
print(x) # Output: 0.12345678912345676

# Create a float with a whole number 9 digits long and a precision of 11. 
# The 9th through 11th digits after the decimal are removed, and the 8th is
# rounded up.
y = 123456789.12345678901
print(y) # Output: 123456789.12345679

# Create a float with a whole number 20 digits long. A number with 17 or more
# digits before the decimal place is stored in scientific notation format. Any 
# digits passed the 17th are removed.
z = 12345678901234567890.123
print(z) # Output: 1.2345678901234567e+19

#*************** Example of floating point precision limitations ***************
a = 0.1
b = 0.2
c = 0.3

# The decimal values 0.1 and 0.2 cannot be represented precisely as binary 
# fractions. Therefore, when these numbers are added together, the result is a 
# slightly imprecise value. Math functions such as math.isclose() can be used 
# if perfect precision is not necessary.
print(a + b) # Output: 0.30000000000000004
print(c) # Output: 0.3
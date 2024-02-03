"""
Author: Jesse Warner
Creation Date: August 1, 2023

Assignment operators are used to assign values to variables. They combine the assignment (=) operator with other arithmetic or bitwise operators to perform an operation and assign the result back to the variable.

Assignment Operators:
    Assignment `=`:
        Assigns the value on the right to the variable on the left.

    Addition Assignment `+=`:
        Adds the value on the right to the variable on the left and assigns the result back to the variable.

    Subtraction Assignment `-=`:
        Subtracts the value on the right from the variable on the left and assigns the result back to the variable.

    Multiplication Assignment `*=`:
        Multiplies the variable on the left by the value on the right and assigns the result back to the variable.

    Division Assignment `/=`:
        Divides the variable on the left by the value on the right and assigns the result back to the variable.

    Floor Division Assignment `//=`:
        Performs floor division of the variable on the left by the value on the right and assigns the result back to the variable.

    Modulus Assignment `%=`:
        Computes the modulus of the variable on the left divided by the value on the right and assigns the result back to the variable.
        
    Exponentiation Assignment `**=`:
        Raises the variable on the left to the power of the value on the right and assigns the result back to the variable.
"""

# Addition assignment
x = 5
x += 3  # Equivalent to: x = x + 3
print(x)  # Output: 8

# Subtraction assignment
y = 10
y -= 2  # Equivalent to: y = y - 2
print(y)  # Output: 8

# Multiplication assignment
z = 3
z *= 4  # Equivalent to: z = z * 4
print(z)  # Output: 12

# Division assignment
a = 15
a /= 5  # Equivalent to: a = a / 5
print(a)  # Output: 3.0 (result is a float)

# Floor division assignment
b = 17
b //= 4  # Equivalent to: b = b // 4
print(b)  # Output: 4 (result is an integer)

# Modulo assignment
c = 20
c %= 7  # Equivalent to: c = c % 7
print(c)  # Output: 6

# Exponentiation assignment
d = 2
d **= 4  # Equivalent to: d = d ** 4
print(d)  # Output: 16

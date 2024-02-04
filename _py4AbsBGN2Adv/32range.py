"""
Author: Jesse Warner
Creation Date: August 1, 2023

The range data type represents an immutable sequence of numbers. Ranges are 
commonly used to generate numbers in a specific range and are often used in for 
loops to iterate over a sequence of numbers. Ranges are created using the 
range(start, stop, step) function.

    - start: The value the range starts at (inclusive). It is an optional 
      parameter that defaults to 0 if no value is provided.

    - stop: The value the range ends at (exclusive). It is a required parameter 
      and is not included in the generated sequence.

    - step: The incremental value of the range. It is an optional parameter   
      that defaults to 1 if no value is provided.

Key features of the range data type:
    - Immutable: The sequence of numbers a range represents is immutable.

    - Lazy access: Ranges generate and use numbers as they are needed rather 
      than storing them in memory.

Common Operations and Methods:
    - Iteration: Ranges can be iterated over using a for loop or converting it
      to a list.

    - Length: The number of elements in a range can be obtained using the 
      `len()` function.

    - Membership Testing: The `in` operator can be used to determine if a value
      is present in a range.
      
    - Arithmetics - Ranges can be used in arithmetics to perform calculations.
"""

# Create a range passing in only a stop argument
my_range1 = range(4) # Generates the numbers 0, 1, 2, 3

# Create a range passing in start and stop arguments
my_range2 = range(3, 6) # Generates the numbers 3, 4, 5

# Create a range passing in start, stop, and step arguments
my_range = range(1, 9, 2) # Generates the numbers 1, 3, 5, 7

print(my_range) # Output: range(1, 9, 2)

# Get the length (number of elements) of a range using the built-in `len()` 
# function
print(len(my_range)) # Output: 4

# Iterate over a range using a for loop
for element in my_range:
    print(element)
    # Output:
    # 1
    # 3
    # 5
    # 7

# Convert a range to a list using the l`ist()` function
my_list = list(my_range)
print(my_list) # Output: [1, 3, 5, 7]

# Arithmetics using a range and for loop
for i in my_range:
    print(f"{i} * 4 = {i * 4}")
    # Output
    # 1 * 4 = 4
    # 3 * 4 = 12
    # 5 * 4 = 20
    # 7 * 4 = 28

# Arithmetics using a range and the `sum()` function
print(f"Sum of my_range: {sum(my_range)}") # Output: Sum of my_range: 16
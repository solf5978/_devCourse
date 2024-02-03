"""
Author: Jesse Warner
Creation Date: August 1, 2023

A tuple is an ordered collection of elements, similar to a list, but with one 
key difference: tuples are immutable, meaning their elements cannot be modified 
once the tuple is created. Tuples are defined using parentheses () or the 
`tuple()` function. Tuples can also be created by tuple packing which is 
assigning comma-separated values to a single variable.

Key features of Python tuples:
    - Immutable: Tuples are immutable, meaning their elements cannot be 
      modified after creation. Once a tuple is defined, its elements remain
      fixed.

    - Ordered: Tuples are ordered collections, which means the order of
      elements is preserved.

    - Indexed: Each element in a tuple has a specific index based on its
      position starting at [0].

    - Heterogeneous Elements: Tuples can contain elements of different data
      types. You can mix integers, floats, strings, booleans, or even other
      tuples within a single tuple.

Common operations and methods you can perform on tuples:
    - Creating Tuples: Tuples can be created using parentheses (),  commas `,`, 
      or the `tuple()` function. Elements are separated by commas.

    - Accessing Elements: Individual elements of a tuple can be accessed using
      indexing, similar to lists. Indexing starts from 0 for the first element.

    - Slicing Tuples: You can extract a subset of elements from a tuple using
      slicing. This creates a new tuple containing the selected elements.

    - Concatenating Tuples: Tuples can be concatenated using the `+` operator,
      resulting in a new tuple that combines the elements of both tuples.

    - Unpacking Tuples: Tuples can be unpacked into multiple variables,
      allowing you to assign each element of a tuple to a separate variable in
      a single line.

    - Packing Tuples: Tuples can be packed by assigning multiple values to a
      single variable. 

Tuples are commonly used when you want to store related data that should remain
unchanged. They provide an efficient way to group elements together and 
maintain their integrity. Tuples are often used in scenarios where data 
integrity and immutability are desired.
"""

# Create a tuple using parentheses and separating the elements by commas
my_tuple = (1, "Hello", 3.14)

# Create tuple using the `tuple()` function. When using the `tuple()` 
# function, an iterable must be passed in as an argument (list here).
my_other_tuple = tuple([1, 2, 4])

# Strings are iterable objects, so passing a string as an argument creates a 
# tuple with the individual characters of the string as elements.
my_str_tuple = tuple("Hello World!")
print(my_str_tuple) 
# Output: ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!')

# To use the `tuple()` function with a single string element, put the string 
# into a list.
my_str_tuple = tuple(["Hello World!"])
print(my_str_tuple) 
# Output: ('Hello World!',)

# Create a single element tuple
my_tuple_1 = tuple([1]) 
my_tuple_2 = (1,) # Note the comma after the single element
my_tuple_3 = 1, # Note the comma after the single element


# Access elements in a tuple using square bracket syntax and indexing
print(my_tuple[0]) # Output: 1
print(my_tuple[1]) # Output: Hello

# Get a subset of a tuple using slicing syntax
print(my_tuple[1:3]) # Output: ('Hello', 3.14)

# Iterating over a tuple using a for loop and the `in` operator
for element in my_tuple:
    print(element)
    # Output: 
    # 1
    # Hello
    # 3.14

# Creating a tuple from a list with the `tuple()` function
my_list = [7, 7.0, "seven"]
constructed_tuple = tuple(my_list)
print(constructed_tuple) # Output: (7, 7.0, 'seven')
    
# Unpacking a tuple (first element into `x`, second into `y`, third into `z`)
x, y, z = my_tuple
print(x) # Output: 1
print(y) # Output: Hello
print(z) # Output: 3.14

# Packing a tuple (multiple elements packed into a single variable)
packed_tuple = 1, 2, 3
print(packed_tuple) # Output: (1, 2, 3)

# Concatenate tuples using the `+` operator
concatenated_tuple = my_tuple + packed_tuple
print(concatenated_tuple) # Output: (1, 'Hello', 3.14, 1, 2, 3)

# Repeat a tuple's elements using the `*` operator
repeated_tuple = my_tuple * 3
print(repeated_tuple) 
# Output: 1, 'Hello', 3.14, 1, 'Hello', 3.14, 1, 'Hello', 3.14)

# Find the number of occurences of an element using the `count()` method
count = concatenated_tuple.count(1)
print(f"`1` is in concatenated_tuple {count} times.")
# Output: `1` is in concatenated_tuple 2 times.

# Find the index of the first occurance of an element using the `index()` 
# method. NOTE: If the element is not present, an error is raised.
index = concatenated_tuple.index(3.14)
print(f"`3.14` is at index {index} in concatenated_tuple.")
# Output: `3.14` is at index 2 in concatenated_tuple.

"""
Author: Jesse Warner
Date: August 1, 2023

The difference between mutable and immutable types is that mutable types can be
changed after creation, but immutable types cannot. Some examples of mutable
types are lists, dictionaries, sets, and user-defined classes. Immutable types
include strings, tuples, numbers, Booleans, and None.

In Python, when you pass an object as an argument to a function or assign it to 
a variable, you are working with references to the object rather than the 
object itself. Understanding the concepts of reference and copy is important 
for understanding how objects are passed and modified in Python. Let's explore 
the concepts of reference and copy in Python:

Reference:
    In Python, variables are references to objects in memory. When you assign 
    an object to a variable or pass it as an argument to a function, the 
    variable or function parameter becomes a reference to that object. If you 
    assign a new value to the variable or modify the object through that 
    reference, the changes are reflected everywhere the reference is used. 
    This behavior applies to mutable objects like lists, dictionaries, and 
    sets.

Copy:
    Sometimes you may want to create an independent copy of an object instead 
    of working with references to the same object. Python provides different 
    methods for creating copies.

        - Shallow Copy: It creates a new object that references the original
          object's elements. However, if the original object contains nested 
          mutable objects (like lists within a list), the copy still references
          those objects.
          
        - Deep Copy: It creates a completely independent copy of the original   
          object and all its nested objects. Changes made to the copy won't 
          affect the original object.

    Copying applies to mutable objects and is less relevant to immutable 
    objects like integers, strings, and tuples.

Understanding the concepts of reference and copy is crucial when working with 
mutable objects in Python to avoid unexpected modifications and maintain data 
integrity.
"""

# Mutable example using a list.
my_list = [1, 2, 3]
print(my_list) # Output: [1, 2, 3]
my_list[0] = 5
print(my_list) # Output: [5, 2, 3]

# Immutable example using a tuple.
my_tuple = (1, 2, 3)
print(my_tuple) # Output: (1, 2, 3)

# Try to change the first element in my_tuple (raises a TypeError)
try:
    my_tuple[0] = 5 # Raises a TypeError.
    print(my_tuple) 
except TypeError:
    print("Cannot modify my_tuple because it is immutable.")

# Set example showing they are mutable, but do not support item assignment
# like lists do.
my_set = {1, 2, 3}
print(my_set) # Output: {1, 2, 3}
my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

# Try to change the first element in my_set (raises a TypeError)
try:
    my_set[0] = 5
    print(my_set) # Raises a TypeError.
except TypeError:
    print("Cannot change my_set[0] to 5. Sets do not support item assignment.")

# *********************** Working with Mutable Objects *************************

import copy

# Define a function that reverses a list
def reverse_list(my_list):
    print(f"my_list before reversing: {my_list}")
    # Output: my_list before reversing: ['ford', 'chevy', 'dodge']

    my_list.reverse()
    print(f"my_list after reversing: {my_list}")
    # Output: my_list after reversing: ['dodge', 'chevy', 'ford']

cars = ["ford", "chevy", "dodge"]
reverse_list(cars)
print(f"cars list after calling reverse_list: {cars}")
# Output: cars list after calling reverse_list: ['dodge', 'chevy', 'ford']

# Create a list of numbers with a list of numbers at index 3
numbers = [1, 2, 3, [4, 5, 6]]

# Make an exact copy of the `numbers` list by creating a new variable and 
# assigning it the value associated with `numbers`
exact_copy = numbers

# Make a shallow copy of the `numbers` list using the built-in list's`copy` 
# method
shallow_copy1 = numbers.copy()

# Make a shallow copy of the `numbers` list using slicing
shallow_copy2 = numbers[:]

# Make a shallow copy of the `numbers` list by using the imported copy module's 
# copy method.
shallow_copy3 = copy.copy(numbers)

# Make a deep copy of the `numbers` list using the `copy.deepcopy()` function 
# and passing it `numbers` as an argument
deep_copy = copy.deepcopy(numbers)

# Check if `numbers` and `exact_copy` are the same object
if numbers is exact_copy:
     print("Yes! numbers and exact_copy are the same object!")
# Output: Yes! numbers and exact_copy are the same object!

# Check if all 5 lists contain the same values 
if numbers == shallow_copy1 == shallow_copy2 == shallow_copy3 == deep_copy:
    print("All 5 lists have the same values!")
# Output: All 5 lists have the same values!

# Check if `numbers` and `shallow_copy1` are the same object
if numbers is shallow_copy1:
    print("numbers and shallow_copy1 are the same object")
else:
    print("numbers and shallow_copy1 are not the same object")
# Output: numbers and shallow_copy1 are not the same object

# Check if the lists inside `numbers` and `shallow_copy1` are the same object
if numbers[3] is shallow_copy1[3]:
    print("The list in numbers and shallow_copy1 are the same object!")
# Output: The list in numbers and shallow_copy1 are the same object!

# Check if the lists inside `numbers` and `shallow_copy2` are the same object
if numbers[3] is shallow_copy2[3]:
    print("The list in numbers and shallow_copy2 are the same object!")
# Output: The list in numbers and shallow_copy1 are the same object!


# Check if the lists inside `numbers` and `deep_copy` are the same object
if numbers[3] is deep_copy[3]:
    print("The list in numbers and deep_copy are the same object!")
else:
    print("The list in numbers and deep_copy are NOT the same object!")
# Output: The list in numbers and deep_copy are NOT the same object!

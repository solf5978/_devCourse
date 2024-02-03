"""
Author: Jesse Warner
Creation Date: August 1, 2023

A set is a built-in data structure that represents an unordered collection of 
unique elements. It is defined by enclosing a comma-separated sequence of 
elements within curly braces {} or by using the `set()` function. Sets can 
also be created from other iterable objects like lists or tuples using the 
`set()` function. All items in a set must be immutable.

Key features of Python sets:
    - Unique Elements: Sets only contain unique elements. If you try to add an
      element that already exists in the set, it will not be added again.

    - Unordered: The elements in a set are not ordered or indexed.

    - Unindexed: Sets can be shown in a different order each time they are used
      and cannot be referred to by index or key.

    - Mutable: Sets are mutable, meaning you can add or remove elements after
      the set is created.

    - Unchangeable: While you can add or remove items, once an item is in a
      set, it cannot be changed.

Common operations and methods you can perform on sets:
    - Creating Sets: Sets can be created using curly braces {} or the `set()`
      function. Elements are separated by commas.

    - Adding Elements: You can add elements to a set using the `add()` method.

    - Removing Elements: You can remove elements from a set using the `remove()`
      or `discard()` method. The `remove()` method raises a KeyError if the 
      element is not found, while the `discard()` method silently ignores the 
      operation.

    - Set Operations: Sets support various mathematical set operations, such as
      union (|), intersection (&), difference (-), and symmetric difference (^).

    - Set Membership: You can check if an element exists in a set using the `in`
      keyword.

    - Set Size: You can find the number of elements in a set using the `len()`
      function.
      
    - Set Methods: Sets provide methods like `copy()`, `clear()`, and `pop()` 
      for various set operations.

Sets are useful when you want to store a collection of unique elements and
perform operations that involve set theory, such as finding common elements,
removing duplicates, or testing for membership. They are particularly efficient
for membership testing and eliminating duplicate elements from other iterables.
"""

# Create a set with unique elements using curly braces.
my_set = {1, 2, 3}
print(f"my_set: {my_set}") 
# Output: my_set1: {1, 2, 3}

# Create a set with duplicate values. 
# NOTE: The duplicate values will be stripped away.
my_set1 = {1, 2, 3, 2, 3}
print(f"my_set1 created with values '1, 2, 3, 2, 3': {my_set1}") 
# Output: my_set1 created with values '1, 2, 3, 2, 3': {1, 2, 3}

# Create a set without duplicate values using the `set()` function. An iterable 
# object must be passed into the set function as an argument.
my_set2 = set([2,3,4])
print(f"my_set2 created with the set function: {my_set2}") 
# Output: my_set2 created with the set function: {2, 3, 4}

# Create a set using set comprehension (Output could be different each time)
my_set3 = {letter for letter in 'abcdabcdabcd' if letter in 'abc'}
print(f"My set created with set comprehension: {my_set3}")
# Output: My set created with set comprehension: {'c', 'b', 'a'}

# Add an element to a set using the set's `add()` method
my_set2.add(5)
print(f"my_set2 after adding 5: {my_set2}") 
# Output: my_set2 after adding 5: {2, 3, 4, 5}

# Remove an element from a set using the set's `remove()` method
my_set2.remove(5)
print(f"my_set2 after removing 5: {my_set2}") 
# Output: my_set2 after removing 5: {2, 3, 4}

# Create a list with duplicate values and use the set() function to convert
# it to a set. 
# NOTE: The duplicate values will be stripped away.
my_list = [1, 1, 2, 3, 3]
my_set4 = set(my_list)
print(f"{my_list} converted to a set: {my_set4}") 
# Output: [1, 1, 2, 3, 3] converted to a set: {1, 2, 3}

# Create a tuple with duplicate values and use the set() function to convert
# it to a set. 
# NOTE: The duplicate values will be stripped away.
my_tuple = (2, 3, 3, 3, 4)
my_set5 = set(my_tuple)
print(f"{my_tuple} converted to a set: {my_set5}")
# Output: (2, 3, 3, 3, 4) converted to a set: {2, 3, 4}

# Use a for loop to iterate over a set and print its values 
for item in my_set1:
    print(item)
    # Output:
    # 1
    # 2
    # 3

# Try to remove the element `4`, which does not exist, from my_set4 using the 
# `remove()` method. 
# NOTE: A try/except block is used to prevent the program from crashing
try:
    my_set4.remove(4)
except KeyError as e:
    print(f"Key {e.args[0]} does not exist in the set.")
# Output: Key 4 does not exist in the set.

# Try to discard the element `4`, which does not exist, from my_set4 using the 
# `remove()` method. 
my_set4.discard(4)
print("Nothing was removed from my_set4, but no error was raised either.")

# Use the `pop()` method to remove and return a random element from the set
print(f"A random element from my set: {my_set4.pop()}")
# Output: A random element from my set: 1

# Clear all elements from my_set4 using the `clear()` method.
my_set4.clear()
print(f"After clearing a set, you are left with: {my_set4}")
# Output: After clearing a set, you are left with: set()

# Delete the set my_set4 using the `del` keyword.
del my_set4

#***************************** Unique Set Methods ******************************
"""
The following `intersection`, `union`, `difference`, and `symmetric_difference` 
methods return new sets that can be assigned to new variables or used in place. 
These methods also have operators that can be used instead: `&` for 
intersection, `|` for union, `-` for difference, and `^` for 
symmetric_difference. The methods intersection, difference, and 
symmetric_difference also have update versions of the method that modifies the 
calling set in place and does not return a new set. To modify a set in place 
using a union, just use the `update` method. The operators to modify the set in 
place are the assignment operators `&=`, `|=`, `-=`, and `^=`.
"""

# Get the intersection of two sets using the `intersection()` method. The 
# intersection of two sets are the elements that are common in both sets.
set_intersection = my_set1.intersection(my_set2)
print(f"Intersection of my_set1 and my_set2: {set_intersection}") 
# Output: Intersection of my_set1 and my_set2: {2, 3}

# The `&` operator can be used instead of the `intersection()` method
set_intersection = my_set1 & my_set2
print(f"Intersection of my_set1 and my_set2 using &: {set_intersection}") 
# Output: Intersection of my_set1 and my_set2 using &: {2, 3}

# Get the union of sets using the `union()` method. The union of sets is all 
# the elements from all sets with any duplicate elements stripped away.
set_union = my_set1.union(my_set2)
print(f"Union of my_set1 and my_set2: {set_union}") 
# Output: Union of my_set1 and my_set2: {1, 2, 3, 4}

# The `|` operator can be used instead of the `union()` method
set_union = my_set1 | my_set2
print(f"Union of my_set1 and my_set2 using |: {set_union}") 
# Output: Union of my_set1 and my_set2: {1, 2, 3, 4}

# Get the difference of sets using the `difference()` method. The difference of 
# sets are the elements from the calling set with any elements that are in 
# common in the other sets removed.
set_difference = my_set1.difference(my_set2)
print(f"Difference of my_set1 and my_set2: {set_difference}") 
# Output: Difference of my_set1 and my_set2: {1}

# The `-` operator can be used instead of the `difference()` method
set_difference = my_set1 - my_set2
print(f"Difference of my_set1 and my_set2 using -: {set_difference}") 
# Output: Difference of my_set1 and my_set2 using -: {1}

# Get the symmetric difference of two sets using the `symmetric_difference()` 
# method. The symmetric difference of two sets are the elements that are in 
# exactly one of the two sets.
set_sym_difference = my_set1.symmetric_difference(my_set2)
print(f"Symmetric difference of my_set1 and my_set2: {set_sym_difference}") 
# Output: Symmetric difference of my_set1 and my_set2: {1, 4}

# The `^` operator can be used instead of the `symmetric_difference()` method
set_sym_difference = my_set1 ^ my_set2
print(f"Symmetric difference of my_set1 and my_set2 using ^: " \
      f"{set_sym_difference}")
# Output: Symmetric difference of my_set1 and my_set2 using ^: {1, 4}

# Get the intersection of `my_set1' and `my_set2` by modifying `my_set1` in 
# place using the `intersection_update()` method.
my_set1.intersection_update(my_set2)
print(f"my_set1 after calling intersection_update: {my_set1}")
# Output: my_set1 after calling intersection_update: {2, 3}

# Get the union of `my_set2' and `my_set3` by modifying `my_set2` in 
# place using the `update()` method.
my_set2.update(my_set3)
print(f"my_set2 after calling update: {my_set2}")
# Output: my_set2 after calling update: {2, 3, 4, 'c', 'a', 'b'}

# Get the difference of `my_set2' and `my_set1` by modifying `my_set2` in 
# place using the `difference_update()` method.
my_set2.difference_update(my_set1)
print(f"my_set2 after calling difference_update: {my_set2}")
# Output: my_set2 after calling difference_update: {4, 'b', 'c', 'a'}

# Get the symmetric difference of `my_set2' and `my_set5` by modifying 
# `my_set2` in place using the `symmetric_difference_update()` method.
my_set2.symmetric_difference_update(my_set5)
print(f"my_set2 after calling symmetric_difference_update: {my_set2}")
# Output: 
# my_set2 after calling symmetric_difference_update: {2, 'b', 'c', 'a', 3}
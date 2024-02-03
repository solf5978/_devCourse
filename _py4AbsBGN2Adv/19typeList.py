"""
Author: Jesse Warner
Creation Date: August 1, 2023

Lists are versatile and widely used in Python due to their flexibility and 
ability to hold different types of data. They are useful for storing 
collections of related items, iterating over elements, and implementing various
algorithms and data structures. 

Lists are ordered, mutable, and can have duplicate values. Lists are
enclosed in square brackets '[]' and are zero-indexed, which means the first
index in the list is [0]. Lists can contain elements of different types,
including numbers, strings, booleans, or even other lists.

Key features of Python lists:
    - Mutable: Lists can have elements added, removed, or changed after the
      list has been created.

    - Ordered: The order of elements in a list is preserved.

    - Indexed: Each element has an index that represents its position, starting
      from 0.

    - Dynamic Size: Lists can grow or shrink dynamically as you add or remove
      elements.

    - Heterogeneous Elements: Lists can contain elements of different data
      types. You can mix integers, floats, strings, booleans, or even other
      tuples within a single tuple.

Common operations and methods you can perform on lists:
    - Creating lists: Lists can be created using square brackets [] or the
      `list()` function. Elements are separated by commas.

    - Accessing Elements: You can access individual elements in a list using  
      square bracket notation and indexing. For example, numbers[0] would 
      return the first element in the list named `numbers`.

    - Slicing: You can extract a portion of a list using slicing. For example,
      numbers[1:4] returns a new list with elements at indices 1, 2, and 3.

    - Modifying Elements: You can change the value of an element in a list by
      assigning a new value to its index. For example, numbers[2] = 10 would
      change the third element to 10.

    - Adding Elements: You can add elements to the end of a list using the
      `append()` method or insert elements at a specific index using the 
      `insert()` method.

    - Removing Elements: You can remove elements from a list using the 
      `remove()` method to remove a specific value, or the `pop()` method to remove and return an element at a given index.

    - List Length: You can find the number of elements in a list using the
      `len()` function.

    - List Concatenation: You can concatenate two lists using the `+` operator.

    - List Methods: Lists provide various methods such as `sort()`, `reverse()`,
      `count()`, and `index()` to perform specific operations on lists.
"""

#******************* Creating Lists and Using List's Methods *******************

# Create an empty list using square brackets.
empty_list = []
print(f"Empty list: {empty_list}") # Output: Empty list: []

# Create a list of animals using the `list()` function and passing in a tuple.
animals = list(("cat", "dog"))
print(f"animals elements: {animals}")
# Output: animals elements: ['cat', 'dog']

# Access an element by using square brackets and an index. Lists are 
# zero-indexed, so the first element starts at index 0.
print(f"First element in animals: {animals[0]}") 
# Output: First element in animals: cat

# Append "fish" to the end of the list using the `append()` method.
animals.append("fish")
print(f"animals after appending \"fish\": {animals}")
# Output: animals after appending "fish": ['cat', 'dog', 'fish']

# Insert elements into animals using the `insert()` method.
animals.insert(1, "pig")
animals.insert(1, "bat")
print(f"animals after inserting elements twice at index 1: {animals}")
# Output: animals after inserting elements twice at index 1: 
# ['cat', 'bat, 'pig', 'dog', 'fish']

# Create a new list `animals_subset` by slicing elements at indexes 3 and 4 from animals. The number to the right of the colon is non-inclusive.
animals_subset = animals[3:5]
print(f"animals_subset after slicing animals: {animals_subset}")
# Output: animals_subset after slicing animals: ['dog', 'fish']

# Concatenate animals and animals_subset using the addition (+) operator.
animals_joined = animals + animals_subset
print(f"animals_joined after concatenating animals and animals_subset: " 
      f"{animals_joined}")
# Output: animals_joined after concatenating animals and animals_subset: 
# ['cat', 'bat', 'pig', 'dog', 'fish', 'dog', 'fish']

# Using the `*` operator to repeat `animals_subset` three times.
repeating_animals = animals_subset * 3
print(f"Repeating animals: {repeating_animals}")
# Output: Repeating animals: ['dog', 'fish', 'dog', 'fish', 'dog', 'fish']

# Extend the `animals` list with `animals_subset` list using the `extend()` 
# method.
animals.extend(animals_subset)
print(f"animals after extending the list with animals_subset: {animals}")
# Output: animals after extending the list with animals_subset: 
# ['cat', 'bat', 'pig', 'dog', 'fish', 'dog', 'fish']

# Use the `len()` function to get the number of elements in `animals`.
print(f"The length of animals: {len(animals)}")
# Output: The length of animals: 7

# Change the value of the fourth element (index 3) in animals to rabbit
animals[3] = "rabbit"
print(f"animals after changing the fourth element: {animals}")
# Output: animals after changing the fourth element: 
# ['cat', 'bat', 'pig', 'rabbit', 'fish', 'dog', 'fish']

# Change the value of the last element by using negative indexing. The elements 
# using negative indexing start with the last element at -1 and go down 
# (-2, -3, etc.)
animals[-1] = "pig"
print(f"animals after changing a value with negative indexing: {animals}")
# Output: animals after changing a value with negative indexing: 
# ['cat', 'bat', 'pig', 'rabbit', 'fish', 'dog', 'pig']

# Count the number of occurrences of a value in a list using the `count()` 
# method.
print(f"pig is in animals {animals.count('pig')} times!")
# Output: pig is in animals 2 times!

# Remove the first occurrence of "pig" from `animals` using the `remove()` 
# method. NOTE: This method raises an error if the value does not exist.
animals.remove("pig")
print(f"animals after removing element \"pig\": {animals}")
# Output: animals after removing element "pig": 
# ['cat', 'bat', 'rabbit', 'fish', 'dog', 'pig']

# Remove and return the last element (pig) in `animals` using the `pop()` 
# method.
last_animal = animals.pop()
print(f"Last animal in animals: {last_animal}")
# Output: Last animal in animals: pig

print(f"animals after popping the last element: {animals}")
# Output: animals after popping the last element: 
# ['cat', 'bat', 'rabbit', 'fish', 'dog']

# Pop the element at index 1 from `animals` (bat)
animals.pop(1)
print(f"animals after popping element at index 1: {animals}")
# Output: animals after popping element at index 1: 
# ['cat', 'rabbit', 'fish', 'dog']

# Delete an element from animals (fish at index 2) using the `del` keyword. 
# NOTE: `del` is not list specific and can delete other objects.
del animals[2]
print(f"animals after deleting element at index 2: {animals}")
# Output: animals after deleting element at index 2: ['cat', 'rabbit', 'dog']

# Return a new list of animals in sorted order using the `sorted()` function.
sorted_animals = sorted(animals)
print(f"animals sorted in ascending order: {sorted_animals}")
# Output: animals sorted in ascending order: ['cat', 'dog', 'rabbit']

# Sort animals in place in ascending order using the `sort()` method
animals.sort()
print(f"animals sorted in place in ascending order: {animals}")
# animals sorted in place in ascending order: ['cat', 'dog', 'rabbit']

# Sort animals in descending order using the `sort()` method with the argument 
# `reverse` equal to 'True'
animals.sort(reverse=True)
print(f"animals sorted in descending order: {animals}")

# Reverse a list's order using the `reverse()` method. 
# NOTE: This is not a sort, it only reverses the order of elements in the list.
animals.reverse()
print(f"animals in reversed order: {animals}")
# Output: animals in reversed order: ['cat', 'dog', 'rabbit']

# Append 'duck' to the animal list
animals.append('duck')

# Sort animals using the `len()` function to sort elements by their character 
# length
animals.sort(key=len)
print(f"animals sorted by their length: {animals}")
# Output: animals sorted by their length: ['cat', 'dog', 'duck', 'rabbit']

# Use the `in` operator to check if the list contains a value
if "cat" in animals:
    print("Yes! \"cat\" is in animals!")
    # Output: Yes! "cat" is in animals!

# Use a for loop to output the animals in the `animals` list
for animal in animals:
    print(animal)
    # Output:
    # cat
    # dog
    # duck
    # rabbit

# Get the index of the first occurence of a value using the `index()` method. 
# NOTE: This method raises an error if the value does not exists in the list.
index = animals.index('duck')
print(f"'duck' is at index {index}")
# Output: 'duck' is at index 2

# Empty the list using the `clear()` method
animals.clear()
print(f"Animals list after using `clear()`: {animals}")
# Output: Animals list after using `clear()`: []

#************************** Multi-Dimensional Lists ****************************

# A list containing three lists with three elements each
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Print the element `5` in `matrix` by using square bracket syntax twice. 
# The element 5 is at the first index of the outer list and the first index of 
# the inner list.
print(f"The number at index 1 of the list at index 1: {matrix[1][1]}")
# Output: The number at index 1 of the list at index 1: 5

# A list containing three lists with three elements each. The second element of the second inner list contains a list.
three_dimensional_list = [[1, 2, 3],
                          [4, [10, 11, 12], 6],
                          [7, 8, 9]]

# Print the element `10` in `three_dimensional_list` by using square bracket 
# syntax three times. 
print(f"The number at index 1 of index 1 of index 0: "
      f"{three_dimensional_list[1][1][0]}")
# Output: The number at index 1 of index 1 of index 0: 10

# ***************************** Copying Lists ********************************

# Import the copy module
import copy

# Create a list of numbers with a list of numbers at index 3
numbers = [1, 2, 3, [4, 5, 6]]

# Make an exact copy of the `numbers` list by creating a new variable and 
# assigning it the value associated with `numbers`
exact_copy = numbers

# Make a shallow copy of the `numbers` list using the `copy()` method
shallow_copy1 = numbers.copy()

# Make a shallow copy of the `numbers` list using slicing syntax
shallow_copy2 = numbers[:]

# Make a deep copy of the `numbers` list using the `copy.deepcopy()` method 
# and passing it `numbers` as an argument
deep_copy = copy.deepcopy(numbers)

# Check if `numbers` and `exact_copy` are the same object
if numbers is exact_copy:
     print("Yes! numbers and exact_copy are the same object!")
# Output: Yes! numbers and exact_copy are the same object!

# Check if all 5 lists contain the same values 
if numbers == exact_copy == shallow_copy1 == shallow_copy2 == deep_copy:
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

# **************************** Pitfall With Lists ******************************
"""
What is important to notice here is that although the function `reverse_list` 
is reversing the list that is passed in as an argument (`my_list`), it is 
changing the original list `cars` too. This is because lists are mutable 
objects. When an integer (`my_number`) is passed into the function `add_five`, 
it remains 10 after the function call because it is immutable.
"""
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

# Define a function that adds 5 to a number
def add_five(number):
    number += 5

my_number = 10
add_five(my_number)
print(f"my_number after calling add_five: {my_number}")
# Output: my_number after calling add_five: 10

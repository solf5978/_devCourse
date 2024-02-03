"""
Author: Jesse Warner
Date: August 1, 2023

In this activity, you are going to practice working with lists, list methods, 
and list comprehension.
"""
# List to work with
numbers = [24, 57, 36, 99, 105]

# Use Python's built-in `sum` function to get the output of all the numbers in 
# the list
print(sum(numbers)) # Output: 321

# Create a new list by using list comprehension to divide each value in the 
# numbers list by 3 and output the new list.
numbers_div = [num / 3 for num in numbers]
print(numbers_div) # Output: [8.0, 19.0, 12.0, 33.0, 35.0]

# Output the sum of the new list.
print(sum(numbers_div)) # Output: 107.0

# In a single statement, output the value of the sum of the numbers list plus 
# the sum of the new list, but you can only call the sum function once, and you 
# cannot modify the numbers or new list. HINT: Use c___________n
print(sum(numbers + numbers_div)) # Output: 428.0

# Extend the numbers list with a list containing the values 48, 36, and 3.
new_list = [48, 36, 3]
numbers.extend(new_list)

# Remove and return the first item in the numbers list and print it to the 
# console.
print(numbers.pop(0)) # Output: 24

# Remove and return the last item in the numbers list using negative indexing 
# and print it to the console.
print(numbers.pop(-1)) # Output: 3

# Output the number of times 36 is in the numbers list
print(numbers.count(36)) # Output: 2

# Output the index of 99 in the numbers list
print(numbers.index(99)) # Output: 2

# Using slice notation, output the second through the second to last item of 
# the numbers list.
print(numbers[1:-1]) # Output: [36, 99, 105, 48]

# Insert the value 50 into the numbers list before index 3 and output the 
# list
numbers.insert(3, 50)
print(numbers) # Output: [57, 36, 99, 50, 105, 48, 36]

# Reverse the list and output it
numbers.reverse()
print(numbers) # Output: [36, 48, 105, 50, 99, 36, 57]

# Sort the list in ascending order and output the list
numbers.sort()
print(numbers) # Output: 36, 36, 48, 50, 57, 99, 105]

# Remove all the items from the numbers list and print the empty list.
numbers.clear()
print(numbers) # Output: []

# Delete the new list to clear it from memory.
del numbers_div
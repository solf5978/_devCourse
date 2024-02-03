"""
Author: Jesse Warner
Date: August 1, 2023

In this activity, you are going to practice working with lists, list methods, 
and list comprehension.
"""
# List to work with
numbers = [24, 57, 36, 99, 105]

# Use Python's built-in `sum` function to output the sum of all the numbers in 
# the list
sum_all = sum(numbers)
# Create a new list by using list comprehension to divide each value in the 
# numbers list by 3 and output the new list.
new_list = [num / 3 for num in numbers]
# Output the sum of the new list.
sum(new_list)
# In a single statement, output the value of the sum of the numbers list plus 
# the sum of the new list, but you can only call the sum function once, and you 
# cannot modify the numbers or new list. HINT: Use c___________n
sum(numbers + new_list)
# Extend the numbers list with a list containing the values 48, 36, and 3.
numbers.append([48, 36, 3])
# Remove and return the first item in the numbers list and print it to the 
# console.
print(numbers.pop())
# Remove and return the last item in the numbers list using negative indexing 
# and print it to the console.
print(numbers.pop(-1))
# Output the number of times 36 is in the numbers list
print(numbers.count(36))
# Output the index of 99 in the numbers list
print(numbers.index(99))
# Using slice notation, output the second through the second to last item of 
# the numbers list.
print(numbers[1:-1])
# Insert the value 50 into the numbers list before index 3 and output the 
# list
numbers.insert(3, 50)
# Reverse the list and output it
numbers.reverse()
# Sort the list in ascending order and output the list
numbers.sort()
# Remove all the items from the numbers list and print the empty list.
print(number.clear())
# Delete the new list to clear it from memory.
del new_list
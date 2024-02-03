"""
Author: Jesse Warner
Date: August 1, 2023

For this challenge, you are going to practice working with sets and their 
methods. For each activity that may involve an operator, you may use the 
operator or the built-in method, but I encourage you to try out both! 

HINT: Some methods update the sets in place and return the value None.
"""

# Create a set containing the elements 1-4
set1 = {1, 2, 3, 4}

# Create a set containing the elements 3-6
set2 = {3, 4, 5, 6}

# Create a set containing the elements 7-8
set3 = {7, 8}

# Output the union of all the sets
print(set1.union(set2, set3)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Output the intersection of the first and second sets
print(set1 & set2) # Output: {3, 4}

# Output the symmetric difference between the first and second sets
print(set1 ^ set2) # Output: {1, 2, 5, 6}

# Output the difference between the first and second sets, and the second and 
# first sets
print(set1.difference(set2)) # Output: {1, 2}
print(set2 - set1) # Output: {5, 6}

# Add the element 5 to the first set
set1.add(5)

# Remove the element 6 from the second set
set2.remove(6)

# Output the Boolean value of whether the first set is a superset of set two
print(set1.issuperset(set2)) # Output: True

# Output the Boolean value of whether the second set is a subset of set one
print(set2.issubset(set1)) # Output: True

# Output the Boolean value of whether the first set is a subset of set two
print(set1.issubset(set2)) # Output: False

# Output the Boolean value of whether the third set has no common elements with 
# the union of the first and second sets
print(set3.isdisjoint(set1 | set2)) # Output: True

# Modify the first set in place by adding sets two and three to it and output 
# it. (Output should not be None)
set1.update(set2, set3)
print(set1) # Output: {1, 2, 3, 4, 5, 7, 8}

# Remove all the elements from the second set and print it (Output should not 
# be None)
set2.clear()
print(set2) # Output: set()

# Delete the third set
del set3

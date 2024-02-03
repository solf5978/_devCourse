"""
Author: Jesse Warner
Date: August 1, 2023

For this challenge, you are going to practice working with sets and their 
methods. For each activity that may involve an operator, you may use the 
operator or the built-in method, but I encourage you to try out both! 

HINT: Some methods update the sets in place and return the value None.
"""

# Create a set containing the elements 1-4
set1_4 = {1, 2, 3, 4}
# Create a set containing the elements 3-6
set3_6 = {3, 4, 5, 6}
# Create a set containing the elements 7-8
set7_8 = set([7, 8])
# Output the union of all the sets
print(set1_4.union(set3_6, set7_8))
print(set1_4 | set3_6 | set7_8)
# Output the intersection of the first and second sets
print(set1_4.intersection(set3_6))
# Output the symmetric difference between the first and second sets
print(set1_4.symmetric_difference(set3_6))
# Output the difference between the first and second sets, and the second and 
# first sets
print(set1_4.difference(set3_6))
print(set3_6.difference(set1_4))
# Add the element 5 to the first set
set1_4.add(5)
# Remove the element 6 from the second set
set3_6.remove(6)
# Output the Boolean value of whether the first set is a superset of set two
print(set1_4.issuperset(set3_6))
# Output the Boolean value of whether the second set is a subset of set one
print(set3_6.issubset(set1_4))
# Output the Boolean value of whether the first set is a subset of set two
print(set1_4.issubset(set3_6))
# Output the Boolean value of whether the third set has no common elements with 
# the union of the first and second sets
print(set7_8.isdisjoint(set1_4.union(set3_6)))
# Modify the first set in place by adding sets two and three to it and output 
# it. (Output should not be None)
set1_4.update(set3_6, set7_8)
# Remove all the elements from the second set and print it (Output should not 
# be None)
print(set3_6.clear())
# Delete the third set
del set7_8
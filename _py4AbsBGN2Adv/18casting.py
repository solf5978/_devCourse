"""
Author: Jesse Warner
Creation Date: August 1, 2023

Casting is the process of converting one data type to another. It allows the
programmer to change the variable or value to match the data type for an
operation or requirement. Python provides several built-in functions for casting
or type conversion.

Casting is beneficial when you need to perform operations that are for a 
specific data type or you need to ensure data compatibility. However, not all 
types of casting are possible or meaningful. Trying to convert a string that 
does not contain the correct value to an integer will raise a ValueError.
"""

# Converting a float to an integer using the `int()` function removes the 
# decimals and returns the whole number.
my_int = int(3.14)
print(my_int) # Output: 3

# Converting a string to a float using the `float()` function will change the 
# data type from string to float.
my_float = float("7.77")
print(my_float) # Output: 7.77

# Converting a float to a string using the `str()` function will change the 
# numeric value to a string representation of that value.
my_string = str(3.14)
print(type(my_string), my_string) # Output: <class 'str'> 3.14

# Converting a value to a boolean will return True, if the object is "truthy" 
# and False, if the object is "falsy"
my_true = bool(1234)
my_false = bool(0)
print("bool(1234) is:", my_true) # Output: bool(1234) is: True
print("bool(0) is:", my_false) # Output: bool(0) is: False

# Converting a string to a list using the `list()` function takes the 
# individual characters from the string and makes them separate elements of a 
# list.
my_list = list("Hello")
print(my_list) # Output: ['H', 'e', 'l', 'l', 'o']

# Convert a list to a tuple using the `tuple()` function
my_tuple = tuple([1, 2, 3])
print(my_tuple) # Output: (1, 2, 3)

# Converting a list to a set using the `set()` function will create a set with 
# any duplicate values in the list removed.
my_set = set([1, 2, 2, 3])
print(my_set) # Output: {1, 2, 3}

# Convert a list containing tuples of key-value pairs into a dictionary using 
# the `dict()` function. The inner collection (tuples shown here) must contain 
# two elements. The first element must be an immutable data type, and the 
# second element can be any data type.
my_dict = dict([("name", "John"), ("age", 30)])
print(my_dict) # Output: {'name': 'John', 'age': 30}

# Convert an integer to a Unicode character using the `chr()` function.
my_char = chr(65)
print(my_char) # Output: A

# Convert a Unicode character to its corresponding integer using the `ord()` 
# function
my_unicode = ord('A')
print(my_unicode) # Output: 65

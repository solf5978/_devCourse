"""
Author: Jesse Warner
Creation Date: August 1, 2023

A variable is a named location in memory that can be used to store data. In 
Python, all data is represented by objects, which includes things like numbers, 
strings, lists, dictionaries, and even functions. To create a variable, you 
give it a name and assign it a value. Then, you can use the variable name to 
refer to the value (object). 

When you create a variable, you are creating a reference to an object. The 
variable itself is not the object but a way to access the object in memory. 
Unlike many other languages, Python is dynamically typed, meaning that the 
variable type is not declared when it is created. Instead, the variable's type 
is inferred from the value passed into it and can change afterward. 

Rules for naming variables in Python:
    - Variable names can only contain alphanumeric characters and the underscore
      character.
    - Variable names must start with a letter or the underscore character.
    - Variable names cannot contain spaces.
    - Variable names cannot contain special characters.
    - Variable names are case-sensitive.

Tips for naming variables in Python:
    - Use short variable names, but make sure they are descriptive.
    - Avoid using abbreviations in variable names.
    - Avoid using acronyms in variable names unless they are very well-known.
    - Use consistent capitalization in variable names.
    - Use meaningful names for your variables.
"""

# Create the variable `age` and assign it the value `10` using the assignment 
# operator (=), and output the information using the `print()` function.
age = 10
print(age) # Output: 10

# Create the variable `name` and assign it the value `Tim`
name = "Tim"
print(name) # Output: Tim

# Assign an integer to `x` then change `x` to a string value. Since variables 
# in Python are dynamic, the data type can change too.
x = 7
x = "seven"
print(x) # Output: seven

# Determine the data type of a variable using the `type()` function. The 
# variable `age_type` is assigned the value returned by the `type()` function 
# with the variable `age` passed into it, and the `type()` function with the 
# variable `name` passed into it is passed into the `print()` function directly.
age_type = type(age)
print(age_type) # Output: <class 'int'>
print(type(name)) # Output: <class 'str'>

# Add two variables together using the additional operator (+) and assign the 
# value to a third variable `num3`.
num1 = 3
num2 = 4
num3 = num1 + num2
print(num3) # Output: 7

# Assign multiple values to multiple variables by separating the variables and 
# values with a comma.
a, b, c = "Apple", "Banana", "Coconut"
print(a) # Output: Apple
print(b) # Output: Banana
print(c) # Output: Coconut

# Assign one value to multiple variables by using successive assignment 
# operators (=).
d = e = "Fruit"
print(d) # Output: Fruit
print(e) # Output: Fruit

# Variable names can only contain letters, numbers, and underscores and must
# start with a letter or underscore.
mynumber = 3
my_number = 4
myNumber = 5
MyNumber = 6
my_number_1 = 1
_my_number_9 = 9
MY_NUMBER = 7
# 8_my_number = 8 # Raises a SyntaxError if the # is removed.

# Variable names are case-sensitive, so `dog` and `DOG` are two different 
# variables.
dog = "Poodle"
DOG = "Hound"
print(dog) # Output: Poodle
print(DOG) # Output: Hound
# print(Dog) Raises a NameError because no variable named `Dog` exists
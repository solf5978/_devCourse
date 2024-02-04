"""
Author: Jesse Warner
Date: August 1, 2023

A module is a file containing Python code that defines functions, classes, and 
variables. It allows you to organize and reuse code by splitting it into 
separate files. Modules provide a way to encapsulate related code and make it 
more manageable. To use a module in Python, you need to `import` it into your 
program. The `import` statement is used for this purpose and should go at the 
top of Python file. 

Syntax to import a module:
    - import module_name: This syntax is used to import a module and 
      executes its contents. This allows you to access the functions,
      variables, and classes defined in that module.

    - import module_name as alias: This syntax is used to import a module and 
      give it an alternative name or alias. This can be useful when you want to 
      refer to the module using a shorter or more convenient name in your code.

    - from module_name import (variable, function, class): This syntax allows 
      you to import specific objects (variables, functions, classes) or 
      submodules from a module directly into your current namespace. This means 
      you can use the imported objects without having to reference the module 
      name every time.
"""

#******************** Import built-in Python `math` Module *********************

import math # Import statement to import the `math` module

# Assign value to a variable using the imported math module and dot notation to 
# access its factorial method
x = math.factorial(5)
print(f"Factorial of 5: {x}") # Output: Factorial of 5: 120

#*********** Import Specific Components of the Python `math` Module ************

from math import sqrt # Import the `sqrt` method from the `math` module
from math import sin, cos, tan # Import multiple methods from the `math` module

# Assign values to variables using the multiple imported math module's methods
a = sin(1)
b = cos(1)
c = tan(1)
print(f"Sine 1: {a:.5f} - Cosine 1: {b:.5f} - Tangent 1: {c:.5f}")
# Output: Sine 1: 0.84147 - Cosine 1: 0.54030 - Tangent 1: 1.55741

# Assign a value to a variable using the imported math module's sqrt method
y = sqrt(16)
print(f"Squareroot of 16: {y}") # Output: Squareroot of 16: 4.0

#************ Import Built-In Python Module `random` With An Alias *************

import random as r # Import `random` as `r` so we don't have to type `random`

# Assign a random integer to a variable using the alias created for the random 
# module and dot notation to access the random module's methods
z = r.randint(1, 10)
print(f"Random number: {z}") # Output: Random number: (random generated number)

#****************** Import User-Made `string_utility` Module *******************

# Import user-made custom module string_utility.py and give it an alias. 
# NOTE: There must be a file with the import name in the same folder as this 
# Python file, or you must add the folder where the module is to the `sys.path`
# list or the PYTHONPATH environment variable) 
import string_utility as su 

# Create a string to use with the custom module `string_utility`
message = "Hello, Cold World!"

# Use the custom module's `snowmanify` function to add snowmen to the string
message = su.snowmanify(message)
print(message) # Output: ☃☃ Hello, Cold World! ☃☃

# Use the custom module's `desnowmanify` function to remove snowmen from the 
# string
message = su.desnowmanify(message)
print(message) # Output: Hello, Cold World!

#******************** Import User-Made `import_me` Module **********************

"""
One issue that could arise when making and importing custom modules is code 
from the imported module executing when the current script is executed. When a 
Python script is executed, the Python interpreter sets the built-in variable 
__name__ to the string "__main__" for the script that is being run. This 
indicates that the script is the main program being executed. When a script is 
imported as a module into another script, the __name__ variable is set to the 
name of the module. 
"""

# Import the import_me.py file
import import_me
print("Hello from Modules!")
# Output: 
# This is a regular statement inside the script.
# Hello from Modules!

# If you remove the `if` condition above the `main()` function in import_me.py, 
# you would also get the following output: 
#   This is the main function in the import_me.py file

#********************** Import Third-Party `numpy` Module **********************

# Import a third-party module called `numpy` (must be installed)
import numpy as np

# Create an array using the third-party numpy module
my_array = np.array([1, 4, 5, 2, 3])

# Sort the array
my_array = np.sort(my_array)
print(f"Sorted array: {my_array}")
# Output: Sorted array: [1 2 3 4 5]



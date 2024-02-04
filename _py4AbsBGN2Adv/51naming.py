"""
Author: Jesse Warner
Date: August 1, 2023

Programming languages typically have a naming convention that most users have 
adopted. Sometimes companies will specify their own naming convention when 
doing work for them. Naming conventions help make the code more readable and 
allow others to better understand and collaborate on your code. It is important 
that all names are descriptive and meaningful.

Common naming conventions in Python:
    - Variables, functions, methods, modules, packages: Use snake case, which 
      uses lowercase letters and separate words with underscores.

    - Constant Name: Uppercase letters and separate words with underscores.

    - Private Name: prefix the name with an underscore, lowercase letters, and
      separate words with underscores. It is important to note that Python does
      not enforce private variables, functions, methods, etc. This is just a 
      convention to help indicate how they should be used.

    - Class Name: Use PascalCase where each word starts with an uppercase 
      letter.
      
    - Special Name: Python uses special names that have specific meanings, such
      as constructors that start and end with double underscores.
"""

# Create a class using PascalCase for the name.
class MyClass:
    # Variable that starts with an underscore to indicate it should be private.
    _number = 0

    # All uppercase indicates a constant value that should never change.
    TRIPLER = 3

    # The constructor `__init__()`, which starts and ends with double 
    # underscores.
    def __init__(self, number):
        self._number = number

    # A setter class method that uses snake case and sets the private variable.
    def set_number(self, number):
        self._number = number

    # A getter class method that uses snake case and returns the private 
    # variable
    def get_number(self):
        return self._number
    

# Create the variable `my_number` using snake case for the name, and assign it 
# the value of a new `MyClass` object instantiated with a 5.
my_number = MyClass(5)

# Call the `get_number()` method in the `my_number` object and print the value
print(my_number.get_number()) # Output: 5

# Use the `set_number` method to change `_number` in `my_number` to 10
my_number.set_number(10)
print(my_number.get_number()) # Output: 10

# Use the constant variable `TRIPLER` in `my_number` to triple the value 
# returned by the `get_number()` method.
print(my_number.get_number() * my_number.TRIPLER) # Ouput: 30
"""
Author: Jesse Warner
Date: August 1, 2023

While Python is a powerful and flexible programming language, there are some 
common pitfalls that developers may encounter. Here are a few of them:

    - Mutable Default Arguments:A common pitfall is using mutable objects (such 
      as lists or dictionaries) as default arguments in function definitions.
      The problem is if the mutable default argument is modified within the 
      function, the changes persist across multiple function calls. To avoid 
      this, it is recommended to use immutable objects (like None) as default 
      arguments and handle mutable objects inside the function.

    - Modifying Iterables During Iteration: Modifying an iterable (such as a 
      list or dictionary) while iterating over it can lead to unexpected 
      behavior or errors. If you need to modify an iterable, it's better to 
      create a copy or use techniques like list comprehension to generate a new 
      iterable.

    - Unintended Variable References: For mutable objects, Python uses
      references to the object, and assigning one variable to another does not 
      create a new copy of the object. Modifying one variable can affect other 
      variables that reference the same object. It's important to understand 
      object references and use techniques like copying or creating new objects 
      when needed.

    - Mixing Tabs and Spaces for Indentation: Python relies on consistent 
      indentation to define code blocks. Mixing tabs and spaces for indentation 
      can lead to syntax errors. It's recommended to use spaces for indentation 
      and configure your editor to convert tabs to spaces. Try/except blocks do 
      not catch IndentationErrors because they happen during the parsing phase 
      before the code is executed.

    - Unhandled Exceptions: Failing to handle exceptions properly can result in 
      program crashes or unexpected behavior. It's good practice to use 
      try-except blocks to catch and handle exceptions appropriately, 
      preventing your program from terminating abruptly.
      
    - Floating-Point Precision: Due to the way floating-point numbers are 
      represented in computers, performing calculations with floats can 
      sometimes lead to unexpected results. It's important to be aware of 
      floating-point precision limitations and consider using the decimal 
      module or other techniques for precise calculations involving decimal 
      numbers.

These are just a few common pitfalls in Python programming. It's always 
recommended to carefully review and test your code, follow best practices, and 
leverage the rich set of Python's built-in functions and libraries to avoid 
potential issues.
"""

#************************** Mutable Default Argument ***************************

# Add an item to a list if one is passed in or use the default list.
def add_item_wrong(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item_wrong('dog'))  # Output: ['dog']
print(add_item_wrong('cat'))  # Output: ['dog', 'cat']
print(add_item_wrong('rabbit'))  # Output: ['dog', 'cat', 'rabbit']

# Add an item to a list if one is passed in or create an empty list
def add_item_correct(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item_correct('dog'))  # Output: ['dog']
print(add_item_correct('cat'))  # Output: ['cat']
print(add_item_correct('rabbit'))  # Output: ['rabbit']


#******************** Modifying Iterables During Iteration *********************
# Incorrect way
animals = ['kangaroo', 'lion', 'tiger', 'bear']

"""
Loop through animals, and if the current animal is 'lion', remove it. When 
lion is removed, tiger moves to index 1 and bear moves to index 2. Since 
the iteration was on index 1 it goes to index 2, which is now bear, and skips 
over tiger.
"""
for animal in animals:
    print(animal)
    if animal == 'lion':
        animals.remove(animal)
# Output:
# kangaroo
# lion
# bear

print(animals)  # Output: ['kangaroo', 'tiger', 'bear']

# One of many correct ways
animals = ['kangaroo', 'lion', 'tiger', 'bear']

# Loop through a copy of the animals list by using index slicing [:]. When 
# lion is removed from the original list, the copy is unaffected and 
# continues the iteration correctly.
for animal in animals[:]:
    print(animal)
    if animal == 'lion':
        animals.remove(animal)
# Output:
# kangaroo
# lion
# tiger
# bear

print(animals)  # Output: ['kangaroo', 'tiger', 'bear']

#*********************** Unintended Variable References ************************
list1 = [1, 2, 3]
list2 = list1

list2.append(4)

# Because list1 and list2 are mutable and reference the same object, list1 
# shows the 4 appended to the end of it
print(f"list1 after appending 4 to list2: {list1}")  
# Output: list1 after appending 4 to list2: [1, 2, 3, 4]

x = 10
y = x

y = 20
# Since x is an integer and immutable, changing y to 20 does not affect x
print(f"x after changing y to 20: {x}")  
# Output: x after changing y to 20: 10

#******************* Mixing Tabs and Spaces for Indentation ********************

print("It's True!") # Output: It's True!
#    print("I know!") # Raises an IndentationError if the first # is removed

#**************************** Unhandled Exceptions *****************************

# Defines a function that divides the first argument by the second. Does not 
# account for the second argument being 0, which causes a ZeroDivisionError to 
# be raised.
def divide_numbers_wrong(a, b):
    result = a / b
    return result

num1 = 10
num2 = 0
# result = divide_numbers_wrong(num1, num2) # Raises a ZeroDivisionError

# Defines a function that divides the first argument by the second and 
# correctly handles the second argument being 0.
def divide_numbers_correct(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

# Call `divide_numbers_correct` using num1 (10) and num2 (0) as arguments
result = divide_numbers_correct(num1, num2)
# Output: Error: Division by zero is not allowed!

print(result) 
# Output: None (No explicit return statement exists in the except block, so the 
# function defaults to returning None)

#************************** Floating-Point Precision ***************************

a = 0.1
b = 0.2
c = 0.3

"""
The decimal values 0.1 and 0.2 cannot be represented precisely as binary 
fractions. Therefore, when these numbers are added together, the result is a 
slightly imprecise value. As a result, the comparison with the expected value 
of 0.3 fails. Math functions such as math.isclose() can be used if perfect 
precision is not necessary.
"""
if a + b == c:
    print("Equal")
else:
    print("Not equal")
# Output: Not equal

print(f"a(0.1) + b(0.2) = {a + b}") 
# Output: a(0.1) + b(0.2) = 0.30000000000000004


"""
Author: Jesse Warner
Creation Date: August 1, 2023

List comprehension is a concise and expressive way to create new lists in 
Python. It allows you to define a new list by transforming or filtering an 
existing iterable, such as a list, string, or range. The syntax of list 
comprehension follows a specific pattern:

    new_list = [expression for item in iterable if condition]

The components of list comprehension are as follows:
    - expression: The expression that defines how each item in the new list 
      should be computed or transformed.

    - item: A variable that represents each item in the iterable.

    - iterable: The existing iterable from which the items are taken.

    - condition: An optional condition that filters the items based on a 
    Boolean expression. Only items that satisfy the condition will be included 
    in the new list.

List comprehensions are concise and readable, allowing you to perform complex 
transformations and filtering operations on iterables in a single line of code. 
They are a powerful tool for creating new lists based on existing data.
"""

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Create a new list with each number squared.
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
"""
`num ** 2` is the expression, `num` is the item, and `numbers` is the iterable. Each element in the list `numbers` is going to be evaluated in the expression and the result is going to be added to the new list.
"""

# Create a new list with only the even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4]
"""
Here, `num` is the expression and the item, `numbers` is the iterable, and 
`num % 2 == 0` is the condition. When the condition evaluates to True (2 and 4 in this example), the result of the expression is added to the new list. Since the expression is just the variable `num` that is what gets added to the list.
"""

# Since the object created using list comprehension is a list, you can use the 
# result like you would any other list.
for number in [num for num in numbers if num % 2 == 0]:
    print(number)
    # Output:
    # 2
    # 4
"""
This code is equivalent to the following:
    for number in even_numbers:
        print(number)
This example was to show that you did not necessarily need to put the new list created by list comprehension in a variable to use it. However, putting the new list in a variable and then using the variable makes the code easier to read and is the better option.
"""
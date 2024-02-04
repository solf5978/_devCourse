"""
Author: Jesse Warner
Creation Date: August 1, 2023

The boolean data type represents the concept of truth values, which can either 
be `True` or `False`. Booleans are used to perform logical operations, control 
program flow, and make condition-based decisions.

Key concepts about Booleans:
    - Values: The boolean data type has two possible values: `True` and `False`.
      These values are case-sensitive, so they should be written with an 
      uppercase first letter (`True` and `False`).

    - Logical Operations: Booleans are often used in conjunction with logical 
      operators to evaluate conditions and perform logical operations.
        - Logical AND: `and`
        - Logical OR: `or`
        - Logical NOT: `not`

    - Comparison Operators: Booleans are often obtained by comparing values 
      using comparison operators. These operators return True or False based on 
      the comparison result.
        - Equal to: `==`
        - Not equal to: `!=`
        - Greater than: `>`
        - Less than: `<`
        - Greater than or equal to: `>=`
        - Less than or equal to: `<=`

    - Truthiness and Falsiness: In addition to the explicit `True` and `False` 
      values, Python has the concept of "truthy" and "falsy" values. Certain 
      values, such as non-zero numbers and non-empty containers (e.g., 
      non-empty strings, lists, etc.), are considered "truthy" and evaluate to 
      `True` in a boolean context. Conversely, values like `0`, `None`, empty 
      strings, and empty containers are considered "falsy" and evaluate to 
      `False`.

    - Boolean Functions: Python provides built-in functions that work with 
      booleans, such as `bool()` to explicitly convert a value to a boolean, 
      `all()` to check if all elements in an iterable are true, and `any()` to 
      check if any element in an iterable is true.

    - `is` and 'is not' Operators: The `is` keyword is used for identity 
      comparison to determine if two variables are the same object in memory. 
      With immutable types such as strings or numbers, variables that have the 
      same value point to the same object in memory. However, mutable types 
      such as lists can have the same value but point to different objects in 
      memory. The `not` keyword can be used to negate the boolean.
        - `is`: Returns `True` if two variables refer to the same object.
        - `is not`: Returns `True` if two variables do not refer to the same 
          object.

    - `in` and `not in` Operators: The `in' keyword is used to check if a value 
      is present in a sequence or collection, such as a string, list, set, or 
      tuple. These operators return a boolean value indicating the result of the membership test.
        - `in`: Returns `True` if a value is present in a sequence.
        - `not in`: Returns `True` if a value is not present in a sequence.


Truth tables for `and`, `or`, and `not`:
    A     B     A and B
    -------------------
    True  True   True
    True  False  False
    False True   False
    False False  False

    A     B     A or B
    ------------------
    True  True   True
    True  False  True
    False True   True
    False False  False

    A     not A
    ------------
    True  False
    False True
"""

# Initialize some values to perform comparisons on
a = 5
b = 10
c = 10
d = 15

#********************* Booleans Using Comparison Operators *********************

# Equality operator (==) with `False` evaluation
result = a == b
print(f"Is 5 equal to 10: {result}") 
# Output: Is 5 equal to 10: False

# Equality operator (==) with `True` evaluation
result = b == c
print(f"Is 10 equal to 10: {result}")
# Output: Is 10 equal to 10: True

# Inequality Operator (!=) with `True` evaluation
result = a != b
print(f"Is 5 not equal to 10: {result}")
# Output: Is 5 not equal to 10: True

# Inequality Operator (!=) with `False` evaluation
result = b != c
print(f"Is 10 not equal to 10: {result}") 
# Output: Is 10 not equal to 10: False

# Greater than operator (>) with `False` evaluation
result = a > b
print(f"Is 5 greater than 10: {result}")
# Output: Is 5 greater than 10: False

# Greater than operator (>) with `True` evaluation
result = b > a
print(f"Is 10 greater than 5: {result}")
# Output: Is 10 greater than 5: True

# Less than operator (<) with `True` evaluation
result = a < b
print(f"Is 5 less than 10: {result}")
# Output: Is 5 less than 10: True

# Less than operator (<) with `False` evaluation
result = b < a
print(f"Is 10 less than 5: {result}")
# Output: Is 10 less than 5: False

# Greater than or equal to operator (>=) with `False` evaluation
result = a >= b
print(f"Is 5 greater than equal to 10: {result}")
# Output: Is 5 greater than equal to 10: False

# Greater than or equal to operator (>=) with `True` evaluation
result = b >= c
print(f"Is 10 greater than or equal to 10: {result}")
# Output: Is 10 greater than or equal to 10: True

# Less than or equal to operator (<=) with `False` evaluation
result = b <= a
print(f"Is 10 less than or equal to 5: {result}")
# Output: Is 10 less than or equal to 5: False

# Less than or equal to operator (<=) with `True` evaluation
result = b <= c
print(f"Is 10 less than or equal to 10: {result}")
# Output: Is 10 less than or equal to 10: True

#********************** Booleans Using Logical Operators ***********************

# The `not` logical operator negates the boolean value of a comparison. For better readability, the boolean expression is put in parentheses.
result = not (b == c)
print(f"not 5 is equal to 5 evaluates to: {result}")
# Output: not 5 is equal to 5 evaluates to: False

result = not (a == b)
print(f"not 5 is equal to 10 evaluates to: {result}")
# Output: not 5 is equal to 10 evaluates to: True

# The expressions on both sides of the `and` logical operator must evaluate to 
# `True` or the condition is false.
result = a < b and c < d
print(f"Is 5 less than 10 and is 10 less than 15: {result}")
# Output: Is 5 less than 10 and is 10 less than 15: True

result = a < b and c > d
print(f"Is 5 less than 10 and is 10 greater than 15: {result}")
# Output: Is 5 less than 10 and is 10 greater than 15: False

result = False and False
print(f"False and False evaluates to: {result}")
# Output: False and False evaluates to: False

result = True and True
print(f"True and True evaluates to: {result}")
# Output: True and True evaluates to: True

# Either expression on the left or right side of the `or` logical operator must 
# be `True` for the condition to evaluate to `True`
result = a < b or c < d
print(f"Is 5 less than 10 or is 10 less than 15: {result}")
# Output: Is 5 less than 10 or is 10 less than 15: True

result = a < b or c > d
print(f"is 5 less than 10 or is 10 greater than 15: {result}")
# Output: is 5 less than 10 or is 10 greater than 15: True

result = False or False
print(f"False or False evaluates to: {result}")
# Output: False or False evaluates to: False

result = True or False
print(f"True or False evaluates to: {result}")
# Output: True or False evaluates to: True

#*************** Combining the `not`, `and`, and `or` operators ****************

result = (a < b) and (c > a) or (a == 5)
# The expression evaluates to (True and True) or True
print(f"(True and True) or True is: {result}")
# Output: (True and True) or True is: True

result = not (a < b or d < a) or b > d
# The expression evaluates to (not True) or False
print(f"(not True) or False is: {result}")
# Output: (not True) or False is: False

result = (True and False) or (True and not False)
# The expression evaluates to: False or (True and True)
print(f"False or (True and True) is: {result}")
# Output: False or (True and True) is: True

#************** Order of Precedence in Boolean Logical Operators ***************
# The order of precedence in Python's logical operators is not > and > or, so 
# any `not` expressions will be evaluated first, then the `and` expressions, 
# and finally, the `or` expressions. Parenthesis can be used to have greater 
# control over the order as anything inside parenthesis will always evaluate 
# first.

x = True
y = False
z = True

result = x or y and not z
# The expression is evaluated as x or (y and (not z))
# The `not` operator has the highest precedence, so `not z` is evaluated first, 
# resulting in `False`. Then, the `and` operator is evaluated as `y and 
# False`, resulting in `False`. Finally, the `or` operator is applied as `x or 
# False`, resulting in `True`

#************************* `is` and `is not` Keywords **************************
# Immutable type comparisons that have the same values are the same objects in 
# memory.
str1 = "Hello"
str2 = "Hello"
result = str1 is str2
print(f'Is str1 and str2 the same object: {result}')
# Output: Is str1 and str2 the same object: True

a = 5
b = 5
result = a is b
print(f'Is a and b the same object: {result}')
# Output: Is a and b the same object: True

# Mutable type comparisons with the same values are not necessarily the same 
# object in memory.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Although list1 and list2 have the same value, they are not referencing the 
# same object
result = list1 is list2
print(f"Is list1 and list2 the same object: {result}")
# Output: Is list1 and list2 the same object: False

# Since list3 was assigned list1, they are referencing the same object
result = list1 is list3
print(f"Is list1 and list3 the same object: {result}")
# Output: Is list1 and list3 the same object: True

# You can also use `not` in conjunction with `is` to negate the boolean
result = list1 is not list3
print(f"Is list1 and list3 not the same object: {result}")
# Output: Is list1 and list3 not the same object: False

#************************* `in` and `not in` Keywords **************************
# Create a string and list to use the `in` and `not in` operators on
message = "The cat catches mice."
numbers = [1, 2, 3, 7, 8, 9]

# Check if the value "dog" is in the `message` string
result = "dog" in message
print(f"Is 'dog' in '{message}': {result}")
# Output: Is 'dog' in 'The cat catches mice.': False

# Check if the value "cat" is in the `message` string
result = "cat" in message
print(f"Is 'cat' in '{message}': {result}")
# Output: Is 'cat' in 'The cat catches mice.': True

# Check if the value 4 is not in the `numbers` list
result = 4 not in numbers
print(f"Is 4 not in {numbers}: {result}")
# Output: Is 4 not in [1, 2, 3, 7, 8, 9]: True

# Check if 50 is not in the range 1 (inclusive) through 101 (non-inclusive). 
# Since 50 is in that range, using `not in` returns `False`.
result = 50 not in range(1, 101)
print(f"Is 50 not in range(1, 101): {result}")
# Output: Is 50 not in range(1, 101): False

#*************** Truthiness, Falsiness, and The `bool` Function ****************
"""
These values are considered falsy in Python (not an exhaustive list):
    False - The boolean value representing false.
    None - The absence of a value.
    0 - The integer zero.
    0.0 - The float zero.
    '' - The empty string.
    "" - Another form of the empty string.
    [] - An empty list.
    {} - An empty dictionary.
    () - An empty tuple.
    set() - An empty set.
    frozenset() - An empty frozen set.
"""
# Use the `bool` function to determine if something is `True` or `False`
result = bool(0)
print(f"Zero evaluates to: {result}")
# Output: Zero evaluates to: False

empty_string = ""
result = bool(empty_string)
print(f"An empty string evaluates to: {result}")
# Output: An empty string evaluates to: False

non_empty_string = "Hello"
result = bool(non_empty_string)
print(f"A non-empty string evaluates to: {result}")
# Output: A non-empty string evaluates to: True


#************************** Functions `any` and `all` **************************
# Using the truthiness and falsiness concepts, the `any()` and `all()` 
# functions can be used to determine if any object or all objects in an 
# iterable evaluate to `True`.
my_list = [0, 2, 4]
result = any(my_list)
print(f"Does {my_list} contain at least 1 truthy object: {result}")
# Output: Does [0, 2, 4] contain at least 1 truthy object: True

result = all(my_list)
print(f"Does {my_list} contain all truthy objects: {result}")
# Output: Does [0, 2, 4] contain all truthy objects: False

# Create a list containing all falsy objects
empty_objects = [
        [],             # list
        0,              # integer
        0.0,            # float
        '',             # single quote string
        "",             # double quote string
        {},             # dictionary
        (),             # tuple
        set(),          # set
        frozenset(),    # frozenset
        None,           # None
        False           # False
    ]
result = any(empty_objects)
print(f"Does {empty_objects} contain at least 1 truthy object: {result}")
# Output: Does [[], 0, 0.0, '', '', {}, (), set(), frozenset(), None, False] 
# contain at least 1 truthy object: False

# Create a list containing all falsy objects
non_empty_objects = [
        [1],                    # list
        6,                      # integer
        0.000001,               # float
        'a',                    # single quote string
        "hi",                   # double quote string
        {"name": "Joe"},        # dictionary
        (3, 4, 5),              # tuple
        set([1, 2, 3, 3]),      # set
        frozenset((1, 3, 5)),   # frozenset
        True                    # True
    ]
result = all(non_empty_objects)
print(f"Does {non_empty_objects} contain all truthy objects: {result}")
# Output: Does [[1], 6, 1e-06, 'a', 'hi', {'name': 'Joe'}, (3, 4, 5), {1, 2, 
# 3}, frozenset({1, 3, 5}), True] contain all truthy objects: True
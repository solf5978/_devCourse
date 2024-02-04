"""
Author: Jesse Warner
Date: August 1, 2023

lambda functions are small, anonymous functions that can have any number of 
arguments but can only have one expression. They are defined using the lambda 
keyword and are often used for short and simple functions that don't require a 
separate def statement. The syntax for a lambda function is as follows:

    lambda arguments: expression

Lambda functions are a handy tool for writing concise, functional-style code in 
Python. They are particularly useful when you need to define a simple function 
on the fly without creating a separate function using def. However, for more 
complex logic and larger functions, it's generally better to use regular 
functions for better readability and maintainability.
"""

# Create a basic lambda function with `x` as the argument and `x**2` as the 
# expression.
square = lambda x: x**2
print(square(5))  # Output: 25

"""
In this example, we define a lambda function called "square" that takes one
argument "x" and returns the square of "x" by raising it to the second power.
The lambda function is equivalent to the regular function definition:

    def square(x):
        return x**2

We can call the lambda function just like any other function, passing an 
argument (5 in this case) and getting the result (25).
"""

#******************** Using lambda with built-in functions *********************

# Using a lambda function with the `map()` function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

"""
In this example, we use the lambda function with the built-in "map" function.
The "map" function applies the lambda function to each element of the 
"numbers" list and returns a new list with the results. The lambda function 
takes one argument "x" and returns the square of "x". The "map" function 
effectively squares each element in the "numbers" list and stores the results 
in the "squared_numbers" list.
"""

# Using a lambda function with the `filter()` function
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

"""
In this example, we use the lambda function with the built-in "filter" 
function. The "filter" function applies the lambda function to each element 
of the "numbers" list and returns a new list with the elements from `numbers` 
that caused the lambda function to return a True value. The lambda function 
takes one argument "x" and returns the Boolean value of `x % 2 == 0`. The 
"filter" function effectively separates the even numbers from the "numbers" 
list and stores the results in the "even_numbers" list.
"""

# Using a lambda function as the key argument in a list's `sort()` method
students = [('Alice', 25), ('Bob', 20), ('Eve', 22)]
students.sort(key=lambda x: x[1])
print(students)  # Output: [('Bob', 20), ('Eve', 22), ('Alice', 25)]

"""
In this example, we use the lambda function as the sorting key in the "sort" 
method for the list of tuples "students". The lambda function takes one 
argument "x" (each tuple in the list) and  returns the second element of the 
tuple (the age). The "sort" method sorts the "students" list based on the 
age, resulting in a list of students sorted by their ages in ascending order.
"""

#*************** Passing lambda Functions as a Function Argument ***************

# Define a function that takes a lambda function as an optional argument
def apply_operation(x, y, operation=lambda a, b: a + b):
    return operation(x, y)

# Define a lambda function for multiplication
multiply = lambda a, b: a * b

# Call the `apply_operation()` function and leave the operation parameter as 
# the default lambda function.
add = apply_operation(5, 3)
print(add)  # Output: 8

# Call the `apply_operation` function passing in the lambda function `multiply` 
# for the operation parameter.
multi = apply_operation(7, 8, multiply)
print(multi) # Output: 56

"""
In this example, we have a function called `apply_operation` that takes three 
arguments: `x`, `y`, and an optional parameter `operation`. The `operation` 
parameter represents a lambda function that performs some arithmetic operation 
on the arguments `x` and `y` and defaults to adding them together. The return 
statement invokes the lambda function and passes in the values in `x` and `y` 
for its parameters `a` and `b`.
"""

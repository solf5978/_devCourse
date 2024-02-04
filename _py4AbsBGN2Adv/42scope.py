"""
Author: Jesse Warner
Date: August 1, 2023

The scope is the region or context in which a variable or name is defined and 
can be accessed. It determines how other program portions view a variable and 
how long it exists in memory. Understanding how scope works is important to 
accessing variables, avoiding naming conflicts, and knowing the lifetime of a 
variable. Variables created inside loops and conditionals are in the scope of 
the function or class where the loop or conditional is, or they are in global 
scope if the variable is created outside any function or class. Scope 
precedence means that Python looks for names in the order of local > enclosing 
> global > built-in. The innermost scope takes precedence if a name is defined 
in multiple scopes.

    Local Scope (Function Scope):
        - Variables defined within a function have local scope.
        - Local variables are accessible within the function they were defined.
        - After a function completes, the local variables are destroyed.

    Enclosing Scope (Nested Function Scope):
        - Functions that are defined within another function have access to the
          local variables of that function, variables in the enclosing 
          function, and global variables.
        - The enclosing function (outer function) does not have access to the 
          nested function's local variables.

    Global Scope:
        - Global variables are variables that are defined outside of any class 
          or function.
        - Global functions are functions that are defined outside of any class  
          or function.
        - Global variables and functions can be accessed from anywhere in the 
          program, including functions and classes (must use the global 
          defkeyword).
          
    Built-in Scope:
        - Python has built-in functions and types that are available globally.
        - The built-in names make up the built-in scope and can use used 
          anywhere in the program.
"""

# Create a global variable outside of any function or class.
my_global_var = 10

# Define a function that incorrectly changes `my_global_var`
def modify_global_wrong():
    # Create a local variable called `my_global_var` in the modify_global_wrong
    # function. Although this variable has the same name as the global 
    # my_global_var, it does not change the value assigned to it.
    my_global_var = 20

# Define a function that correctly changes `my_global_var`
def modify_global_correct():
    # The `global` keyword indicates that `my_global_var` should reference the 
    # global variable, not a local variable.
    global my_global_var
    my_global_var = 20

# Define a function with a nested function that accesses its variables and 
# global variables
def outer_function():
    # Create a local variable
    my_local_var = 25

    # Print the variable `my_local_var`
    print(f"my_local_var: {my_local_var}") # Output: my_local_var: 25

    # Print the variable `my_global_var`. Python will first check the local 
    # scope for the variable `my_global_var`, and since it will not find the 
    # variable, it will check the global scope.
    print(f"my_global_var: {my_global_var}") # Output: my_global_var: 10

    # Define a nested function that accesses its variables, the outer function's
    # variables, and global variables. The function `inner_function` is only 
    # accessible by the function `outer_function`.
    def inner_function():
        # Create a variable that is only accessible by the function 
        # `inner_function`
        my_inner_var = 50

        # Print the variables that `inner_function` has access to
        print(f"my_inner_var: {my_inner_var}") # Output: my_inner_var: 50
        print(f"my_local_var: {my_local_var}") # Output: my_local_var: 25
        print(f"my_global_var: {my_global_var}") # Output: my_global_var: 10

    # Call the nested function
    inner_function()

# Call the outer_function function.
outer_function()

# Print my_global_var before attempting to modify it.
print(f"my_global_var before modification: {my_global_var}") 
# Output: my_global_var before modification: 10

# Call the function that incorrectly modifies `my_global_var`
modify_global_wrong()
print(f"my_global_var after incorrect modification: {my_global_var}") 
# Output: my_global_var after incorrect modification: 10

# Call the function that correctly modifies `my_global_var`
modify_global_correct()
print(f"my_global_var after correct modification: {my_global_var}") 
# Output: my_global_var after correct modification: 20

#********************* Loop and Conditional Scope Examples *********************
# Create a loop that initializes a variable. Variables created in a loop are in 
# the same scope as the loop.
for num in range(1):
    loop_var = "Created in the for loop!"

# Print the loop_var created in the for loop
print(loop_var) # Output: Created in the for loop!

# Create a conditional that initializes a variable. Variables created in a 
# conditional are in the same scope as the conditional.
if loop_var:
    if_var = "Created in an if conditional!"

# Print the if_var created in the if conditional
print(if_var) # Output: Created in an if conditional!

#************************** Built-in Scope Examples ****************************
# The built-in scope in Python refers to the namespace that contains all the 
# built-in functions, types, and exceptions provided by the Python language 
# itself. These built-in entities are available for use without the need to 
# import any modules.
str(my_global_var)
range(1, 10, 2)
float(5)
int(5.0)
tuple([1, 2, 3])

#************************** Scope Precedence Example ***************************
# Initialize a variable outside of any function or class
car = "Chevy"

# Define an outer function
def outer_car():
    # Initialize a local variable named the same as the global variable `car`
    car = "Ford"

    # Print the value of `car` from the closest scope (local scope)
    print(f"Outer car: {car}") # Output: Outer car: Ford

    # Define an inner function
    def inner_car():
        # Print the value of `car` from the closest scope (enclosing scope)
        print(f"Inner car: {car}") # Output: Inner car: Ford
    
    # Invoke the `inner_car` function
    inner_car()

outer_car()

# Print the value of `car` from the closest scope (global scope)
print(f"Outside any function or class car: {car}") 
# Output: Outside any function or class car: Chevy

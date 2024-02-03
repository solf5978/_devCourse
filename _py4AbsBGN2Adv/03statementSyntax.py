"""
Author: Jesse Warner
Creation Date: August 1, 2023

Syntax refers to the set of rules and conventions that determine the structure
and formation of valid Python code. It defines how statements, expressions, and 
other elements should be written to create executable code.

Key aspects of Python syntax:
    - Indentation: Python uses indentation to define the structure of code
      blocks, such as loops, conditionals, and functions. Typically, it uses
      four spaces (or a tab) for each level of indentation, but it is up to you
      as the programmer to make that decision. Consistent and proper indentation
      is necessary for correct program execution.

    - Statements: A statement is a complete instruction that performs an action.
      Individual statements are typically written on separate lines.

    - Expressions: An expression is a combination of values, variables, and
      operators that produce a result. Expressions can be standalone or part of
      a statement.
      
    - Comments: Comments are used to add notes to code that explain the purpose
      of the code. The Python interpreter ignores them as they are solely for 
      people reading the code. Python uses the hash/pound `#` symbol to 
      indicate the start of a comment and continues until the end of the line.
"""

# This is a comment. Comments last until the end of the line. If you want to go
# to a new line, you must use another hash/pound `#` symbol. You can create 
# multiline comments using multiple hash/pound `#` symbols.

""" You can also make multiple line comments by creating a string with 3 double 
quote `"` or single quote `'` symbols and not assigning it to a variable. The 
Python interpreter will simply ignore it. However, it must use proper indention for the code block that it is in."""

# This is a statement
x = 3

# This is an expression
x + 5

# This is a statement with an expression
y = x + 5

# An if/elif/else conditional showing that indentation is up to the programmer. 
# Indentation must be the same in each individual code block, but can be 
# different from other code blocks. However, it is difficult to read when the 
# indentation is not consistent. 
if x > 5:
    print("x is greater than 5") # 4 space indentation (1 tab)
    # print("hello") # Adding a space before this statement causes an error.
elif x == 5:
            print("x is equal to 5") # 12 space indentation
else:
 print("x is less than 5") # 1 space indentation
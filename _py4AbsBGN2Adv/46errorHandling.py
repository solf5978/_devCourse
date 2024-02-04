"""
Author: Jesse Warner
Date: August 1, 2023

Error handling is when a Python program catches errors that may occur during 
execution and gracefully handles the errors and prevents the program from 
crashing.

Key concepts in error handling:
    - Exception: An exception is an error that occurs during the execution of a 
      program. It can be caused by various factors, such as invalid input, 
      logical errors, or external dependencies.

    - try-except block: The try-except block is used to catch and handle 
      exceptions. The code that might raise an exception is placed inside the 
      try block. If an exception occurs, it is caught and handled in the 
      corresponding except block.

    - except statement: The except statement specifies the type of exception to 
      catch. It allows you to define custom handling logic for different types 
      of exceptions. You can catch specific exceptions or use a generic except 
      block to catch any exception.

    - finally block: The finally block is optional and is used to specify   
      cleanup code that should be executed regardless of whether an exception 
      occurred or not. It is typically used to release resources or perform 
      necessary clean-up operations.

    - Exception types: Python provides a wide range of built-in exception types 
      that cover various error scenarios. Some common exception types include 
      TypeError, ValueError, FileNotFoundError, and ZeroDivisionError. You can 
      also create custom exception classes by deriving them from the base 
      Exception class.
"""

# Basic try/except block where `except` can catch any exceptions that may 
# occur, but is not able to provide any details about any exceptions it catches.
try:
    x = 10 / 0 # Division by zero
except:
    print('Oh no! Something went wrong!')
# Output: Oh no! Something went wrong!

# Try/except block that catches the ZeroDivsionError exception
try:
    x = 10 / 0 # ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero!")
# Output: You cannot divide by zero!

# Try/except block that catches the ZeroDivisionError exception and any other 
# exceptions that may occur but is unable to provide any details about other 
# exceptions.
try:
    x = 10 / 2
    print(y) # NameError: 'y' is not defined
except ZeroDivisionError:
    print("You cannot divide by zero!")
except:
    print('Oh no! Something went wrong!')
# Output: Oh no! Something went wrong!

# Try/except block that catches the ZeroDivsionError exception and and other 
# exceptions and can give details about the other exceptions.
try:
    x = 10 / 2
    print(y) # NameError: 'y' is not defined
except ZeroDivisionError:
    print("You cannot divide by zero!")
except Exception as e:
    print("Error:", e)
# Output: Error: name 'y' is not defined

# Try/except block that catches multiple specified exceptions. The first error 
# encountered is the error that throws the exception.
try:
    x = 10 / 2
    my_list = [x, 0, 'hi', y] # NameError: 'y' is not defined
    print(f"Fourth index is: {my_list[4]}")  # IndexError: 4 is out of range
except ZeroDivisionError:
    print("You cannot divide by zero!")
except IndexError:
    print("Index is out of range!")
except Exception as e:
    print("Error:", e)
# Output: Error: name 'y' is not defined

# Another try/except block that catches multiple specified exceptions. The 
# first error encountered is the error that throws the exception.
try:
    my_list = [x, 0, 'hi', []]
    print(f"Fourth index is: {my_list[4]}") # IndexError: 4 is out of range
    x = 10 / 0 # ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero!")
except IndexError:
    print("Index is out of range!")
except Exception as e:
    print(f"Error: {str(e)}")
# Output: Index is out of range!


# Another try/except block that catches multiple specified exceptions, but they 
# all produce the same message
try:
    my_list = [x, 0, 'hi', y] # NameError: 'y' is not defined
    print(f"Fourth index is: {my_list[4]}") # IndexError: 4 is out of range
    x = 10 / 0 # ZeroDivisionError
except (ZeroDivisionError, IndexError, NameError):
    print("Division by zero, index error, or name error occurred!")
# Output: Division by zero, index error, or name error occurred!


# A try/except/finally block. `finally` runs whether or not an exception 
# occured.
try:
    x = 10 / 0 # ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print('Try/except block is complete!')
# Output: 
# You cannot divide by zero!
# Try/except block is complete!

# Create a custom error class that extends the `Exception` class
class InvalidEmailError(Exception):
    def __init__(self, message):
        super().__init__(f"Invalid email address: {message}")
        self.message = message

# Check if `@` or `.` are not in the email string. Raise the InvalidEmailError 
# exception if either symbol is missing.
def validate_email(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailError(email)

# Try to validate an email address (valid email) 
try:
    # Email correctly contains the '.' and '@' characters.
    email = "leet.coder@xyz.com"
    validate_email(email)
    print("Email address is valid:", email)
except InvalidEmailError as e:
    print("Error:", e)
# Output: Email address is valid: leet.coder@xyz.com

# Try to validate an email address (invalid email) 
try:
    # Email is missing the '.' character.
    email = "leetcoder@xyzcom"
    validate_email(email)
    print("Email address is valid:", email)
except InvalidEmailError as e:
    print("Error:", e)
# Output: Error: Invalid email address: leetcoder@xyzcom




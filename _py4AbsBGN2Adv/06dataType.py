"""
Author: Jesse Warner
Creation Date: August 1, 2023

Data types define the kinds of data that can be stored and manipulated in
variables. Each data type has unique properties, behaviors, and operations
associated with it. Python has numerous built-in data types and allows users to 
define their own data types by creating classes.

Python data types:
    Numeric Types:
        - int: Represents integers values (1, 1000, -25).
        - float: Represents floating-point numbers (1.0, 3.14, -200.867).
        - complex: Represents complex numbers. Must use the form 'real + imagj'
          where 'real' and 'imag' are numeric values (5 + 10j, 4 - 2j).
    Sequence Types:
        - str: Represents a sequence of characters ("Hello", 'World') and are 
          enclosed in single or double quotes.
        - list: Represents an ordered collection of items [1, 2, 3] and is 
          enclosed in square brackets.
        - tuple: Represents an ordered collection of items (1, 2, 3). Tuples 
          are immutable and enclosed in parentheses.
        - range: Represents an immutable sequence of numbers (range(1, 10, 1)). 
          Ranges generate numbers as needed to reduce memory usage.
    Bytes Types:
        - bytes: Represents a sequence of bytes, often used for handling binary 
          data.
        - bytearray: Represents a mutable version of the 'bytes' type.
        - memoryview: Represents a memory view of an object allowing access to 
          its internal data.
    Mapping Type:
        - dict: Represents a collection of key-value pairs, where each key is 
          unique. Dictionaries are enclosed in curly braces {key: value}.
    Set Types:
        - set: Represents an unordered collection of unique elements. Sets are 
        mutable, but the elements are unchangeable. Like dictionaries, sets are 
        enclosed in curly braces, but contain individual elements {1, 2, 3}.
        - frozenset: Represents an immutable version of a set.
    Boolean Type:
        - bool: Represents a boolean value of 'True' or 'False'.
    None Type:
        - None: Represents the absence of a value or a null value.
"""

# Numeric type examples (int, float, and complex)
num_int = 10
num_float = 3.14
num_complex = 2 + 3j

# Sequence type examples (list, tuple, str, and range)
my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
my_str = "Hello, World!"
my_range = range(5)

# Byte type examples (bytes, bytearray, and memoryview)
my_bytes = b'\x48\x65\x6C\x6C\x6F' # Hexadecimal representation of "Hello"
print(my_bytes.decode()) # Output: Hello

my_bytearray = bytearray(b'Hello')
print(my_bytearray.decode()) # Output: Hello

my_memoryview = memoryview(my_bytearray)
print(my_memoryview) # Output: The memory location where my_bytearray is stored.

# Mapping type (dictionary) with key-value pairs. The key "name" is assigned 
# the string value "Alice" and the key "age" is assigned the integer value 25.
my_dict = {"name": "Alice", "age": 25}

# Set types set and frozenset
my_set = {1, 2, 3, 4}
my_frozenset = frozenset({1, 2, 3, 4})

# Boolean type (True and False)
is_true = True
is_false = False

# None type (None)
my_var = None
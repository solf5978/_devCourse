"""
Author: Jesse Warner
Date: August 1, 2023

The `with` statement and `as` keyword are used together to work with context 
managers. Context managers are objects that define the methods `__enter__()` 
and `__exit__()`, and they allow you to allocate and release resources when 
entering and exiting a block of code. The `with` statement provides a clean and 
concise way to work with context managers and ensures that the resources are 
properly managed, even if an exception occurs.

Syntax of the `with` statement with the `as` keyword:

    with context_manager_expression as variable:
        Code block that uses the context_manager

When the `with` statement is executed, the `__enter__()` method of the context 
manager is called, and any value returned by it is assigned to the variable 
specified after the `as` keyword. Then, the code block inside the `with` 
statement is executed, allowing you to work with the managed resources. After 
the code block is executed or if an exception occurs, the `__exit__()` method 
of the context manager is called, allowing you to release the allocated 
resources or perform necessary cleanup tasks.

The `with` statement is a useful tool for handling resources in a clean and 
efficient way and is commonly used when working with files, database 
connections, network connections, and other resources that need to be properly 
managed.

The `open()` function is used as a context manager with the `with` statement. 
The file is opened for reading, and the contents are read and stored in the 
data variable. Once the code block inside the with statement is executed, the 
file is automatically closed, regardless of whether an exception occurred or 
not.
"""

"""
Attempt to open a file in `read` mode by passing in an `r` for mode. When you 
open a file in read mode, the file is opened for reading. If the file does 
not exist, it will raise a FileNotFoundError. You can read the content of the 
file using methods like read(), readline(), or readlines(). The file pointer 
is at the beginning of the file, and you can only read from the file; you 
cannot write to it. If you try to write to a file opened in read mode, it 
will raise an UnsupportedOperation error.
"""
try:
    with open('non_existent_file.txt', 'r') as file:
        contents = file.read() # Does nothing as the file does not exist.
except FileNotFoundError:
    print("File not found!")

"""
Open a file in `write` mode by passing in a `w` for mode. When a file is 
opened in write mode, it truncates the file's content if the file already 
exists. If the file does not exist, a new file is created. Any data written 
to the file will overwrite the previous content, so use this mode with 
caution when you want to create a new file or completely rewrite an existing 
file.
"""
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

"""
Attmept to create a file that does not exist in `exclusive creation` mode by 
passing in a `x` for mode. If the file does exists, it raises a 
`FileExistsError` exception. The `x` mode allows you to write to the file and 
is useful when you want to create a new file safely without overwriting an 
existing file. 
NOTE: In this example the file already exists. If it did not exist, it would 
be created and "Hello World!" would be written to it.
"""
try:
    with open('example.txt', 'x') as file:
        file.write("Hello World!") # Does nothing as the file exists already.
except FileExistsError:
    print("File already exists!")
    # Output: File already exists!

"""
Open a file in `append` mode by passing in an `a` for mode. When a file is 
opened in append mode, it does not truncate the file's content. Instead, it 
starts writing data at the end of the file, preserving the existing content. 
If the file does not exist, a new file is created.
"""
with open('example.txt', 'a') as file:
    file.write('\nAppending additional content.')
    file.write('\nAppending even more content.')

#************************** Using the read() method ****************************

# Open a file and print the contents to the console with the read() method.
with open("example.txt", 'r') as file:
    print(f"Read entire file: {file.read()}")
    # Output:
    # Read entire file: Hello, World!
    # Appending additional content.
    # Appending even more content.

# Open a file and print the contents to the console with the read() method 
# using a size argument to only print a specific number of characters.
with open("example.txt", 'r') as file:
    print(f"Read partial file: {file.read(5)}") # Hello
    # Output: Read partial file: Hello

"""
Open a file and print the contents to the console with the read() method 
using a size argument to only print a specific number of characters multiple 
times. The `read` method starts where the handle currently is in the file, so 
multiple calls in the same `with` statement move through the files contents. 

NOTE: The third set of 5 characters contains a newline character because the 
end of the first line was reached and ends with a '\n' character, which is why the 'A' is below the 'ld!' in 
the output.
"""
with open("example.txt", 'r') as file:
    print(f"First 5 characters: {file.read(5)}")    # Hello
    print(f"Second 5 characters: {file.read(5)}")   # , Wor
    print(f"Third 5 characters: {file.read(5)}")    # ld!\nA
    # Output:
    # First 5 characters: Hello
    # Second 5 characters: , Wor
    # Third 5 characters: ld!
    # A

#************************* Using the readline() method *************************

# Open a file and print the contents to the console with the readline() method.
with open("example.txt", 'r') as file:
    print(f"Read entire line: {file.readline()}")
    # Output: Read entire line: Hello, World!

# Open a file and print the contents to the console with the readline() method 
# using a size argument to only print a specific number of characters in that 
# line.
with open("example.txt", 'r') as file:
    print(f"Read partial line: {file.read(5)}")
    # Output: Read partial line: Hello

"""
Open a file and print the contents to the console with the readline() method 
using a size argument to only print a specific number of characters multiple 
times. The `readline` method starts where the handle currently is in the 
file, so multiple calls in the same `with` statement move through the files 
contents. However, unlike with the `read` method, `readline` does not include 
the newline character when returning text from files and does not jump to 
another line when it is encountered.
"""
with open("example.txt", 'r') as file:
    print(f"First 5 characters: {file.readline(5)}")    # Hello
    print(f"Second 5 characters: {file.readline(5)}")   # , Wor
    print(f"Third 5 characters: {file.readline(5)}")    # ld!
    # Output:
    # First 5 characters: Hello
    # Second 5 characters: , Wor
    # Third 5 characters: ld!

#************************ Using the readlines() method *************************

# Open a file and print a list containing each line of the contents to the 
# console with the `readlines()` method. 
with open("example.txt", 'r') as file:
    print(f"Read entire file list: {file.readlines()}")
    # Output: 
    # Read entire file list: ['Hello, World!\n', 'Appending additional content.
    # \n', 'Appending even more content.']

"""
The `readlines()` method takes a `__hint` for the argument. Any lines 
encountered up to and including the character at the number passed in, not 
including newline characters, are returned in the list. Using a character that 
is in the first line of the file
"""
with open("example.txt", 'r') as file:
    print(f"Character in first line list: {file.readlines(5)}")
    # Output: Character in first line list: ['Hello, World!\n']

# Using a character in the second line of the file
with open("example.txt", 'r') as file:
    print(f"Character in second line list: {file.readlines(25)}")
    # Output: Character in second line list: ['Hello, World!\n', 'Appending 
    # additional content.\n']

# Using a character in the third line of the file
with open("example.txt", 'r') as file:
    print(f"Character in third line list: {file.readlines(50)}")
    # Output: Character in third line list: ['Hello, World!\n', 'Appending 
    # additional content.\n', 'Appending even more content.']

"""
Like with the `read()` and `readline()` methods, `readlines()` starts where 
the handle is in the file, so calling it multiple times in the same `with` 
statement moves through the file. Each `readlines()` call, returns the entire 
line and moves the handle to the next line.
"""
with open("example.txt", 'r') as file:
    print(f"First call list: {file.readlines(1)}")
    print(f"Second call list: {file.readlines(1)}")
    print(f"Third call list: {file.readlines(1)}")
    # Output:
    # First call list: ['Hello, World!\n']
    # Second call list: ['Appending additional content.\n']
    # Third call list: ['Appending even more content.']

#****************************** Using a for loop *******************************

"""
Open a file and print the contents to the console using a for loop. Add 
`end=''` into the print functions parameters to prevent extra spacing between 
lines in the console. The file ends each line with a newline character and 
the print function dedaults to ending with a newline character causing space 
between each printed row.
"""
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
        # Output:
        # Hello, World!
        # Appending additional content.
        # Appending even more content.

#*************************** Using the seek() method ***************************

# You can also use the `seek()` method to place the handle at a specific 
# location within the file.
with open('example.txt', 'r') as file:
    file.seek(7) # Move the handle to before 7th character (W) in the file
    print(f"7th character read: {file.read(5)}") # read 5 characters
    # Output: 7th character read: World

"""
NOTE: There are dozens of `modes` you can open files with. The `r`, `w`, and 
`a` modes can all have a `+` suffix to allow you to read and write to the 
files. If you use `r+`, the handle is positioned at the beginning of 
the file, and the data already in the file will be overwritten. If you use 
`w+', the data in the file will be truncated and new data will be written. If 
you use `a+`, the handle will be positioned at the end of the file and new 
data will be appended to the old data.
"""

"""
Author: Jesse Warner
Creation Date: August 1, 2023

Strings are a built-in data type used to represent text or a sequence 
of characters. They are enclosed within either single quotes `'` or double 
quotes `"`, and multi-line strings are created by using three single or double 
quotes consecutively. The `str()` function can be used to explicitly convert 
other data types into strings.

Key features of strings in Python:
    - Immutable: Strings are immutable, which means that their values cannot be
      changed after they are created. If you modify a string, you create an 
      entirely new string with the changes.

    - Indexing: The characters within a string can be accessed by using square 
      bracket syntax and a character's index starting at 0.

    - Slicing: A subset of a string can be retrieved by using slicing syntax.
      
    - Concatenation: Strings can be concatenated using the `+` operator, which
      allows you to combine multiple strings into a single string.
      
    - Escape Characters: Certain characters are not allowed to be put into
      strings. To put these characters into a string, you must use the escape
      character `\` followed by the character you want to insert.

Strings in Python are versatile and widely used for working with text-based 
data, input/output operations, manipulation of textual information, and more.
They provide a rich set of operations and methods to manipulate, analyze, and 
format text in various ways.
"""
#******************************* String Basics *********************************
# Create two strings that can be concatenated. One uses double quotes, and the 
# other uses single quotes. It does not matter as long as whichever type of 
# quotes you open the string with is what you close it with.
greeting = "Hello, "
name = 'World!'

# Concatenate two strings using the addition (+) operator
my_string = greeting + name
print(my_string) # Output: Hello, World!

# Repeat a string using the multiplication (*) operator
print(name * 5)
# Output: World!World!World!World!World!

# Get the length of a string using the `len()` function
str_length = len(my_string) 
print(f"'{my_string}' has {str_length} characters in it.") 
# Output: 'Hello, World!' has 13 characters in it.

# Print the first character in a string using square brackets and the index 0
print(f"The first character of '{my_string}' is {my_string[0]}") 
# Output: The first character of 'Hello, World!' is H

multi_line_string = """This is a multi-line
string. They are printed in the
terminal as they are written in
the program."""
print(multi_line_string)
# Output: 
# This is a multi-line
# string. They are printed in the
# terminal as they are written in
# the program.

# Create a string using the `str()` function and passing in a Boolean value
converted_string = str(False)
print(converted_string) # Output: False

#************************* Examples of Slicing Strings *************************

# Slice a string using an end (non-inclusive) index and no start index
print(my_string[:5]) # Output: Hello

# Slice a string using a start (inclusive) and end (non-inclusive) index
print(my_string[7:10]) # Output: Wor

# Slice a string using a start (inclusive) index and no end index
print(my_string[7:]) # Output: World!

# Slice a string using negative indexing
print(my_string[-6:-1]) # Output: World

# Slice a string using a start (inclusive), end (non-inclusive), and step
print(my_string[1:10:2]) # Output: el,Wr


#******************** Examples of Built-In String Methods **********************

print(my_string.upper()) # Output: HELLO, WORLD! (all uppercase letters)

print(my_string.lower()) # Output: hello, world! (all lowercase letters)

# Create a string with leading and trailing spaces to perform string methods on
space_string = "    Too many spaces!     "

# Strip the extra spaces before and after the text. If no argument is passed 
# into the `strip` method, space is used by default)
space_string = space_string.strip()
print(space_string) 
# Output: Too many spaces! (leading and trailing spaces are removed)

# A string with leading and trailing dashes to perform string methods on
dash_string = "-----Too many dashes-----"
# Strip the dashes on the left side of the text
print(dash_string.lstrip('-')) # Output: Too many dashes-----!

# Strip the dashes on the right side of the text
print(dash_string.rstrip('-')) # Output: -----Too many dashes!

# A string with leading and trailing symbols to perform string methods on
symbol_string = "*-,-,*-,-^,-Too many symbols-,-,-,-,-#"

# Strip the symbols on the left and right sides of the text. The `strip` 
# function checks each character on either side of the string, and if the 
# character is in the characters we passed into the function, it is removed 
# from the string. This action repeats until a character not in the function 
# argument is encountered.
print(symbol_string.strip('-,*#')) # Output: ^,-Too many symbols

# A quote by Mahatma Gandhi to perform string operations on
quote = "Learn as if you will live forever, live like you will die tomorrow."

# Check if a string ends with a sequence of characters
print(quote.endswith("tomorrow.")) # Output: True

# Check if a string starts with a sequence of characters
print(quote.startswith("Learn")) # Output: True

# Convert the string to a list of substrings using `split` with a space 
# (default separator string) as the separator
print(quote.split()) 
# Output: ['Learn', 'as', 'if', 'you', 'will', 'live', 'forever,', 'live',
#          'like', 'you', 'will', 'die', 'tomorrow.']

# Convert the string to a list of substrings using `split` with 'you' as the 
# separator. Notice that the word 'you' is not included in the substrings.
print(quote.split('you'))
# Output: 
# ['Learn as if ', ' will live forever, live like ', ' will die tomorrow.']

# Use the replace method to change all spaces to dashes
print(quote.replace(' ', '-'))
# Output: Learn-as-if-you-will-live-forever,-live-like-you-will-die-tomorrow.

# Method chaining a string (Strip the dashes, make it uppercase, and split it)
chained_string = dash_string.strip('-').upper().split()
print(f"Chained method string: {chained_string}")
# Output: Chained method string: ['TOO', 'MANY', 'DASHES']

# Join a string together using an iterable
print(f"Joined string: {' '.join(chained_string)}")
# Output: Joined string: TOO MANY DASHES

print(f"Joined string dash separated: {'-'.join(chained_string)}")
# Output: Joined string dash separated: TOO-MANY-DASHES

#*********************** Examples of formatting strings ************************
name = "John"
age = 35
job = "Spy"

# Format a string with empty placeholders
person_string = "My name is {}. I am {} years old and a {}!"
print(person_string.format(name, age, job))
# Output: My name is John. I am 35 years old and a Spy!

# Format a string with indexed placeholders
person_string = "My name is {1}. I am {0} years old and a {2}!"
print(person_string.format(age, name, job))
# Output: My name is John. I am 35 years old and a Spy!

# Format a string with indexed placeholders and reusing indexes
person_string = "His name is {1}. {1} is {0} years old and a {2}!"
print(person_string.format(age, name, job))
# Output: His name is John. John is 35 years old and a Spy!

# Format a string with key-value pairs
person_string = "His name is {_name}. {_name} is {_age} years old and a {_job}!"
print(person_string.format(_age=40, _name="Tim", _job="Cowboy"))
# Output: His name is Tim. Tim is 40 years old and a Cowboy!

# Format a string using f-string formatting by placing a 'f' before the string
# and using the variables directly in the {} placeholders.
print(f"My name is {name}. I am {age} years old and a {job}!")
# Output: My name is John. I am 35 years old and a Spy!

# Format a string by restricting the number of decimal places to 2
pi = 3.141592653589793238
print(f"The value of pi is approximately {pi:.2f}.")  
# Output: The value of pi is approximately 3.14.

#***************************** Escape Characters *******************************
"""
Examples of escape characters (must be preceded with a backslash character `\`):
    `\` - Backslash: Represents a literal backslash character.
    `'` - Single Quote: Represents a literal single quote character.
    `"` - Double Quote: Represents a literal double quote character.
    `n` - Newline: Represents a line break or newline character.
    `t` - Tab: Represents a horizontal tab character.
    `r` - Carriage Return: Represents a carriage return character.
    `b` - Backspace: Represents a backspace character.
    `f` - Form Feed: Represents a form feed character.
    `ooo` - Octal Value: Represents a character based on its octal value
    `xhh` - Hexadecimal Value: Represents a character based on its hexadecimal
            value (e.g., x0A represents a newline character).
    `uhhhh` - Unicode Character: Represents a Unicode character based on its 
              4-digit hexadecimal value.
    `Uhhhhhhhh` - Unicode Character: Represents a Unicode character based on
                  its 8-digit hexadecimal value.
    `N{name}` - Unicode Character by Name: Represents a Unicode character based 
                on its name.
"""
print("The file path is C:\\Users\\Path") 
# Output: The file path is C:\Users\Path

print("The letter \'A\' please")
# Output: The letter 'A' please

print("He said, \"Yes I will!\"!")
# Output: He said, "Yes I will!"!

# You can also use single or double quotes without the escape characters if 
# they are different from type that are enclosing the string.

# Double quoted string with single quotes in it
print("The letter 'B' please")
# Output: The letter 'B' please

# Single quoted string with double quotes in it
print('She said, "Hello!"')
# Output: She said, "Hello!"

# Using the \n escape character to create new lines
print("This is a\nMulti-line\nstring!")
# Output:
# This is a
# Multi-line 
# string!

# Using the \t escape character to put a tab in the string
print("This line has a tab\tin it!")
# Output: This line has a tab     in it!

# Using the 4-digit hex value escape character to create a smiley face
print("Unicode character by hex value: \u263A")
# Output: Unicode character by hex value: ☺

# Using the Unicode character by name escape character to create a snowman
print("Unicode character by name: \N{SNOWMAN}")  
# Output: Unicode character by name: ☃

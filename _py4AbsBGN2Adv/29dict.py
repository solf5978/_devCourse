"""
Author: Jesse Warner
Creation Date: August 1, 2023

A dictionary is a mutable and unordered collection of key-value pairs. It is a 
versatile data structure that allows you to store and retrieve data based on 
unique keys. Dictionaries are enclosed in curly braces {} and consist of 
comma-separated key-value pairs.

Key Features of Dictionaries:
    - Key-Value Relationship: Each key is associated with a value, forming a
      mapping relationship.

    - Mutable: Dictionaries can be modified by adding, modifying, or removing
      key-value pairs.

    - Dynamic: Dictionaries can grow or shrink as needed to accommodate new
      key-value pairs.

    - Efficient Data Retrieval: Dictionaries provide fast access to values
      based on their unique keys.

    - Flexible Keys and Values: Keys can be of various data types as long as 
      they are immutable, such as numbers, strings, and tuples. Values can be 
      of any type.

    - Key Uniqueness: Each key in a dictionary must be unique. If a duplicate
      key is added, it will overwrite the existing value.

Common Operations and Methods:
    - Accessing Values: Use the `get()` method or square bracket [] notation to
      retrieve a value based on its key.

    - Adding and Modifying Values: Use the `update()` method or square bracket 
      [] notation to add new key-value pairs or modify existing ones.

    - Removing Key-Value Pairs: Use the `del` statement, `popitem()` method, or 
      `pop()` method to remove key-value pairs from the dictionary.

    - Checking Key Existence: Use the `in` operator to check if a key exists in
      the dictionary.

    - Length: Use the `len()` function to get the number of key-value pairs in
      the dictionary.

    - Iteration: Use a `for` loop with the `keys()`, `values()`, or `items()` 
      methods to iterate over the keys, values, or both in the dictionary.

    - Clearing: Use the `clear()` method to remove all key-value pairs from the
      dictionary.

    - Copying: Use the `copy()` method or the `dict()` function to create a
      copy of the dictionary.

    - Merging: Use the `update()` method to combine two dictionaries into a
      single dictionary.
      
    - Dictionary Comprehension: Use a concise syntax to create new dictionaries
      based on existing dictionaries using comprehension techniques.

Dictionaries are commonly used when you need to organize and access data based 
on unique identifiers or keys. They are suitable for scenarios where fast data
retrieval and flexible data storage are required.
"""

# Create a dictionary using curly braces: {key: value}
my_dict = {1: 'one', 2: 'two', 3: 'three'}
print(my_dict) # Output: {1: 'one', 2: 'two', 3: 'three'}

# Create a dictionary using the `dict()` function with key-value pairs: 
# dict(key=value). 
# NOTE: The key must be a valid Python variable name when using key-value pairs.
my_dict = dict(one='one', two='two', three='three')
print(my_dict) # Output: {'one': 'one', 'two': 'two', 'three': 'three'}

# Create a dictionary using the `dict()` function with an iterable: 
# dict(iterable). A list of tuples is used here.
# NOTE: The iterable must contain collections of length two, and the first 
# element must be an immutable type.
my_dict = dict([(4, 'four'), (5, 'five'), (6, 'Hello!')])
print(my_dict) # Output: {4: 'four', 5: 'five', 6: 'Hello!'}

# Create a dictionary to store information about a person
person = {
    "first_name": "John",
    "last_name": "Smith",
    "phone": "555-555-1234",
    "email": "john_smith@xyz.com",
    "age": 30
}

# Accessing dictionary values by using their keys with square bracket syntax.
print(f"First name: {person['first_name']}") # Output: First name: John
print(f"Last name: {person['last_name']}") # Output: Last name: Smith
print(f"Phone number: {person['phone']}") # Output: Phone number: 555-555-1234
print(f"Email: {person['email']}") # Output: Email: john_smith@xyz.com
print(f"Age: {person['age']}") # Output: Age: 30

# Update a value associated with a key using square bracket syntax.
person["age"] = 31
print(f"Age: {person['age']}") # Output: Age: 31

# Add a new key-value pair with the key "job" using square bracket syntax.
person["job"] = "Explorer"
print(f"person dictionary after adding the `job` key: {person}")
# Output: 
# person dictionary after adding the `job` key: 
# {'first_name': 'John', 'last_name': 'Smith', 'phone': '555-555-1234', 
# 'email': 'john_smith@xyz.com', 'age': 31, 'job': 'Explorer'}

# Delete a key-value pair with key 'age' using the `del` keyword.
del person['age']
print(f"person dictionary after deleting the 'age' key: {person}")
# Output: 
# person dictionary after deleting the `age` key: 
# {'first_name': 'John', 'last_name': 'Smith', 'phone': '555-555-1234', 
# 'email': 'john_smith@xyz.com', 'job': 'Explorer'}


# Use the `pop()` method to get a value and remove the item from the dictionary 
# (key is present)
email = person.pop("email", "email not found")
print(f"Using pop with key `email` when it's present gives: {email}")
# Output: 
# Using pop with key `email` when it's present gives: john_smith@xyz.com

# Using the `pop()` method with the key 'email' again returns the default value 
# or raises a KeyError if a default value is not provided. This is because the 
# key 'email' is no longer in the dictionary.
email = person.pop("email", "email not found")
print(f"Using pop with key `email` when it's not present gives: {email}")
# Output: 
# Using pop with key `email` when it's not present gives: email not found

# NOTE: "email not found" is what was chosen to be the default value in the 
# `pop()` method. If that value is not added as an argument, a KeyError is
# raised.

# Use the `popitem()` method to get the last dictionary item added.
lifo_item = person.popitem()
print(f"The last item in the person dictionary was: {lifo_item}")
# Output: The last item in the person dictionary was: ('job', 'Explorer')

# Iterate over keys using the `keys()` method with a for loop
for key in person.keys():
    print(key)
    # Output:
    # first_name
    # last_name
    # phone

# Iterate over values using the `values()` method with a for loop
for value in person.values():
    print(value)
    # Output:
    # John
    # Smith
    # 555-555-1234

# Iterate over key-value pairs using the `items()` method with a for loop
for key, value in person.items():
    print(key, value)
    # Output
    # first_name John
    # last_name Smith
    # phone 555-555-1234

# Check if a key exists using the `in` operator
if "phone" in person:
    print("Phone is in the dictionary")

# Use the `get()` method to safely retrieve a value (key is present)
phone = person.get("phone", "Unknown")
print(f"Phone number: {phone}") # Output: Phone number: 555-555-1234

# Use the `get()` method to safely retrieve a value (key is not present)
job = person.get("job", "Job not found")
print(f"Job: {job}") # Output: Job: Job not found

# NOTE: "Job not found" is what was chosen to be the default value in the 
# `get()` method. If that value is not added as an argument, `None` is returned.

# Use the `setdefault()` method to retrieve a value (key is not present)
city = person.setdefault("city", "Las Vegas")
print(f"City: {city}") # Output: City: Las Vegas
# The key 'city' did not exist, so it was created with the value `Las Vegas`

# Use the setdefault() method to retrieve a value (key is present)
city = person.setdefault("city", "Paris")
print(f"City: {city}") # Output: City: Las Vegas
# The key already exists, so the value returned is the value of person["city"]

# Create a new dictionary containing information to add to the person dictionary
new_info = {
    "state": "Nevada",
    "age": 31
}

print(f"Person before update: {person}")
# Output: 
# Person before update: {'first_name': 'John', 'last_name': 'Smith', 
# 'phone': '555-555-1234', 'city': 'Las Vegas'}

# Update the person dictionary with the `new_info` dictionary using the 
# `update()` method
person.update(new_info)
print(f"Person after update: {person}")
# Output:
# Person after update: {'first_name': 'John', 'last_name': 'Smith', 'phone': 
# '555-555-1234', 'city': 'Las Vegas', 'state': 'Nevada', 'age': 31}

# Use the `clear()` method to remove all contents of the dictionary
person.clear()
print(f"person after using clear(): {person}")
# Output: person after using clear(): {}

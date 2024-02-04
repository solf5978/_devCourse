"""
Author: Jesse Warner
Date: August 1, 2023

A function is a named block of reusable code that performs a specific task. If 
the function is inside a class, it is called a method. Functions allow you to 
organize your code into logical units, making it easier to read, understand, 
and maintain. Functions in Python can take input values called parameters, and 
they can return output values. Functions are created by using the `def` keyword 
and giving the function a name, and optionally, parameters and a return type.

Key concepts of functions:
    - Signature: A function's signature is the declaration or definition of the 
      function, which includes its name, parameters, and return type (optional).
      It describes the information necessary to call the function correctly.

    - Parameters: Parameters are variables declared in the function's signature 
      that serve as placeholders for the values passed into the function when 
      it is called. 

    - Arguments: Arguments are the values that are passed into a function when 
      it is called. They match the parameters defined in the function signature 
      and provide the values necessary for the function to perform its 
      operations.

    - Body: The function's body contains the actual code that executes when 
      the function is called. It is a block of indented code that defines the 
      operations to be performed.
      
    - Return Value: Functions can optionally return a value using the `return` 
      statement. The return value is the result or output produced by the 
      function's operations and can be any valid Python object. If no explicit 
      value is returned, the function returns `None`.

Functions provide a way to encapsulate reusable code, accept inputs, and 
produce outputs. They promote code modularity, readability, and reusability. 
Understanding the concepts of function signature, parameters, arguments, and 
return values is essential for effective use of functions in Python.
"""

#************************* Function with no parameters *************************

# Define a function named `print_greeting` using the `def` keyword with no 
# parameters or return type
def print_greeting():
    print("Hello! Welcome to Python functions!")

# Call the `print_greeting` function by typing its name followed by parentheses
print_greeting() # Output: Hello! Welcome to Python functions!

#************************** Function with parameters ***************************

# Define a function named `add_numbers`, and give it the parameters `a` and `b`
def add_numbers(a, b):
    # Get the sum of `a` and `b` and place the value in a variable named `sum`
    sum = a + b 
    # Call the `print` function and pass it the variable `sum` as an argument
    print(sum) 

# Call the `add_numbers` function using 3 and 4 as the argument values for `a` 
# and `b`.
add_numbers(3, 4) # Output: 7

#********************** Function with the `pass` keyword ***********************

# Define a function named `do_nothing` and put the pass keyword in the body
def do_nothing():
    # The `pass` keyword allows the programmer to not put code in a code block
    # without causing errors.
    pass

# Call the `do_nothing` function inside of a `print` function call
print(do_nothing()) # Output: None

#************************ Function with a return value *************************

# Multiply two numbers and return the resulting product
def multiply_numbers(a, b):
    product = a * b
    # The return keyword passes a value back to the caller immediately when it 
    # is encountered. Any statements after a `return` keyword is executed are 
    # not executed.
    return product

result = multiply_numbers(4, 7)
print(f"Product: {result}") # Output: Product: 28

#********************** Function with optional parameters **********************

# Define a function with an optional parameter for `greeting`. If no argument 
# is passed in for `greeting`, "Hello" will be used by default.
def greet(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    print(message)

# Call the `greet` function with the value "Howdy" for the optional parameter.
greet("Bob", "Howdy") # Output: Howdy, Bob!

# Call the `greet` function with no value for the optional parameter.
greet("Tina") # Output: Hello, Tina!

#******************* Function called with keyword arguments ********************

# Print the volume of a cube by multiplying the length, width, and height 
# arguments and storing the value in `volume`.
def calculate_cube_volume(length, width, height=1):
    volume = length * width * height
    print(f"Volume: {volume}")

# Call the `calculate_cube_volume` function using keyword arguments
calculate_cube_volume(length=5, width=5, height=2) # Output: Volume: 50

# Call the `calculate_cube_volume` function using keyword arguments out of order
calculate_cube_volume(width=5, height=2, length=5) # Output: Volume: 50

#****************** Function with multiple return statements *******************

# Return a letter grade based on the value of `score`. When a return statement 
# is encountered anywhere in a function, the function immediately stops 
# executing and returns the specified value back to the caller.
def get_letter_grade(score):
    # If `score` is greater than or equal to 90, return 'A'
    if score >= 90:
        return 'A'
    # If `score` is greater than or equal to 80, return 'B'
    elif score >= 80:
        return 'B'
    # For all `score` values under 80, return 'C'
    else:
        return 'C'

# Call the function `get_letter_grade` with different grades
grade1 = get_letter_grade(97)
print(f"Grade: {grade1}") # Output: Grade: A

grade2 = get_letter_grade(85)
print(f"Grade: {grade2}") # Output: Grade: B

grade3 = get_letter_grade(70)
print(f"Grade: {grade3}") # Output: Grade: C


#********* Function with type hinting for parameters and return value **********

# Define a function that divides two numbers and returns their quotient. Type 
# hinting is used to indicate that integer values should be passed in as 
# arguments, and a float will be returned. It is important to note that Python 
# does not strictly enforce the types passed into for returned from the 
# function.
def divide_numbers(a: int, b: int) -> float:
    quotient = a / b
    return quotient

quotient = divide_numbers(10, 2)
print(quotient) # Output: 5.0

#************************** Function with docstrings ***************************

# The information inside the triple quotes immediately following 
# the function signature is called a docstring. By providing a well-structured 
# docstring, you make it easier for others (including yourself) to understand 
# and use the function. It serves as a useful reference for the function's 
# purpose, input requirements, and expected output. Docstrings are also used by 
# the IDE to provide the user with information.
def calculate_average_speed(distance: float, time: float) -> float:
    """
    Calculates the average speed of a car.

    Args:
        distance (float): The distance traveled by the car in kilometers.
        time (float): The time taken by the car to cover the distance in hours.

    Returns:
        float: The average speed of the car in kilometers per hour.
    """
    average_speed = distance / time
    return average_speed

# Call the function `calculate_average_speed` with sample values
distance_traveled = 150   # kilometers
time_taken = 2.5          # hours
speed = calculate_average_speed(distance_traveled, time_taken)

print("Average speed:", speed, "km/h") # Output: Average speed: 60.0 km/h

#******************** Function with multiple return values *********************

# Calculate and return the area and circumference of a circle
def get_circle_info(radius):
    pi = 3.14159
    area = pi * radius**2
    circumference = 2 * pi * radius
    # Return multiple values separated by commas
    return area, circumference

# Call the function `get_circle_info` and receive multiple return values. 
# Since the function returns two values, we must provide two variables for the 
# values to be assigned. Providing more than two variable will cause an error, 
# and providing one variable will cause the returned values to be placed in a 
# tuple.
circle_area, circle_circumference = get_circle_info(5.0)
print("Area:", circle_area) # Output: Area: 78.53975
print("Circumference:", circle_circumference) # Output: Circumference: 31.4159

#*********** Function called using unpacked iterables for arguments ************

# Print the volume of a cube
def calculate_pyramid_volume(length, width, height=1):
    volume = (length * width * height) / 3
    print(f"Pyramid volume: {volume}")

my_list = [3, 3, 4]
my_tuple = (6, 5, 8)
my_dict = {1:6, 2:5, 3:4} 

# Call the `calculate_pyramid_volume` function using `*` to unpack my_list into 
# separate values
calculate_pyramid_volume(*my_list) # Output: Pyramid volume: 12.0

# Call the `calculate_pyramid_volume` function using `*` to unpack my_tuple 
# into separate values
calculate_pyramid_volume(*my_tuple) # Output: Pyramid volume: 80.0

# Call the `calculate_pyramid_volume` function using `*` to unpack my_dict into 
# separate values. You have to use the dict method `values()` or it will unpack 
# the keys.
calculate_pyramid_volume(*my_dict.values()) # Output: Pyramid volume: 40.0

#**************************** Function using *args *****************************

# The *args syntax is used to pass a variable number of non-keyword arguments 
# to a function. The args parameter name can be any valid variable name, but 
# the preceding asterisk (*) is necessary to indicate that it should collect 
# any extra positional arguments passed to the function.
def calculate_sum(*args):
    total = 0
    # For each number in the arguments that were passed into the function, add 
    # it to `total`
    for num in args:
        total += num
    return total

# Call the function `calculate_sum` with a different number of arguments
result = calculate_sum(1, 2, 3, 4, 5)
print(f"Result of calling 'calculate_sum(1, 2, 3, 4, 5)': {result}")
# Output: Result of calling 'calculate_sum(1, 2, 3, 4, 5)': 15

result = calculate_sum(10, 20, 30)
print(f"Result of calling 'calculate_sum(10, 20, 30)': {result}")
# Output: Result of calling 'calculate_sum(10, 20, 30)': 60

#******************** Function using a parameter and *args *********************

# Take a species and a variable number of names and create a string value to 
# return
def animal_names(species, *names):
    names_list = ", ".join(names)
    message = f"{species} names: {names_list}."
    return message

# Call the function `animal_names` with a species and multiple names
cats = animal_names("Cat", "Whiskers", "Mittens", "Shadow")
print(cats)  # Output: Cat names: Whiskers, Mittens, Shadow.

dogs = animal_names("Dog", "Max", "Bella", "Luna", "Toby")
print(dogs)  # Output: Dog names: Max, Bella, Luna, Toby.

#********** Function using a parameter, default parameter, and *args ***********

def describe_animals(animal_type, *animals, habitat="unknown"):
    """
    Describes animals of a specific type in a given habitat.

    Args:
        animal_type (str): The type of animals.
        *animals: Variable number of animal names.
        habitat (str, optional): The habitat where the animals live. Defaults 
        to "unknown".

    Returns:
        str: A string containing the description of the animals.
    """
    animal_list = ", ".join(animals)
    description = f"The {animal_type} animals in the {habitat} habitat are: "\
                  f"{animal_list}."
    return description

# Calling the function `describe_animals` with `habitat` as Savannah
result = describe_animals("Lion", "Simba", "Mufasa", habitat="Savannah")
print(result)
# Output: The Lion animals in the Savannah habitat are: Simba, Mufasa.

# Calling the function `describe_animals` without specifying the habitat
result = describe_animals("Monkey", "Coco", "Banana")
print(result)
# Output: The Monkey animals in the unknown habitat are: Coco, Banana.

# Calling the function `describe_animals` with `habitat` as Grassland and 
# unpacking a list for the *args arguments
result3 = describe_animals("Giraffe", *["Spike", "Melvin"], habitat="Grassland")
print(result3)
# Output: The Giraffe animals in the Grassland habitat are: Spike, Melvin.

#******************* Function using **kwargs *******************

# The **kwargs syntax in Python allows you to pass a variable number of keyword 
# arguments to a function. The **kwargs parameter collects these keyword 
# arguments into a dictionary within the function. The ** before the parameter 
# name kwargs indicates that it will accept multiple keyword arguments. The ** 
# unpacks the dictionary-like object of keyword arguments. You access key-value 
# pairs in kwargs like you would a dictionary. Like with args, kwargs is a 
# common name, but any valid variable name will be accepted.

def print_details(**kwargs):
    print(f"Keyword dictionary: {kwargs}") 

    # Loop through the kwargs dictionary and print the key, value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the `print_details` function with a person's information
print_details(name="Alice", age=25, city="New York")
# Output:
# Keyword dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# name: Alice
# age: 25
# city: New York

# Calling the `print_details` function with a country's language
print_details(country="USA", language="English")
# Output:
# Keyword dictionary: {'country': 'USA', 'language': 'English'}
# country: USA
# language: English

# Calling the `print_details` function with no keyword arguments
print_details()
# Output:
# Keyword dictionary: {}

#******************* Function using a parameter and **kwargs *******************

def describe_fish(fish_name, **kwargs):
    """
    Describes a fish with additional details.

    Args:
        fish_name (str): The name of the fish.
        **kwargs: Additional keyword arguments for describing the fish.

    Returns:
        str: A string containing the description of the fish.
    """
    # Use the `get()` method on the `kwargs` dictionary to get information or 
    # set it to a default value if that information was not provided.
    color = kwargs.get("color", "unknown color")
    habitat = kwargs.get("habitat", "unknown habitat")
    fins = kwargs.get("fins", 0)
    description = f"A {fish_name} is an {color} fish that inhabits {habitat}." \
                  f"It has {fins} fins."
    return description

# Call the `describe_fish` function with color, habitat, and fins keyword 
# arguments
result1 = describe_fish("Goldfish", color="orange", habitat="freshwater",
                         fins=4)
print(result1)
# Output: A Goldfish is an orange fish that inhabits freshwater. It has 4 fins.

# Call the `describe_fish` function with color and fins keyword arguments
result2 = describe_fish("Clownfish", color="orange", fins=2)
print(result2)
# Output: A Clownfish is an orange fish that inhabits unknown habitat. It has 2 
# fins.

# Call the `describe_fish` function with no keyword arguments
result3 = describe_fish("Barracuda")
print(result3)
# Output: A Barracuda is an unknown color fish that inhabits unknown habitat. 
# It has 0 fins.

#***** Function using a parameter, default parameter, *args, and **kwargs ******

def process_data(name, *args, age=0, **kwargs):
    """
    Process data with various parameters.

    Args:
        name (str): The name of the data.
        *args: Variable-length positional arguments.
        age (int): The age associated with the data (default: 0).
        **kwargs: Additional keyword arguments for processing the data.
    """
    print(f"Processing data: {name}")
    print(f"*args arguments: {args}")
    print(f"Age: {age}")
    print(f"**kwarg arguments: {kwargs}")

# Calling the `process_data` function with only the required argument (name)
process_data("Data 1")
# Output:
# Processing data: Data 1
# *args arguments: ()
# Age: 0
# **kwarg arguments: {}

# Calling the `process_data` function with all arguments
process_data("Data 2", 1, 2, 3, age=30, city="New York")
# Output:
# Processing data: Data 2
# *args arguments: (1, 2, 3)
# Age: 30
# **kwarg arguments: {'city': 'New York'}

# Calling the `process_data` function with all arguments except *args
process_data("Data 3", age=25, country="USA", language="English")
# Output:
# Processing data: Data 2
# *args arguments: ()
# Age: 25
# **kwarg arguments: {'country': 'USA', 'language': 'English'}


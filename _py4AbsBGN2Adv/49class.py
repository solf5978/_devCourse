"""
Author: Jesse Warner
Date: August 1, 2023

A class is a blueprint for creating objects, which are instances of the class. 
Classes provide a way for a programmer to define and organize related data and 
functions into a single entity. They encapsulate attributes (data) and methods 
(functions) that operate on the data within a class.

Key concepts for Python classes:
    - Class Definition: A class is defined by using the `class` keyword, 
      followed by the class name. Typically, class names in Python are written
      using PascalCase, where the first letter of each word is capitalized.

    - Object Creation: After a class is defined, you can create instances of 
      that class by using the class name followed by parenthesis. This process 
      is called instantiation. Each instantiated object is independent and has 
      its own attributes and methods.

    - Attributes: Attributes are variables within a class that hold data 
      specific to each object. You use dot notation to access class attributes 
      (`object.attribute'), and they can either be instance variables (unique 
      to each object) or class variables (shared among all objects of the 
      class).

    - Methods: Methods are functions defined within a class. They perform 
      operations on an object's data and are accessed using dot notation 
      `object.method()`.

    - Constructor: The `__init__()` method is a special method called the 
      constructor and is automatically invoked when an object is instantiated.
      It initializes the object's attributes and sets their initial values.

    - Inheritance: Inheritance allows a programmer to create a new (derived or 
      child) class based on an existing (base or parent) class. The derived 
      class inherits all the attributes and methods of the base class. 

    - Encapsulation: Classes provide a way to encapsulate data and methods 
      together. Encapsulation means that the internal details of a class are 
      hidden from outside access, and only the public interface (attributes and 
      methods) is accessible. This concept promotes data abstraction and allows 
      for more manageable and modular code.

    - Polymorphism: Polymorphism allows objects of different classes to be 
      treated as objects of a common base class. It allows you to define 
      methods with the same name in different classes, and each class can 
      implement the method in its own way. Polymorphism enables code 
      flexibility and supports code reuse in various contexts.

Using classes in Python promotes code organization, modularity, and 
reusability. They help in creating structured and maintainable codebases by 
grouping related data and behavior together. Classes are fundamental to 
object-oriented programming (OOP) and provide a powerful way to model 
real-world concepts and build complex systems.
"""

#********************************* Basic Class *********************************
# A basic class with two class attributes.
class Person:
    # first and last name attributes initialized to empty strings
    first_name = ""
    last_name = ""

# Create an instance of a `Person` object
person1 = Person()

# Set the values of first and last name to `Jesse` and `Warner` using dot 
# notation.
person1.first_name = "Jesse"
person1.last_name = "Warner"

# Print a greeting message using the class attributes
print(f"Hello, {person1.first_name} {person1.last_name}!") 
# Output: Hello, Jesse Warner!

#*************************** Class With Constructor ****************************
# A basic class with instance attributes that uses a constructor to initialize 
# the values instead of modifying them after creating the object.
class Rectangle:
    # The special method __init__ is automatically invoked when an object is 
    # instantiated. The first parameter is used to refer to the instance of a 
    # class and is provided by the interpreter when the class is instaniated. 
    # By convention, this is typically called `self` but could be any valid 
    # variable name.
    def __init__(self, width, height):
        # Assign the instance `width` and `height` attributes using dot 
        # notation with `self` and the arguments passed into the Rectangle 
        # constructor, and create an instance attribute for the area of the 
        # rectangle.
        self.width = width
        self.height = height
        self.area = width * height

# Instantiate a Rectangle object with a width of 5 and height of 3
rect = Rectangle(5, 3)

# Print information about the rectangle
print(f"Width: {rect.width}") # Output: Width: 5
print(f"Height: {rect.height}") # Output: Height: 3
print(f"Area: {rect.area} cm^2") # Output: 15 cm^2

#***************************** Class With A Method *****************************
class Dog:
    # Constructor with the `self` parameter and a parameter for a name.
    def __init__(self, name):
        self.name = name
    
    # A method that uses the `self` argument to invoke the bark method of the
    # specific instance that called it.
    def bark(self):
        print(f'{self.name} says, "Woof!"')

# Create two Dog objects, one named `Max` and the other named `Chief`
dog1 = Dog("Max")
dog2 = Dog("Chief")

# Use dot notation to call the `bark()` method for each Dog object.
dog1.bark() # Output: Max says, "Woof!"
dog2.bark() # Output: Chief says, "Woof!"

#************************* Class With Class Attributes *************************
class Counter:
    # A class attribute that will be consistent across all instances of the 
    # class. Each instance is able to modify this variable.
    count = 0

    def __init__(self, name):
        self.name = name
        Counter.count += 1

# Create two Counter objects
counter1 = Counter("One")
counter2 = Counter("Two")
# Print the class variable count for both objects and the class itself and see 
# they correctly return 2
print(f"Counter {counter1.name} count: {counter1.count}")
# Output: Counter One count: 2
print(f"Counter {counter2.name} count: {counter2.count}")
# Output: Counter Two count: 2
print(f"Class variable count: {Counter.count}")
# Output: Class variable count: 2

# Manually set the second Counter's count to 7
counter2.count = 7
"""
By changing the class variable on a specific object, it will create an 
instance attribute with the same name that shadows the class attribute for that 
specific object. Since Python first looks for instance attributes before class 
attributes, this causes an unexpected outcome.
"""

# Create a third Counter object
counter3 = Counter("Three")

# Print the Counter object's counts and you will now see that 'one' and 'three' 
# print the expected 3, but 'two' prints 7. However, the class attribute is 
# still correctly 3, 'two' now has an instance attribute named 'count'
print(f"Counter {counter1.name} count: {counter1.count}")
# Output: Counter One count: 3
print(f"Counter {counter2.name} count: {counter2.count}")
# Output: Counter Two count: 7
print(f"Counter {counter3.name} count: {counter3.count}")
# Output: Counter Three count: 3
print(f"Class variable count: {Counter.count}")
# Output: Class attributes count: 3

#************************** Class With A Class Method **************************
class Fish:
    # Constructor that takes a species and color as arguments
    def __init__(self, species, color):
        self.species = species
        self.color = color
    
    # Instance method that prints the fish's color and species swims around
    def swim(self):
        print(f"The {self.color} {self.species} swims around!")

    """
    Class method with the `@classmethod` decorator that can create a Fish 
    object when the species, color, or both are not known. The `@classmethod` decorator makes the interpreter pass the class as the implicit first argument when this method is called. The parameter name `cls` is by convention and can be any valid Python variable name.
    """
    @classmethod
    def create_unknown(cls, species="unknown species", color="unknown color"):
        return cls(species, color)
    
# Create a Fish object with the species and color known
fish1 = Fish("snapper", "red")

# Create a Fish object with no information known
fish2 = Fish.create_unknown()

# Create a Fish object with only the color known
fish3 = Fish.create_unknown(color="black")

# Call the `swim()` function for each Fish object
fish1.swim() # Output: The red snapper swims around!
fish2.swim() # Output: The unknown color unknown species swims around!
fish3.swim() # Output: The black unknown species swims around!

#************************** Class With Static Methods **************************
"""
Create a class that will only contain static methods. Static methods are 
commonly used when a method does not depend on any instance-specific data but 
is still related to the class. They are often used for utility functions or 
helper methods that perform operations related to the class but do not 
require any instance state. 

Static methods are created by adding the `@staticmethod` decorator above the 
method signature. The `@staticmethod` decorator makes the method static and the 
interpreter will not pass in any implicit arguments like it would with class or 
instance methods.
"""
class MathUtility:
    # Create a method to add/concatenate two values and give it the 
    # `@staticmethod` decorator. 
    @staticmethod
    def add(a, b):
        return a + b
    
    # Create a method to multiply/repeat two values and give it the 
    # `@staticmethod` decorator. 
    @staticmethod
    def multiply(a, b):
        return a * b
    
    # Create a method to return the square of a value and give it the 
    # `@staticmethod` decorator. 
    @staticmethod
    def square(a):
        return a ** 2

# Create variables for the return values and call the three static methods from 
# the MathUtility class.
add = MathUtility.add(1, 3)
multiply = MathUtility.multiply(2, 3)
square = MathUtility.square(4)

print(f"MathUtility add 1 and 3: {add}") 
# Output: MathUtility add 1 and 3: 4

print(f"MathUtility multiply 2 and 3: {multiply}") 
# Output: MathUtility multiply 2 and 3: 6

print(f"MathUtility square 4: {square}") 
# Output: MathUtility square 4: 16

#************************* Class With Special Methods **************************

# Create a car class that takes a color, make, model, and year as arguments.
class Car:
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    # Define the special method `__str__` which returns a string representation 
    # of an object
    def __str__(self) -> str:
        return f"A {self.color} {self.make} {self.model} made in {self.year}"
    
    # Define the special method `__eq__` that defines the behavior of the 
    # equality operator (==) for objects of this class.
    def __eq__(self, other) -> bool:
        # Check to make sure the other object is a Car object by using the 
        # `isinstance()` function.
        if isinstance(other, Car):
            # Compare the make, model, and year of the two Car objects and 
            # return whether they are equal
            return (
                self.make == other.make
                and self.model == other.model
                and self.year == other.year
            )
        # Return False if the other object is not a Car object
        return False
    
# Create 3 Car objects
car1 = Car("Black", "Chevy", "Silverado", 2023)
car2 = Car("Red", "Ford", "Explorer", 2015)
car3 = Car("Blue", "Chevy", "Silverado", 2023)

# Print the string representation of the `Car` objects
print(car1) # Output: A Black Chevy Silverado made in 2023
print(car2) # Output: A Red Ford Explorer made in 2015

# Check if two `Car` objects are equal. 
result = car1 == car2
print(f"car1 and car2 are equal: {result}") 
# Output: car1 and car2 are equal: False

# Check if two `Car` objects are equal. Since the special method `__eq__` only 
# checks the make, model, and year, these two car objects evaluate to `True` 
# even though their colors are different.
result = car1 == car3
print(f"car1 and car3 are equal: {result}") 
# Output: car1 and car3 are equal: True

#*************************** Class With Inheritance ****************************
# Create the parent class Dessert
class Dessert:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor
    # Define a method that that child and parent classes can access
    def Cook(self):
        print(f"You bake the {self.flavor} {self.name}!")

# Create a child class called Cake that inherits from Dessert
class Cake(Dessert):
    # Define a method only the Cake class can access
    def Cut(self):
        print(f"You cut a piece of the {self.name}!")

"""
Create a child class called Cookie that inherits from Dessert and has a 
unique attribute. In the Cookie class, when you call Dessert.__init__(self, 
name, flavor), you are explicitly invoking the constructor of the Dessert 
class. Since the __init__ method of Dessert takes self as the first 
parameter, you need to pass the instance of the Cookie class as the self 
argument to the Dessert constructor. This way, the Dessert constructor can 
initialize the attributes name and flavor for the Cookie instance.
"""
class Cookie(Dessert):
    def __init__(self, name, flavor, price):
        Dessert.__init__(self, name, flavor)
        self.price = price
    # Define a method only the Cookie class can access
    def Dunk(self):
        print(f"You dunk the {self.name} in milk!")

# Create an instance of the parent class
pie = Dessert("pie", "apple")

# Create an instance of the Cookie child class
cookie = Cookie("cookie", "chocolate chip", 4.99)

# Create an instance of the Cake child class
cake = Cake("cake", "black forest cherry")

# Call the parent class method for each dessert
pie.Cook() # Output: You bake the apple pie!
cookie.Cook() # Output: You bake the chocolate chip cookie!
cake.Cook() # Output: You bake the black forest cherry cake!

# Call the child class methods for each child of Dessert
cookie.Dunk() # Output: You dunk the cookie in milk!
cake.Cut() # Output: You cut a piece of the cake!

#********************* Class With Inheritance and super() **********************
# Create a parent class with attributes that all children classes will share
class Boat:
    def __init__(self, length, type):
        self.length = length
        self.type = type

    # Print the type and length of the boat
    def info(self):
        print(f"This boat is a {self.type} and is {self.length}ft long.")

"""
Create a child class of Boat that has an additional attribute for number of 
seats. The super() method is used to call a method from the base class (also 
known as the superclass) within the context of the derived class (also known 
as the subclass). It allows you to access and invoke methods from the base 
class even if they are overridden in the derived class. This is useful when 
you want to extend the functionality of the base class and then call the base 
class's method to ensure proper initialization or to reuse code.
"""
class Canoe(Boat):
    def __init__(self, length, type, num_seats):
        super().__init__(length, type)
        self.num_seats = num_seats

    # Print the number of seats the canoe has
    def canoe_info(self):
        print(f"This canoe has {self.num_seats} seats.")

# Create a child class of Boat that has additional attributes for a mast height 
# and ballast weight
class Sailboat(Boat):
    def __init__(self, length, type, mast_height, ballast_weight):
        super().__init__(length, type)
        self.mast_height = mast_height
        self.ballast_weight = ballast_weight

    # Print the mast height and ballast weight for the sailboat
    def sailboat_info(self):
        print(f"This sailboat's mast is {self.mast_height}ft tall, and the " 
              f"ballast weighs {self.ballast_weight}lbs.")

# Instantiate objects for the parent and two children classes
kayak = Boat(13, "Kayak")
canoe = Canoe(15, "Canoe", 3)
sailboat = Sailboat(30, "Sailboat", 35, 500)

# Invoke the `info` method on the Boat object
kayak.info() # Output: This boat is a Kayak and is 13ft long.

# Invoke the base class `info` method on the child class Canoe object
canoe.info() # Output: This boat is a Canoe and is 15ft long.

# Invoke the child class `canoe_info` method on the child class Canoe object
canoe.canoe_info() # Output: This canoe has 3 seats.

# Invoke the child class `sailboat_info` function on the child class Sailboat 
# object
sailboat.sailboat_info() 
# Output: This sailboat's mast is 35ft tall, and the ballast weighs 500lbs.


#************************** Class With Polymorphism ****************************
# Create a parent class with attributes and methods shared by all child classes
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    # Base class attack method
    def attack(self):
        print(f"{self.name} attacks!")

# Create a child class of Monster called Goblin
class Goblin(Monster):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    # Override the base class `attack` method to provide an implementation that 
    # is specific to the `Goblin` class
    def attack(self):
        print(f"{self.name} swings {self.weapon}!")

class Dragon(Monster):
    def __init__(self, name, health, element):
        super().__init__(name, health)
        self.element = element

    # Override the base class `attack` method to provide an implementation that 
    # is specific to the `Dragon` class
    def attack(self):
        print(f"{self.name} breathes {self.element}!")

# Create a Cat class that implements an `attack` method
class Cat:
    def __init__(self, name):
        self.name = name
    def attack(self):
        print(f"{self.name} attacks the string!")

"""
Define a function called attack. When an object is passed into the function, 
Python will attempt to invoke the object's attack method, if it exists. 
Polymorphism is a concept in object-oriented programming that allows objects 
of different classes to be treated as objects of a common superclass. It 
enables a single interface (the attack(obj) function) to represent multiple 
types of objects, making the code more flexible and reusable.
"""
def attack(obj):
    obj.attack()

# Create parent and child objects of the `Monster` class
rat = Monster("Rat", 10)
goblin = Goblin("Goblin", 50, "Club")
dragon = Dragon("Dragon", 200, "Fire")

# Create an instance of the Cat class
cat = Cat("Mittens")

# Invoke the attack function and pass in different objects to see how that 
# single interface can work seamlessly with objects of different types, if they 
# have the required attributes.
attack(rat)            # Output: Rat attacks!
attack(goblin)         # Output: Goblin swings Club!
attack(dragon)         # Output: Dragon breathes Fire!
attack(cat)            # Output: Mittens attacks the string!



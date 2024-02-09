# Python - More Classes and Objects

## TASKS

0. Simple rectangle
   - Write an empty class `Rectangle` that defines a rectangle
0. Real definition of a rectangle
   - Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)
0. Area and Perimeter
   - Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)
0. String representation
   - Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)
0. Eval is magic
   - Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)
0. Detect instance deletion
   - Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)
0. How many instances
   - Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)
0. Change representation
   - Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)
0. Compare rectangles
   - Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)
0. A square is a rectangle
   - Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)

### class rectangle

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter def `height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a TypeError exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
  - Initialized to `0`
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Public class attribute `print_symbol`:
  - Initialized to `#`
  - Used as symbol for string representation
  - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
  - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
  - Returns `rect_1` if both have the same area value
- Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
- You are not allowed to import any module

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- What are the special `__str__` and `__repr__` methods and how to use them
- What is the difference between `__str__` and `__repr__`
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain `__dict__` of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the `getattr` function

### Object-Oriented Programming (OOP)
- OOP in Python is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc., in the programming.

### "First-class everything"
- In Python, everything is an object (or first-class citizen), including functions, classes, modules, etc. This means they can be assigned to variables, passed as arguments, or used as return values in functions.

### Class
- A class is a blueprint for creating objects (a particular data structure), providing initial values for state (attributes), and implementations of behavior (methods).

### Object and Instance
- An object is an instantiation of a class. When a class is defined, only the description for the object is defined. An instance is a specific object created from a particular class.

### Difference Between a Class and an Object/Instance
- A class is a blueprint for objects; an object is an instance of a class. When you create an object, you are creating an instance of a class with its own state and behavior.

### Attribute
- Attributes are variables that belong to a class or an instance of a class. They represent the state or data of the object.

### Public, Protected, and Private Attributes
- `Public attributes` can be freely used inside or outside of a class definition.
- `Protected attributes` are intended for internal use. They are denoted by a single underscore `_`.
- Private attributes are inaccessible and invisible from outside. They are denoted by double underscores `__`.

### self
- self in Python is used to represent the instance of the class. It binds the attributes with the given arguments.

### Method
- A method in a class is a function that belongs to an object. Unlike a function, methods are called on an object.

### __init__ Method
- `__init__` is a special method in Python classes. It is called when an object is created from a class and allows the class to initialize the attributes of the class.

### Data Abstraction, Data Encapsulation, and Information Hiding
- `Data Abstraction` is the concept of providing only essential information to the outside world.
- `Data Encapsulation` is a method where data and the code that manipulates the data are bundled together.
- `Information Hiding` is about hiding the internal states and functionalities.

### Property
- A property in Python refers to a special kind of attribute, whose access (read or write) can be controlled by getter, setter, and deleter methods.

### Difference Between an Attribute and a Property
- An attribute is a value stored in an object, whereas a property provides a controlled interface to that attribute using getter and setter methods.

### Pythonic way to write getters and setters
- The Pythonic way to write getters and setters is by using the `@property` decorator.

### Special __str__ and __repr__ Methods
- `__str__` is used for creating output for end-users.
- `__repr__` is used for debugging and development.

### Difference Between __str__ and __repr__
- The main difference is the goal of each. `__str__` is readable and for end-users, while `__repr__` is more for debugging and development, showing internal representations.

### Class Attribute
- Class attributes belong to the class itself, they are shared by all instances.

### Difference Between Object Attribute and Class Attribute
- Object attributes are specific to each instance of a class, whereas class attributes are shared by all instances.

### Class Method and Static Method
- `Class method` takes `cls` as the first parameter and can access class attributes.
- `Static method` doesn't take `self` or `cls`, but behaves like a regular function that belongs to a class.

### Dynamically Creating Arbitrary New Attributes
- Python allows adding new attributes to instances of a class dynamically, by simply assigning a value to an attribute that wasn't previously defined.

### Binding Attributes to Object and Classes
- Attributes can be bound to objects or classes by assignment (`obj.attribute = value` or `ClassName.attribute = value`).
- `__dict__`
- `__dict__` is a dictionary containing all the attributes and their values for an object or class instance.

### Attribute Resolution in Python
- Python finds attributes using a specific order: instance __dict__, class __dict__, and the base classes.

### getattr Function
`getattr` is used to access the attribute value of an object dynamically, e.g., `getattr(obj, 'attribute_name')`.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

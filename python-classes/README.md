# Python - Classes and Objects

## TASKS

0. My first square
   - Write an empty class `Square` that defines a square
0. Square with size
   - Write a class `Square` that defines a square by: (based on `0-square.py`)
0. Size validation
   - Write a class `Square` that defines a square by: (based on `1-square.py`)
0. Area of a square
   - Write a class `Square` that defines a square by: (based on `2-square.py`)
0. Access and update private attribute
   - Write a class `Square` that defines a square by: (based on `3-square.py`)
0. Printing a square
   - Write a class `Square` that defines a square by: (based on `4-square.py`)
0. Coordinates of a square
   - Write a class `Square` that defines a square by: (based on `5-square.py`)

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
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
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the `getattr` function

### What is OOP:
- OOP is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods). It emphasizes modularity, reusability, and encapsulation.

### “First-Class Everything” in Python:
- In Python, everything is an object (including classes, functions, numbers, etc.), meaning they can be assigned to variables, passed as arguments, returned from functions, etc.

### What is a Class:
- A class is a blueprint for creating objects (a particular data structure), providing initial values for state (attributes), and implementations of behavior (methods).

### Object and Instance:
- An `object` is a unique instance of a data structure defined by its class. An `instance` refers to a concrete occurrence of any object.

### Difference Between a Class and an Instance:
- A class is a blueprint for creating instances. Each instance is an object constructed from this class, with its own set of attributes and methods.

### What is an Attribute:
- An attribute is a variable that belongs to an instance or class. For example, an `Employee` class might have `name` and `age` as attributes.

### Public, Protected, and Private Attributes:
- `Public attributes` can be freely used inside or outside of a class definition.
- `Protected attributes` (prefixed with a single underscore `_`) should not be used outside of the class definition, unless inside of a subclass definition.
- `Private attributes` (prefixed with double underscores `__`) are inaccessible and invisible from outside the class definition.

### What is self:
- `self` in Python is a reference to the current instance of the class, used to access variables that belong to the class.

### What is a Method:
- A method is a function that is associated with an object. In Python, all methods require `self` as their first parameter.
#### The __init__ Method:
- `__init__` is a special method in Python classes, called a constructor, used to initialize a newly created object. It's called when an object is created from a class.

### Data Abstraction, Encapsulation, and Information Hiding:
- `Data Abstraction`: The representation of essential features without including background details.
- `Encapsulation`: The bundling of data and methods that operate on the data within one unit.
- `Information Hiding`: Restricting access to certain parts of an object's data or methods.

### What is a Property:
- A property in Python is a special kind of attribute that provides a way to use getters and setters when accessing data.

### Attribute vs. Property in Python:
- An attribute is a value stored in an object, while a property is an interface to access and set a specific attribute.

### Pythonic Way to Write Getters and Setters:
- Use `@property` to define getters and setters in a Pythonic way.

### Dynamically Creating Attributes:
- You can dynamically add new attributes to existing instances by simply assigning to an attribute that doesn’t yet exist.

### Binding Attributes to Objects and Classes:
- You can bind attributes to objects or classes by assigning values to a variable name in the class or object.

### What is the __dict__:
- `__dict__` is a dictionary or other mapping object used to store an object's (writable) attributes.

### Finding Attributes of an Object or Class:
- Python searches for attributes in an object's `__dict__` attribute, then in the class's `__dict__`, and then in the base classes, following the method resolution order.

### Using getattr Function:
- `getattr(object, 'attribute', default)` is used to access the attribute of an object dynamically. If the attribute is not found, `default` is returned if provided.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
# Python - Inheritance

## TASKS

0. Lookup
   - Write a function that returns the list of available attributes and methods of an object:
     - Prototype: `def lookup(obj):`
     - Returns a `list` object
     - You are not allowed to import any module

0. My list
   - Write a class `MyList` that inherits from `list`:
     - Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
     - You can assume that all the elements of the list will be of type `int`
     - You are not allowed to import any module

0. Exact same object
   - Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.
     - Prototype: `def is_same_class(obj, a_class):`
     - You are not allowed to import any module

0. Same class or inherit from
   - Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
     - Prototype: `def is_kind_of_class(obj, a_class):`
     - You are not allowed to import any module

0. Only sub class of
   - Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
     - Prototype: `def inherits_from(obj, a_class):`
     - You are not allowed to import any module

0. Geometry module
   - Write an empty class `BaseGeometry`.
     - You are not allowed to import any module

0. Write a class `BaseGeometry` (based on `5-base_geometry.py`).
   - Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
   - You are not allowed to import any module

0. Integer validator
   - Write a class `BaseGeometry` (based on `6-base_geometry.py`).
     - Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
     - Public instance method: `def integer_validator(self, name, value):` that validates `value`:
       - you can assume `name` is always a string
       - if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
       - if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
     - You are not allowed to import any module

0. Rectangle
   - Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
     - Instantiation `with` width and `height`: `def __init__(self, width, height):`
       - `width` and `height` must be private. No getter or setter
       - `width` and `height` must be positive integers, validated by `integer_validator`

0. Full rectangle
   - Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task `based on 8-rectangle.py`)
     - Instantiation `with` width and `height`: `def __init__(self, width, height):`
       - `width` and `height` must be private. No getter or setter
       - `width` and `height` must be positive integers, validated by `integer_validator`
     - the `area()` method must be implemented
     - `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

0. Square #1
   - Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):
     - Instantiation with `size`: `def __init__(self, size):`:
       - `size` must be private. No getter or setter
       - `size` must be a positive integer, validated by `integer_validator`
     - the `area()` method must be implemented

0. Square #2
   - Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).
     - Instantiation with `size`: `def __init__(self, size):`:
       - `size` must be private. No getter or setter
       - `size` must be a positive integer, validated by `integer_validator`
     - the `area()` method must be implemented
     - `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

### Superclass, Baseclass, or Parentclass
- A superclass, baseclass, or parentclass in object-oriented programming is a class that is inherited from by other classes. It's the "parent" in the relationship, providing a template or blueprint with attributes and methods that subclasses can inherit.

### Subclass
- A subclass is a class that inherits from a superclass. It can add new attributes and methods or modify existing ones inherited from the superclass, thus extending or customizing the functionality.

### Listing All Attributes and Methods
- To list all attributes and methods of a class or an instance, you can use the built-in `dir()` function. This function returns a list of valid attributes and methods for that object.
```bash
class MyClass:
    pass

obj = MyClass()
print(dir(obj))  # Lists all attributes and methods of instance obj
```

### Instance Having New Attributes
- In Python, instances can have new attributes assigned to them dynamically, even if those attributes were not defined in the class.
```bash
obj.new_attribute = "New Value"  # Adding a new attribute to obj
```

### Inheriting from Another Class
- To inherit a class from another, simply pass the parent class as a parameter in the class definition.
```bash
class Parent:
    pass

class Child(Parent):
    pass
```

### Defining a Class with Multiple Base Classes
- Python supports multiple inheritance, where a class can be derived from more than one base class.
```bash
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
```

### Default Class Every Class Inherits From
- Every class in Python inherits from the base class object, either directly or indirectly.
```bash
class MyClass:
    pass

# MyClass inherits from 'object' implicitly
```

### Overriding Inherited Methods or Attributes
- You can override a method or attribute inherited from the base class by defining a method or attribute with the same name in the subclass.
```bash
class Parent:
    def my_method(self):
        print("Parent method")

class Child(Parent):
    def my_method(self):
        print("Child method")
```

### Attributes and Methods Available by Heritage to Subclasses
- Subclasses inherit all non-private methods and attributes from the superclass. This includes special methods like `__init__` and `__str__`.

### Purpose of Inheritance
- Inheritance enables code reuse and the creation of hierarchical structures. It allows for the extension and customization of classes without modifying the original class code.

### Built-in Functions: isinstance, issubclass, type, and super
- `isinstance(object, classinfo)` checks if an object is an instance of a class or of a subclass thereof.
- `issubclass(class, classinfo)` checks if a class is a subclass of another.
- `type(object)` returns the type of an object.
- `super()` returns a temporary object of the superclass, allowing you to call methods of the superclass.
```bash
class Parent:
    pass

class Child(Parent):
    pass

child_obj = Child()
print(isinstance(child_obj, Parent))  # True
print(issubclass(Child, Parent))      # True
print(type(child_obj))                # <class '__main__.Child'>
```

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

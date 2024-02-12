# Python - Everything is object

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

### What is an Object?
In Python, an object is an entity that contains data along with associated metadata and functionality. Everything in Python is an object, including numbers, strings, functions, classes, etc.

### Difference Between a Class and an Object or Instance
- `Class:` A class is a blueprint for creating objects. It defines a set of attributes and methods that characterize any object of the class.
- `Object/Instance:` An object (or instance) is a concrete occurrence of a class. It is created using the class blueprint and can have its own specific data.

### Difference Between Immutable and Mutable Objects
`Immutable Object:` An immutable object cannot be altered after it is created. Examples include `int`, `float`, `bool`, `str`, `tuple.
`Mutable Object:` A mutable object can be modified after it is created. Examples include `list`, `dict`, `set`.

### What is a Reference?
- In Python, a reference is a name that points to an object stored in memory. When you create a variable, you are creating a reference to an object.

### What is an Assignment?
- Assignment in Python means binding a reference (a variable) to an object. When you assign a value to a variable, you are creating a reference to an object.

### What is an Alias?
- An alias occurs when two or more variables refer to the same object in memory. For example, if you have `a = [1, 2]` and then do `b = a`, `b` is an alias for `a`.

### How to Know if Two Variables are Identical?
- You can use the `is` operator to check if two variables (references) point to the same object.

### How to Display the Variable Identifier?
- The `id()` function returns a unique identifier for an object, which is its memory address in the CPython implementation.

### Mutable vs Immutable
- `Mutable:` Objects whose value can change. Mutable objects can be altered or their contents can be modified post-creation.
- `Immutable:` Objects whose value is unchangeable once they are created.

### Built-in Mutable Types
- Examples include `list`, `dict`, `set`, and user-defined classes (unless specifically made immutable).

### Built-in Immutable Types
- Examples include `int`, `float`, `bool`, `str`, `tuple`, and `frozenset`.

### How Does Python Pass Variables to Functions?
- Python uses a mechanism known as "pass-by-object-reference" or "pass-by-assignment". The function receives a reference to the actual object. If the object is mutable, the function may modify it. However, if you reassign the parameter to a new object within the function, the external reference remains unchanged.

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

### .txt Answer Files
- Only one line
- No Shebang on the first line (i.e. “#!/usr/bin/python3”)
- All your files should end with a new line

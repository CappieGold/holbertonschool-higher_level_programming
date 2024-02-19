![image](https://github.com/CappieGold/holbertonschool-higher_level_programming/assets/144028326/255c2a0b-7988-4278-850b-da2b9e9b5420)

# Python - Almost a circle

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

### Unit Testing

Unit testing involves testing individual components of a program (usually functions or methods) in isolation from the rest of the application. In a large project, this is critical to ensure that each part of the codebase functions correctly.

#### Implementation in Large Projects:
- `Organize Tests Logically:` For large projects, organize tests into separate files and directories that mirror the structure of your codebase.
- `Use a Testing Framework:` Python's unittest module is commonly used. It offers features like test fixtures, test cases, test suites, and a test runner to enable automated testing.
- `Write Test Cases:` Create a class derived from unittest.TestCase for each module or functionality, and write methods within these classes to test different aspects of your code.
- `Run Tests Regularly:` Integrate testing into your development process and use continuous integration tools to automate testing.

### Serialization and Deserialization

Serialization is the process of converting a data object (like a Python class instance) into a format that can be stored or transmitted (like JSON), and deserialization is the reverse process.

#### JSON Serialization:
- Use the `json` module in Python.
- Serialize an object: `json.dumps(my_object)` converts an object to a JSON string.
- Deserialize an object: `json.loads(json_string)` converts a JSON string back into a Python object.

### Working with JSON Files

#### Writing to a JSON file:
```bash
import json
with open('file.json', 'w') as f:
    json.dump(my_data, f)
```

#### Reading from a JSON file:
```bash
with open('file.json', 'r') as f:
    my_data = json.load(f)
```

### *args and **kwargs

#### *args:
- Used to pass a variable number of non-keyword arguments to a function.
- Inside the function, it behaves like a tuple.
- Example:
```bash
def function(*args):
    for arg in args:
        print(arg)
```

#### **kwargs:
- Used to pass a variable number of keyword arguments (named arguments) to a function.
- Inside the function, it behaves like a dictionary.
- Example:
```bash
def function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### Handling Named Arguments in a Function

- You can define a function that accepts named arguments, which are essentially key-value pairs.
- Use `**kwargs` to accept an arbitrary number of named arguments.
- Example:
```bash
def greet(**kwargs):
    name = kwargs.get('name', 'Guest')
    age = kwargs.get('age')
    if age:
        print(f"Hello, {name}. You are {age} years old.")
    else:
        print(f"Hello, {name}.")
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
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the `unittest module`
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start with `test_`
- Your file organization in the tests folder should be the same as your project: ex: for `models/base.py`, unit tests must be in: `tests/test_models/test_base.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
- We strongly encourage you to work together on test cases so that you don’t miss any edge case

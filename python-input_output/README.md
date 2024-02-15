# Python - Input/Output

## TASKS

0. Read file
   - Write a function that reads a text file (`UTF8`) and prints it to stdout:
     - Prototype: `def read_file(filename=""):`
     - You must use the `with` statement
     - You don’t need to manage `file permission` or `file doesn't exist` exceptions.
     - You are not allowed to import any module

0. Write to a file
   - Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:
     - Prototype: `def write_file(filename="", text=""):`
     - You must use the `with` statement
     - You don’t need to manage file permission exceptions.
     - Your function should create the file if doesn’t exist.
     - Your function should overwrite the content of the file if it already exists.
     - You are not allowed to import any module

0. Append to a file
   - Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:
     - Prototype: `def append_write(filename="", text=""):`
     - If the file doesn’t exist, it should be created
     - You must use the `with` statement
     - You don’t need to manage `file permission` or `file doesn't exist` exceptions.
     - You are not allowed to import any module

0. To JSON string
   - Write a function that returns the JSON representation of an object (string):
     - Prototype: `def to_json_string(my_obj):`
     - You don’t need to manage exceptions if the object can’t be serialized.

0. From JSON string to Object
   - Write a function that returns an object (Python data structure) represented by a JSON string:
     - Prototype: `def from_json_string(my_str):`
     - You don’t need to manage exceptions if the JSON string doesn’t represent an object.

0. Save Object to a file
   - Write a function that writes an Object to a text file, using a JSON representation:
     - Prototype: `def save_to_json_file(my_obj, filename):`
     - You must use the `with` statement
     - You don’t need to manage exceptions if the object can’t be serialized.
     - You don’t need to manage file permission exceptions.

0. Create object from a JSON file
   - Write a function that creates an Object from a “JSON file”:
     - Prototype: `def load_from_json_file(filename):`
     - You must use the `with` statement
     - You don’t need to manage exceptions if the JSON string doesn’t represent an object.
     - You don’t need to manage file permissions / exceptions.

0. Load, add, save
   - Write a script that adds all arguments to a Python list, and then save them to a file:
     - You must use your function `save_to_json_file` from `5-save_to_json_file.py`
     - You must use your function `load_from_json_file` from `6-load_from_json_file.py`
     - The list must be saved as a JSON representation in a file named `add_item.json`
     - If the file doesn’t exist, it should be created
     - You don’t need to manage file permissions / exceptions.

0. Class to JSON
   - Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
     - Prototype: `def class_to_json(obj):`
     - `obj` is an instance of a Class
     - All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
     - You are not allowed to import any module

0. Student to JSON
   - Write a class `Student` that defines a student by:
     - Public instance attributes:
       - `first_name`
       - `last_name`
       - `age`
     - Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
     - Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
     - You are not allowed to import any module

0. Student to JSON with filter
   - Write a class `Student` that defines a student by: (based on `9-student.py`)
     - Public instance attributes:
       - `first_name`
       - `last_name`
       - `age`
     - Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
     - Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
       - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
       - Otherwise, all attributes must be retrieved
     - You are not allowed to import any module

0. Student to disk and reload
   - Write a class `Student` that defines a student by: (based on `10-student.py`)
     - Public instance attributes:
       - `first_name`
       - `last_name`
       - `age`
     - Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
     - Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
       - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
       - Otherwise, all attributes must be retrieved
     - Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
       - You can assume `json` will always be a dictionary
       - A dictionary key will be the public attribute name
       - A dictionary value will be the value of the public attribute
     - You are not allowed to import any module

0. Pascal's Triangle
   - Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
     - Returns an empty list if `n <= 0`
     - You can assume `n` will be always an integer
     - You are not allowed to import any module

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is `JSON`
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
- How to access command line parameters in a Python script

### Opening a file
- Use the `open()` function. For instance, `open('file.txt', 'r')` opens a file in read mode.
```bash
file = open('example.txt', 'r')
```

### Writing text in a file
- Use the `write()` method on a file opened in write mode (`'w'`).
```bash
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
```

### Reading the full content of a file
- Use the `read()` method.
```bash
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Reading a file line by line
- Iterate over the file object or use `readline()`
```bash
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
```

### Moving the cursor in a file
- Use the `seek()` method.
```bash
file = open('example.txt', 'r')
file.seek(0)  # Go to the beginning of the file
```

### Ensuring a file is closed after its use
- Use the `with` statement which guarantees the file will be closed after the block of code.
```bash
with open('example.txt', 'r') as file:
    content = file.read()
# File is automatically closed here
```

### The 'with' statement
- It's used for resource management and simplifies exception handling.
```bash
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
```

### What is JSON
- A lightweight data-interchange format that's easy for humans to read and write, and easy for machines to parse and generate.
```bash
import json
data = {"name": "John", "age": 30}
json_data = json.dumps(data)
print(json_data)
```

### Serialization and Deserialization
- Serialization is converting an object into a format that can be saved or transmitted (like JSON or XML). Deserialization is the reverse process.
```bash
# Serialization
serialized_data = json.dumps(data)

# Deserialization
deserialized_data = json.loads(serialized_data)
```

### Converting a Python data structure to a JSON string
- Use `json.dumps()`.
```bash
python_data = {'name': 'Jane', 'age': 25}
json_string = json.dumps(python_data)
```

### Converting a JSON string to a Python data structure
- Use `json.loads()`.
```bash
python_data = json.loads(json_string)
```

### Accessing command line parameters
- Use the `sys` module and `sys.argv`.
```bash
import sys

# Accessing command line arguments
if len(sys.argv) > 1:
    print(f"Argument received: {sys.argv[1]}")
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

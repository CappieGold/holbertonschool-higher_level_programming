# Python - import & modules

## TASKS

0. Import a simple function from a simple file
   - Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
0. My first toolbox!
   - Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
0. How to make a script dynamic!
   - Write a program that prints the number of and the list of its arguments.
0. Infinite addition
   - Write a program that prints the result of the addition of all arguments
0. Who are you?
   - Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally in your sandbox using curl).
0. Everything can be imported
   - Write a program that imports the variable a from the file variable_load_5.py and prints its value.

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

### Why Python Programming is Awesome:
- `Ease of Learning and Readability`: Python has a clear and readable syntax, making it accessible for beginners.
- `Versatility`: Used in web development, data analysis, artificial intelligence, data science, and much more.
- `Strong Community Support`: A wide range of libraries and frameworks backed by an active community.
- `Portability`: Python is cross-platform. It works on Windows, macOS, Linux.
- `Rapid Development`: Python is ideal for rapid application development due to its simplicity.

### How to Import Functions from Another File:
- Create a Python file (e.g., `module.py`) and define some functions.
- In another file, use `import module` to access those functions.

### How to Use Imported Functions:
After importing, use `module.function()` to call a function from the module.

### How to Create a Module:
- A module is simply a `.py` file containing Python definitions and statements. For example, a file `my_module.py` with some functions can be imported and used in other Python scripts.

### How to Use the Built-in Function dir():
- `dir()` is used to list the defined names in a module. It provides a sorted list of variable names, functions, classes, etc.
- Use `dir(module)` to see the attributes of the imported module.

### How to Prevent Code in Your Script from Being Executed When Imported:
- Use if `__name__ == "__main__":` to allow a script to be used as an importable module without running certain parts of the code upon import.

### How to Use Command Line Arguments with Your Python Programs:
- Python provides a built-in module `sys` for accessing command-line arguments.
- `sys.argv` is a list in Python, which contains the command-line arguments passed to the script.
- Import it via `import sys` and access the arguments using `sys.argv`.
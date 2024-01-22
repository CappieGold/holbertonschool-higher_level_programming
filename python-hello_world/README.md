# Python - Hello, World

## TASKS

0. Hello, print
   - Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
0. Print integer
   - Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
0. Print float
   - Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
0. Print string
   - Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
0. Play with strings
   - Complete this source code to print Welcome to Holberton School!
0. Copy - Cut - Paste
   - Complete this source code
0. Create a new sentence
   - Complete this source code to print object-oriented programming with Python, followed by a new line.
0. Easter Egg
   - Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- How to use the Python interpreter
- How to print text and variables using `print`
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with `pycodestyle`

### Using the Python Interpreter:
- The Python interpreter is a program that reads and executes Python code. You can use it as a calculator or to run scripts.
- To access the interpreter, just type python in your command line (CMD on Windows, Terminal on macOS and Linux). This will open an interactive session where you can type Python code directly.
- In this mode, you can type Python commands and they will be executed as soon as you press Enter.

### Printing Text and Variables Using print:
- The print() function is used to display output in Python.
- You can print simple text by enclosing it in quotes. For example: `print("Hello, World!")`.
- To print variables, just pass them into the `print()` function. For example:
```bash
x = 10
print(x)
```
- You can also combine text and variables using a comma `,` or the string formatting method. For instance:
```bash
name = "Jeremy"
print("Hello,", name)
```

### Using Strings:
- Strings in Python are sequences of characters enclosed in quotes (either single `'` or double `"`).
- You can assign a string to a variable: `greeting = "Hello, World!"`.
- Strings have many built-in methods for manipulation, like `upper()` for uppercase: `greeting.upper()` would return `"HELLO, WORLD!"`.

### Indexing and Slicing in Python:
- `Indexing` is used to access individual characters in a string. Python indices start at 0. For example, `greeting[0]` would return `'H'`.
- `Slicing` is used to access a subset of the string. It's done with `[start:stop]`, where `start` is inclusive and `stop` is exclusive. For example, `greeting[0:5]` would return `'Hello'`.
- You can also use negative indices to start from the end of the string. For instance, `greeting[-1]` gives the `last character`.

### Python Coding Style and pycodestyle:
- The official Python coding style guide is PEP 8. It includes rules for formatting Python code to make it more readable and consistent.
- To check your code against these standards, you can use tools like `pycodestyle`.
- To use `pycodestyle`, first install it using `pip`:
```bash
pip install pycodestyle
```
- Then, run it against your Python file:
```bash
pycodestyle your_script.py
```
- `pycodestyle` will give you a list of any style issues in your code.

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
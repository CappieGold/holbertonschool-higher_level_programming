# Python - Test-driven development

## TAKS

0. Integers addition
   - Write a function that adds 2 integers.
0. Divide a matrix
   - Write a function that divides all elements of a matrix.
0. Say my name
   - Write a function that prints `My name is <first name> <last name>`
0. Print square
   - Write a function that prints a square with the character `#`.
0. Text indentation
   - Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
0. Max integer - Unittest
   - Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.
   - In this task, you will write unittests for the function `def max_integer(list=[]):`.

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

### What is an Interactive Test:
- An interactive test is one that requires user interaction during its execution, such as entering data while the test runs. In Python, this can be achieved with scripts that prompt for user input.

### Importance of Tests:
- `Bug Reduction`: Identifying problems early in the development process.
- `Quality Assurance`: Ensuring that the code works as intended.
- `Facilitating Updates`: Tests allow for code changes with the confidence that existing functionalities won’t break.

### Writing Docstrings to Create Tests:
- In Python, you can write tests within the docstrings of a function using the `doctest` module.
- Docstrings should contain examples of how to use the function and the expected outcome.
- Example:
```bash
def add(a, b):
    """
    Returns the sum of a and b.
    
    >>> add(1, 2)
    3
    """
    return a + b
```

### Documenting Each Module and Function:
- Every module and function should have a docstring describing what it does.
- The docstring should include a description, parameters, return type, and examples.

### Basic Options for Creating Tests:
- Use `doctest` for simple tests embedded in docstrings.
- Use `unittest` for more elaborate tests organized in test classes.
- Example command: `python -m doctest -v your_script.py` to run `doctest` tests.

### Finding Edge Cases:
- Edge cases are unusual or exceptional situations in using a function.
- To identify them, think about unusual scenarios, like empty inputs, extreme values, or incorrect data types.
- Include these cases in your tests to ensure your code handles them appropriately.

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
- Allowed editors: `vi`, `vim`, `emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

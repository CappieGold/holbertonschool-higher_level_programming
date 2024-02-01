# Python - Exceptions

## TASKS

0. Safe list printing
   - Write a function that prints x elements of a list.
0. Safe printing of an integers list
   - Write a function that prints an integer with "{:d}".format().
0. Print and count integers
   - Write a function that prints the first x elements of a list and only integers.
0. Integers division with debug
   - Write a function that divides 2 integers and prints the result.
0. Divide a list
   - Write a function that divides element by element 2 lists.
0. Raise exception
   - Write a function that raises a type exception.
0. Raise a message
   - Write a function that raises a name exception with a message.

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

### Difference Between Errors and Exceptions:
- `Errors`: These are issues in the program that are typically not recoverable. They often result from fundamental problems (like syntax errors).
- `Exceptions`: These are raised when the program encounters an error during execution, but potentially recoverable. They occur, for example, when trying to open a non-existent file or divide by zero.

### What are Exceptions and How to Use Them:
- Exceptions are events that occur during program execution that disrupt the normal flow of instructions.
- In Python, exceptions are triggered automatically on errors, or you can trigger them manually with the `raise` statement.
- Use `try` and `except` blocks to handle exceptions. Code that might raise an exception is put in the `try` block, and the handling of the exception is done in the `except` block.

### When to Use Exceptions:
- Use exceptions when dealing with unpredictable scenarios, like user input, file operations, or network operations.

### How to Correctly Handle an Exception:
- Identify the exception you want to handle.
- Use a `try` block to enclose the code that might cause an exception.
- Use one or more `except` blocks to specify how to handle different exceptions.

### Purpose of Catching Exceptions:
- To maintain control over the program flow in the face of errors.
- To add logic for gracefully handling error scenarios, like logging errors or cleaning up resources.

### How to Raise a Builtin Exception:
- Use the `raise` keyword followed by an exception name: `raise ValueError("Invalid value")`.

### When to Implement a Clean-up Action After an Exception:
- When your program uses resources like file handles or network connections, you often need to ensure these are properly released or closed, even if an error occurs.
- Use a `finally` block to implement clean-up actions. This block will run regardless of whether an exception occurred.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
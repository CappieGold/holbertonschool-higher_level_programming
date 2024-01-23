# Python - if/else, loops, functions

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- Why indentation is so important in Python
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use the `while` and `for` loops
- How to use the `break` and `continues` statements
- How to use `else` clauses on loops
- What does the `pass` statement do, and when to use it
- How to use `range`
- What is a function and how do you use functions
- What does return a function that does not use any `return` statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

### Importance of Indentation in Python:
- Indentation (whitespace at the beginning of a line) is crucial in Python because it defines the scope of loops, functions, and classes. Unlike many other languages that use braces `{}` to define scope, Python uses indentation, making the code neat and readable.

### Using if, if...else Statements:
- These are conditional statements. `if` executes a block of code if a condition is true. `if...else` adds an additional path when the `if` condition is false.
```bash
x = 10
if x > 5:
    print("Greater than 5")
else:
    print("Not greater than 5")
```

### Using Comments:
- Comments are used to explain the code. In Python, a comment starts with `#`.
```bash
# This is a comment
print("Hello, World!")  # Inline comment
```

### Assigning Values to Variables:
- Variables are assigned with the = operator, and they don't need explicit type declaration.
```bash
x = 10
y = "Hello"
```

### Using while and for Loops:
- `while` loop continues as long as a condition is true.
```bash
i = 1
while i <= 5:
    print(i)
    i += 1
```

- `for` loop iterates over a sequence (like a list, tuple, string) or other iterable objects.
```bash
for i in range(1, 6):
    print(i)
```

### Using break and continue Statements:
- `break` exits the loop entirely.
- `continue` skips the current iteration and continues with the next.
```bash
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

### Else Clauses on Loops:
- An `else` block after a loop is executed only if the loop completes normally (without hitting a `break` statement).
```bash
for i in range(1, 4):
    print(i)
else:
    print("Loop finished")
```

### Pass Statement:
- `pass` is a null statement, a placeholder when a statement is required syntactically but you don't want any command or code to execute.
```bash
if x > 5:
    pass  # Will do nothing
```

### Using Range:
- `range()` is used to generate a sequence of numbers. Often used in for loops.
```bash
for i in range(1, 6):  # Generates numbers from 1 to 5
    print(i)
```

### Functions and Their Use:
- Functions are defined using def and are used to encapsulate reusable code.
```bash
def greet(name):
    return f"Hello, {name}!"
print(greet("Jeremy"))
```

### Return of a Function Without Return Statement:
A function without a `return` statement returns `None` by default.

### Scope of Variables:
The scope of a variable determines where it can be accessed. Python has local, enclosing, global, and built-in scopes. Variables defined inside a function are local unless declared global or nonlocal.

### Traceback:
A traceback is an error report that shows the path of execution leading up to the error, helping in debugging.

### Arithmetic Operators:
Basic arithmetic operators in Python include `+`, `-`, `*`, `/` for addition, subtraction, multiplication, and division respectively. There's also % for modulus, ** for power, and // for floor division.

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
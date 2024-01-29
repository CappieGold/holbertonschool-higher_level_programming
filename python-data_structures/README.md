# Python - Data Structures: Lists, Tuples

## TASKS

0. Print a list of integers
   - Write a function that prints all integers of a list.
0. Secure access to an element in a list
   - Write a function that retrieves an element from a list.
0. Replace element
   - Write a function that replaces an element of a list at a specific position.
0. Print a list of integers... in reverse!
   - Write a function that prints all integers of a list, in reverse order.
0. Replace in a copy
   - Write a function that replaces an element in a list at a specific position without modifying the original list.
0. Can you C me now?
   - Write a function that removes all characters c and C from a string.
0. Lists of lists = Matrix
   - Write a function that prints a matrix of integers.
0. Tuples addition
   - Write a function that adds 2 tuples.
0. More returns!
   - Write a function that returns a tuple with the length of a string and its first character.
0. Find the max
   - Write a function that finds the biggest integer of a list.
0. Only by 2
   - Write a function that finds all multiples of 2 in a list.
0. Delete at
   - Write a function that deletes the item at a specific position in a list.
0. Switch
   - Complete the source code in order to switch value of a and b

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the `del` statement and how to use it

### What are Lists and How to Use Them:
- Lists are mutable sequences, typically used to store collections of homogeneous items.
- Creating a list: `my_list = [1, 2, 3]` or `my_list = list()`.
- Accessing elements: `my_list[0]` (returns `1`).
- Modifying elements: `my_list[0] = 10`.
- Common operations: appending (`my_list.append(4)`), removing (`my_list.remove(2)`), and iterating.

### Differences and Similarities Between Strings and Lists:
- `Similarities`: Both are sequences, support indexing and slicing (`my_string[1:3]`, `my_list[1:3]`).
- `Differences`: Lists are mutable, whereas strings are immutable. You can change an item in a list, but not in a string.

### Common Methods of Lists:
- `append(x)`: Add an item to the end.
- `extend(iterable)`: Extend the list by appending elements from the iterable.
- `pop([i])`: Remove and return an item at the given position.
- `sort()`: Sort the items.

### Using Lists as Stacks and Queues:
- `Stacks (LIFO)`: Use `append()` to push an item and `pop()` to pop an item.
- `Queues (FIFO)`: Use `append()` to enqueue and `pop(0)` to dequeue. For large queues, consider using `collections.deque`.

### List Comprehensions:
- A concise way to create lists: `[expression for item in iterable]`.
- Example: squares = `[x**2 for x in range(10)]`.

### What are Tuples and How to Use Them:
- Tuples are immutable sequences, typically used to store heterogeneous data.
- Creating a tuple: `my_tuple = (1, "Hello", 3.14)`.
- Accessing elements: `my_tuple[1]` (returns `"Hello"`).

### When to Use Tuples Versus Lists:
- Use tuples for heterogeneous data and when immutability is required. Lists are better for homogeneous data and when data needs to change.

### What is a Sequence:
- A sequence is an ordered collection of items. Lists, tuples, and strings are examples of sequences in Python.

### Tuple Packing:
- Assigning values to a tuple without parentheses: `my_tuple = 1, "Hello", 3.14`.

### Sequence Unpacking:
- Assigning the elements of a sequence to different variables: `a, b, c = my_tuple`.

### The del Statement:
- Used to delete objects in Python. With lists, it can remove specific items: `del my_list[0]` removes the first item.

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

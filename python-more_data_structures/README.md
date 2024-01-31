# Python - More Data Structures: Set, Dictionary

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- Why Python programming is awesome
- What are sets and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate into a set
- What are dictionaries and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate over a dictionary
- What is a lambda function
- What are the map, reduce and filter functions

### Why Python Programming is Awesome:
- `Ease of Use`: Python's syntax is clear and intuitive, making it an excellent choice for beginners.
- `Versatility`: Used in web development, data science, automation, and more.
- `Rich Ecosystem`: A vast collection of libraries and frameworks.
- `Community Support`: Large and active community.

### Sets and Their Usage:
- A set is an unordered collection of unique elements.
- Example: `my_set = {1, 2, 3}`.
- Useful for operations like unions, intersections, and checking for membership.

### Common Methods of Set:
- `add(element)`: Adds an element.
- `remove(element)`: Removes an element.
- `union(other_set)`, `intersection(other_set)`, `difference(other_set)` for set operations.

### When to Use Sets Versus Lists:
- Use sets when you need uniqueness for the elements and order is not important.
- Lists are ordered collections, suitable when order matters.

### Iterating Into a Set:
- Use a for loop: for element in my_set:.
- Order of elements is not guaranteed.

### Dictionaries and Their Usage:
- Dictionaries store key-value pairs and are ideal for fast lookups.
- Example: `my_dict = {'name': 'Neo', 'age': 30}`.
- Access elements: `my_dict['name']`.

### When to Use Dictionaries Versus Lists or Sets:
- Use dictionaries when you need a logical association between key:value pairs.
- Lists are better for ordered sequences of items; sets are used for unique elements.

### What is a Key in a Dictionary:
- A key is a unique identifier where its associated value can be accessed in a dictionary.

### Iterating Over a Dictionary:
- Use `for key, value in my_dict.items()`:.
- Can also iterate through `my_dict.keys()` or `my_dict.values()`.

### What is a Lambda Function:
- A lambda function is a small anonymous function.
- Example: `lambda x: x * 2` doubles the input value.

### Map, Reduce, and Filter Functions:
- `map(function, iterable)`: Applies a function to every item of an iterable.
- `filter(function, iterable)`: Filters items out of an iterable.
- `reduce(function, iterable)`: Applies a rolling computation by applying a function to pairs of elements (needs to be imported from `functools`).

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
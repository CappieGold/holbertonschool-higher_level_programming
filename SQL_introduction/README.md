# SQL - Introduction

## Learning Objectives
At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are `subqueries`
- How to use MySQL functions

### What's a database?
- A database is an organized system for storing, managing, and retrieving data. It allows for storing large amounts of information in a structured way, facilitating easy access, management, and updating of data.

### What's a relational database?
- A relational database is a type of database that stores data in related tables. The data is organized in rows and columns, and the relationships between tables allow for structured and efficient querying and management of the data.

### What does SQL stand for?
- SQL stands for Structured Query Language. It's a standardized language used to query, manipulate, and manage relational databases.

### What's MySQL?
- MySQL is an open-source relational database management system (RDBMS). It's widely used for database creation and management, especially popular in web development.

### How to create a database in MySQL?
- To create a database in MySQL, you use the following command:
```bash
CREATE DATABASE database_name;
```

### What do DDL and DML stand for?
- DDL stands for Data Definition Language. It includes commands that define the structure of a database, like `CREATE`, `ALTER`, and `DROP`.
- DML stands for Data Manipulation Language. It includes commands used to manipulate data within the database, like `INSERT`, `UPDATE`, `DELETE`, and `SELECT`.

### How to CREATE or ALTER a table?
- To create a table:
```bash
CREATE TABLE table_name (
  column1 data_type,
  column2 data_type,
  ...
);
```

- To alter a table:
```bash
ALTER TABLE table_name
ADD column_name data_type;
```

### How to SELECT data from a table?
- You can select data using the SELECT command:
```bash
SELECT column1, column2 FROM table_name WHERE condition;
```

### How to INSERT, UPDATE, or DELETE data?
- To insert data: `INSERT INTO table_name (column1, column2) VALUES (value1, value2);`
- To update data: `UPDATE table_name SET column1 = value1 WHERE condition;`
- To delete data: `DELETE FROM table_name WHERE condition;`

### What are subqueries?
- A subquery is an SQL query nested inside another query. Subqueries allow for complex operations, where the result of one query is used as a condition or data set for another query.

### How to use MySQL functions?
- MySQL offers a variety of functions for performing operations on data. For example, you can use functions like `SUM()`, `AVG()`, `COUNT()` for mathematical operations, or `UPPER()`, - - `LOWER()` for string manipulation. Use these functions in a `SELECT` query to apply the corresponding operation to the selected data.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info

### Comments for your SQL file:
```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

Connect to your MySQL server:
```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

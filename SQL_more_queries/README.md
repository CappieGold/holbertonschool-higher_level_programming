# SQL - More queries

## Learning Objectives
At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a `PRIMARY KEY`
- What’s a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

### Creating a new MySQL user
- To create a new user, you can use the `CREATE USER` command. Here's an example of how to create a user:
```bash
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
```

### Managing privileges for a user to a database or table
- Once the user is created, you can grant them privileges on a specific database or table using the `GRANT` command. For example:
```bash
GRANT ALL PRIVILEGES ON my_database.* TO 'new_user'@'localhost';
```

### PRIMARY KEY
- A primary key is a column or a set of columns used to uniquely identify each row in a table. Each table can have only one primary key, and none of the fields in it can accept `NULL` values. For example:
```bash
CREATE TABLE my_table (
    id INT NOT NULL,
    name VARCHAR(100),
    PRIMARY KEY (id)
);
```

### FOREIGN KEY
- A foreign key is one or more columns in a table that reference the primary key in another table. It's used to maintain data integrity between tables. For example:
```bash
CREATE TABLE another_table (
    id INT,
    my_table_id INT,
    FOREIGN KEY (my_table_id) REFERENCES my_table(id)
);
```

### NOT NULL and UNIQUE constraints
- `NOT NULL`: This constraint ensures that a column cannot have a `NULL` value.
- `UNIQUE`: This constraint ensures that all values in a column are different.
```bash
CREATE TABLE my_table (
    id INT NOT NULL,
    email VARCHAR(100) UNIQUE
);
```

### Retrieving data from multiple tables in one request
- You can retrieve data from multiple tables in a single query using joins (`JOIN`). For example:
```bash
SELECT * FROM table1
JOIN table2 ON table1.id = table2.table1_id;
```

### Subqueries
- Subqueries are SQL queries nested within another query to provide necessary data for the main query. For example:
```bash
SELECT * FROM table1 WHERE id IN (SELECT table1_id FROM table2);
```

### JOIN and UNION
- `JOIN` is used to combine rows from two or more tables based on a related column between them.
- `UNION` is used to combine the results from two or more queries into a single result set, excluding duplicates. Use `UNION ALL` to include duplicates.
```bash
SELECT * FROM table1
UNION
SELECT * FROM table2;
```

## Requirements
- Allowed editors: `VsCode`, `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## How to import a SQL dump
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
# Python - Object-relational mapping

## Learning Objectives
At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

### Connecting to a MySQL Database

#### Using mysql-connector-python:
1. Install the library: `pip install mysql-connector-python`.
1. Connect to the database:
```bash
import mysql.connector

cnx = mysql.connector.connect(user='username', password='password',
                              host='localhost',
                              database='database_name')
cursor = cnx.cursor()
```

### Selecting Rows
```bash
query = ("SELECT column1, column2 FROM table_name WHERE condition")
cursor.execute(query)

for (column1, column2) in cursor:
    print(f"{column1}, {column2}")

cursor.close()
cnx.close()
```

### Inserting Rows
```bash
add_entry = ("INSERT INTO table_name "
             "(column1, column2) "
             "VALUES (%s, %s)")
data_entry = ('data1', 'data2')
cursor.execute(add_entry, data_entry)

cnx.commit()
cursor.close()
cnx.close()
```

### ORM (Object-Relational Mapping)
- ORM is a programming technique for converting data between incompatible database systems and programming language objects. It allows developers to work with high-level objects instead of SQL queries.

### Mapping a Python Class to a MySQL Table with SQLAlchemy
1. Install SQLAlchemy: `pip install SQLAlchemy`.
1. Define a model that represents a table in the database:
```bash
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

engine = create_engine('mysql+mysqlconnector://username:password@localhost/database_name')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
```

#### To insert:
```bash
new_user = User(name='John', age=30)
session.add(new_user)
session.commit()
```

#### To select:
```bash
users = session.query(User).filter_by(name='John').all()
for user in users:
    print(user.id, user.name, user.age)
```

These examples show basic operations for interacting with a MySQL database using Python and an overview of using an ORM to abstract these operations.

## Requirements
- Allowed editors: `VsCode`, `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Your files will be executed with `MySQLdb` version `2.0.x`
- Your files will be executed with `SQLAlchemy` version `1.4.x`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use `execute` with sqlalchemy

## Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed.
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

## Install SQLAlchemy module version 1.4.x
```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

Also, you can have this warning message:
```bash
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)
```
You can ignore it.
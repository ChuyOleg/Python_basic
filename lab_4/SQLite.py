import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connected to SQLite")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query_sqlite(connection, query):
    cursor = connection.cursor()
    try:
        result = cursor.execute(query)
        connection.commit()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


sqlLite_db = create_connection("server.db")

create_table_1_query = """
CREATE TABLE IF NOT EXISTS system(
    id INT PRIMARY KEY AUTOINCREMENT,
    unit_location INT,
    depart_location TEXT,
    employee INT,
    FOREIGN KEY (employee) REFERENCES person (id),
    FOREIGN KEY (unit_location) REFERENCES location (id)
);
"""

create_table_2_query = """
CREATE TABLE IF NOT EXISTS person(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INT,
    salary INT
);
"""

create_table_3_query = """
CREATE TABLE IF NOT EXISTS location(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
"""

fill_table_1_query = """
INSERT INTO system(unit_location, depart_location, employee)
VALUES
    (1, 'Svyatoshin', 3),
    (1, 'Solomyanskiy', 5),
    (1, 'Obolon', 1),
    (3, 'Phrankivskiy', 2),
    (3, 'Sihovskiy', 8),
    (3, 'Zaliznicnhiy', 4),
    (2, 'Industrialniy', 9),
    (2, 'Slobidskiy', 7),
    (2, 'Onsovyanskiy', 6);
"""

fill_table_2_query = """
INSERT INTO person(name, age, salary)
VALUES 
    ('Rodgo Mark', 27, 2200),
    ('Smith Will', 21, 1400),
    ('Turner Elliot', 28, 3000),
    ('Johnson Lisa', 25, 1700),
    ('Williams Henry', 35, 2900),
    ('Garcia Patricia', 38, 2500),
    ('Miller John', 22, 1200),
    ('Davis Susan', 32, 1600),
    ('Lopez Richard', 25, 1800)
"""

fill_table_3_query = """
INSERT INTO location(name)
VALUES
    ('Kyiv'),
    ('Lviv'),
    ('Kharkiv')
"""

# create table in sqlLite
execute_query_sqlite(sqlLite_db, create_table_2_query)
execute_query_sqlite(sqlLite_db, create_table_3_query)
execute_query_sqlite(sqlLite_db, create_table_1_query)

# fill table
# execute_query_sqlite(sqlLite_db, fill_table_2_query)
# execute_query_sqlite(sqlLite_db, fill_table_3_query)
# execute_query_sqlite(sqlLite_db, fill_table_1_query)

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

create_table_query = """
CREATE TABLE IF NOT EXISTS system(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_location TEXT,
    depart_location TEXT,
    employee TEXT
);
"""

fill_table_query = """
INSERT INTO system(unit_location, depart_location, employee)
VALUES
    ('Kyiv', 'Svyatoshin', 'Rodgo Mark'),
    ('Kyiv', 'Solomyanskiy', 'Smith Will'),
    ('Kyiv', 'Obolon', 'Turner Elliot'),
    ('Lviv', 'Phrankivskiy', 'Johnson Lisa'),
    ('Lviv', 'Sihovskiy', 'Williams Henry'),
    ('Lviv', 'Zaliznicnhiy', 'Garcia Patricia'),
    ('Kharkiv', 'Industrialniy', 'Miller John'),
    ('Kharkiv', 'Slobidskiy', 'Davis Susan'),
    ('Kharkiv', 'Onsovyanskiy', 'Lopez Richard');
"""

# create table in sqlLite
execute_query_sqlite(sqlLite_db, create_table_query)

# fill table
# execute_query_SQLite(sqlLite, fill_table_query)

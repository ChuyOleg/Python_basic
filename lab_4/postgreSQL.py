import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Connected to postgreSQL")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database (postgreSQL) created successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_query_postgreSQL(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The Error '{e}' occurred")


create_table_query = """
CREATE TABLE IF NOT EXISTS my_table (    
    id SERIAL PRIMARY KEY,
    unit_location TEXT,
    depart_location TEXT,
    employee TEXT
)    
"""

# connection_to_pgSQL = create_connection(
#     "postgres", "postgres", "postgreSQL", '127.0.0.1', '5432'
# )

# create_database_query = "CREATE DATABASE db_pgSQL"
# create_database(connection_to_pgSQL, create_database_query)

pgSQL_db = create_connection(
    "db_pgsql", "postgres", "postgreSQL", "127.0.0.1", "5432"
)

execute_query_postgreSQL(pgSQL_db, create_table_query)

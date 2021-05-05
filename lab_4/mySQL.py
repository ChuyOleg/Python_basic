import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name='None'):
    connection = None
    try:
        if db_name == 'None':
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
        else:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
        print("Connected to mySQL")
    except Error as e:
        print(f"The error '{e} occurred")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_database_query = "CREATE DATABASE IF NOT EXISTS db_mySQL"
db = create_connection("localhost", 'oleg', '88888888', 'db_mySQL')

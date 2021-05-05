import sqlite3
from sqlite3 import Error
from mySQL import *

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connected to SQLite")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# db = create_connection('server.db')
# sql = db.cursor()

# sql.execute("""CREATE TABLE IF NOT EXISTS users (
#     login text,
#     password text,
#     cash int
# )""")
#
# db.commit()
#
# require = input('"Do you want to add one more user? (yes | no) => ')
#
# while require == 'yes':
#     user_login = input('Login: ')
#     user_password = input('Password: ')
#     if sql.fetchone() is None:
#         sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
#         db.commit()
#         print('Registered.')
#     else:
#         print("This raw has already existed!")
#     require = input('"Do you want to add one more user? (yes | no) => ')
#
# for value in sql.execute("SELECT * FROM users"):
#     print(value)

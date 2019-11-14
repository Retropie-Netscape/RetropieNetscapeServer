import sqlite3

def create_connection(db_file):
    #Creates connection to the specified sqlite3 database

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
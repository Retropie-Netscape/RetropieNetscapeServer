import sqlite3

class DatabaseConnection:
    
    def create_connection(db_file):
        #Creates connection to the specified sqlite3 database

        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

    def get_connection() -> str:
        return 
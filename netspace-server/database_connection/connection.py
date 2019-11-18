import sqlite3
from sqlite3 import Error


class DatabaseConnection:

    def __init__(self, db_file: str):
        super().__init__(self)
        # Creates connection to the specified sqlite3 database
        self.conn = None

        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

    def get_connection(self):
        return self.conn

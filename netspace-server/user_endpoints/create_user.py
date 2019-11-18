from ..database_connection.connection import DatabaseConnection
from flask import (
    Flask,
    Request,
    Response
)


def create_new_user(connection: DatabaseConnection, req: Request) -> str:
    cursor = connection.conn.cursor()
    
    jsonData = req.get_json()
    if jsonData is None:
        return '400'
    else:
        cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?);", (jsonData['username'], jsonData['ip-address'], 'null', 'null'))
        return '200'


def update_ip(connection: DatabaseConnection, req: Request) -> str:
    cursor = connection.get_connection().cursor()

    jsonData = req.get_json()

    if jsonData is None:
        return '400'
    else:
        username = jsonData['username']
        newaddress = jsonData['ip-address']
        cursor.execute('UPDATE USER SET ip_address=? WHERE username=?;', (newaddress, username))
        return '200'

from connection import DatabaseConnection
from flask import (
    Request
)
import json


def create_new_user(req: Request):
    connection = DatabaseConnection('userbase.db')
    cursor = connection.conn.cursor()
    
    jsonData = (req.get_json())
    if jsonData is None:
        return {'serverCode': 400}
    else:
        cursor.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?);",
                       (jsonData['username'], jsonData['ipAddress'], jsonData['port'],
                        'null', 'null', jsonData['mode']))
        connection.conn.commit()
        return {'serverCode': 200}


def update_ip(req: Request):
    connection = DatabaseConnection('userbase.db')
    cursor = connection.conn.cursor()

    jsonData = (req.get_json())

    if jsonData is None:
        return {'serverCode': 400}
    else:
        username = jsonData['username']
        newaddress = jsonData['ipAddress']
        port = jsonData['port']
        cursor.execute('UPDATE USER SET ipaddress=?, port=? WHERE username=?;', (newaddress, port, username))
        connection.conn.commit()
        return {'serverCode': 200}


def update_leaderboard_stats(req: Request):
    connection = DatabaseConnection('userbase.db')
    cursor = connection.get_connection().cursor()

    jsonData = (req.get_json())

    if jsonData is None:
        return {'serverCode': 400}

    else:
        username = jsonData['username']
        mostplayedgame = jsonData['mostPlayedGame']
        mostplayedsystem = jsonData['mostPlayedSystem']
        cursor.execute('UPDATE USER SET mostplayedgame=?, mostplayedsystem=? WHERE username=?;',
                       (mostplayedgame, mostplayedsystem, username))
        connection.conn.commit()

        return {'serverCode': 200}

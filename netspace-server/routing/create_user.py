from connection import DatabaseConnection
from flask import (
    Request
)


def create_new_user(connection: DatabaseConnection, req: Request):
    cursor = connection.conn.cursor()
    
    jsonData = req.get_json()
    if jsonData is None:
        return {'serverCode': 400}
    else:
        cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?, ?, ?);",
                       (jsonData['username'], jsonData['ip-address'], jsonData['port'],
                        'null', 'null', jsonData['mode']))
        connection.conn.commit()
        return {'serverCode': 200}


def update_ip(connection: DatabaseConnection, req: Request):
    cursor = connection.conn.cursor()

    jsonData = req.get_json()

    if jsonData is None:
        return {'serverCode': 400}
    else:
        username = jsonData['username']
        newaddress = jsonData['ip-address']
        port = jsonData['port']
        cursor.execute('UPDATE USER SET ip_address=?, port=? WHERE username=?;', (newaddress, port, username))
        connection.conn.commit()
        return {'serverCode': 200}


def update_leaderboard_stats(connection: DatabaseConnection, req: Request):
    cursor = connection.get_connection().cursor()

    jsonData = req.get_json()

    if jsonData is None:
        return {'serverCode': 400}

    else:
        username = jsonData['username']
        mostplayedgame = jsonData['mostPlayedGame']
        mostplayedsystem = jsonData['mostPlayedSystem']
        cursor.execute('UPDATE USER SET most_played_game=?, most_played_system=? WHERE username=?;',
                       (mostplayedgame, mostplayedsystem, username))
        connection.conn.commit()

        return {'serverCode': 200}

from ..database_connection.connection import DatabaseConnection
from flask import Request


def get_user_connection_details(connection: DatabaseConnection, request: Request):
    cursor = connection.conn.cursor()
    jsondata = request.get_json()

    if jsondata is None:
        return '400'
    else:
        username = jsondata['username']
        ip = cursor.execute('SELECT ipAddress FROM USER WHERE username=?', (username, ))
        return ip


def get_user_info(connection: DatabaseConnection, reqeust: Request):
    cursor = connection.conn.cursor()
    jsondata = reqeust.get_json()

    if jsondata is None:
        return '400'
    else:
        username = jsondata['username']
        ip = cursor.execute('SELECT ipAddress FROM USER WHERE username=?', (username,))
        mostplayedgame = cursor.execute('SELECT mostPlayedGame FROM USER WHERE username=?', (username, ))
        mostplayedemulator = cursor.execute('SELECT mostPlayedEmulator FROM USER WHERE username=?', (username, ))
        infolist = [ip, mostplayedgame, mostplayedemulator]

        return infolist

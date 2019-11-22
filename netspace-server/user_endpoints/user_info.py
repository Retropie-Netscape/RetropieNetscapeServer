from ..database_connection.connection import DatabaseConnection
from flask import Request


def get_user_connection_details(connection: DatabaseConnection, request: Request):
    cursor = connection.conn.cursor()
    jsondata = request.get_json()

    if jsondata is None:
        return {'serverCode': 400}
    else:
        username = jsondata['username']
        ip = cursor.execute('SELECT ipAddress FROM USER WHERE username=?', (username, ))
        return {'ipAddress': '\'' + ip + '\'', 'serverCode': 200}


def get_user_info(connection: DatabaseConnection, reqeust: Request):
    cursor = connection.conn.cursor()
    jsondata = reqeust.get_json()

    if jsondata is None:
        return {'serverCode': 400}
    else:
        username = jsondata['username']
        ip = cursor.execute('SELECT ipAddress FROM USER WHERE username=?;', (username,))
        port = cursor.execute('SELECT port FROM USER WHERE username=?;', (username,))
        mostplayedgame = cursor.execute('SELECT mostPlayedGame FROM USER WHERE username=?;', (username, ))
        mostplayedemulator = cursor.execute('SELECT mostPlayedEmulator FROM USER WHERE username=?;', (username, ))
        jsonlist = {
            'ipAddress': '\'' + ip + '\'',
            'port': '\'' + port + '\'',
            'mostPlayedGame': '\'' + mostplayedgame + '\'',
            'mostPlayedEmulator': '\'' + mostplayedemulator + '\'',
            'serverCode': 200
        }

        return jsonlist


def get_leaderboard_details(connection: DatabaseConnection, req: Request):
    cursor = connection.conn.cursor()
    jsondata = req.get_json()

    if jsondata is None:
        return {'serverCode': 400}
    else:
        username = jsondata['username']
        mostplayedgame = cursor.execute('SELECT mostPlayedGame FROM USER WHERE username=?;', (username,))
        mostplayedemulator = cursor.execute('SELECT mostPlayedEmulator FROM USER WHERE username=?;', (username,))
        jsonlist = {
            'mostPlayedGame': '\'' + mostplayedgame + '\'',
            'mostPlayedEmulator': '\'' + mostplayedemulator + '\'',
            'serverCode': 200
        }

        return jsonlist
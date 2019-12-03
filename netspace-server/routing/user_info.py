from connection import DatabaseConnection
from flask import Request
import json

def get_user_connection_details(request: Request):
    connection = DatabaseConnection('userbase.db')
    cursor = connection.conn.cursor()
    jsondata = json.loads(request.get_json())

    if jsondata is None:
        return {'serverCode': 400}
    else:
        username = jsondata['username']
        cursor.execute('SELECT ipaddress FROM user WHERE username=?', (username, ))
        ip = cursor.fetchone()
        cursor.execute('SELECT port FROM user WHERE username=?', (username, ))
        port = cursor.fetchone()
        cursor.execute('SELECT netplaymode FROM user WHERE username=?', (username, ))
        mode = cursor.fetchone()

        return {'ipAddress': '\'' + ip + '\'',
                'port': '\'' + port + '\'',
                'mode': '\'' + mode + '\'',
                'serverCode': 200
                }


def get_user_info(reqeust: Request):
    connection = DatabaseConnection('userbase.db')
    cursor = connection.conn.cursor()
    jsondata = json.loads(reqeust.get_json())

    if jsondata is None:
        return {'serverCode': 400}
    else:
        username = jsondata['username']
        cursor.execute('SELECT ipaddress FROM user WHERE username=?;', (username,))
        ip = cursor.fetchone()
        cursor.execute('SELECT port FROM user WHERE username=?;', (username,))
        port = cursor.fetchone()
        cursor.execute('SELECT mostplayedgame FROM user WHERE username=?;', (username, ))
        mostplayedgame = cursor.fetchone()
        cursor.execute('SELECT mostplayedemulator FROM user WHERE username=?;', (username, ))
        mostplayedemulator = cursor.fetchone()
        cursor.execute('SELECT mode FROM user WHERE username=?', (username, ))
        mode = cursor.fetchone()

        jsonlist = {
            'ipAddress': '\'' + ip + '\'',
            'port': '\'' + port + '\'',
            'mostPlayedGame': '\'' + mostplayedgame + '\'',
            'mostPlayedEmulator': '\'' + mostplayedemulator + '\'',
            'serverCode': 200,
            'mode': '\'' + mode + '\''
        }

        return jsonlist


def get_leaderboard_details(req: Request):
    connection = DatabaseConnection('userbase.db')
    cursor = connection.conn.cursor()
    jsondata = json.loads(req.get_json())

    if jsondata is None:
        return {'serverCode': 400}
    else:
        username = jsondata['username']
        cursor.execute('SELECT mostplayedgame FROM user WHERE username=?;', (username,))
        mostplayedgame = cursor.fetchone()
        cursor.execute('SELECT mostplayedemulator FROM user WHERE username=?;', (username,))
        mostplayedemulator = cursor.fetchone()

        jsonlist = {
            'mostPlayedGame': '\'' + mostplayedgame + '\'',
            'mostPlayedEmulator': '\'' + mostplayedemulator + '\'',
            'serverCode': 200
        }

        return jsonlist

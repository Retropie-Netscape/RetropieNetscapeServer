from connection import DatabaseConnection
from flask import Request
import json

def get_user_connection_details(request: Request):
    connection = DatabaseConnection('userbase.db')
    cursor = connection.conn.cursor()
    jsondata = (request.get_json())

    if jsondata is None:
        return {'serverCode': 400}
    else:
        username = jsondata['username']
        cursor.execute('SELECT ipaddress FROM user WHERE username=?', (username, ))
        ip = cursor.fetchone()

        data = {
            'ipAddress': '\'' + ip[1] + '\'',
            'port': '\'' + ip[2] + '\'',
            'mode': '\'' + ip[5] + '\'',
            'serverCode': 200
        }

        return data


def get_user_info(reqeust: Request):
    connection = DatabaseConnection('userbase.db')
    cursor = connection.conn.cursor()
    jsondata = (reqeust.get_json())

    if jsondata is None:
        return {'serverCode': 400}
    else:
        username = jsondata['username']
        cursor.execute('SELECT ipaddress FROM user WHERE username=?;', (username,))
        ip = cursor.fetchone()

        jsonlist = {
            'ipAddress': '\'' + ip[1] + '\'',
            'port': '\'' + ip[2] + '\'',
            'mostPlayedGame': '\'' + ip[3] + '\'',
            'mostPlayedEmulator': '\'' + ip[4] + '\'',
            'serverCode': 200,
            'mode': '\'' + ip[5] + '\''
        }

        return jsonlist


def get_leaderboard_details(req: Request):
    connection = DatabaseConnection('userbase.db')
    cursor = connection.conn.cursor()
    jsondata = (req.get_json())

    if jsondata is None:
        return {'serverCode': 400}
    else:
        username = jsondata['username']
        cursor.execute('SELECT mostplayedgame FROM user WHERE username=?;', (username,))
        mostplayedgame = cursor.fetchone()

        jsonlist = {
            'mostPlayedGame': '\'' + mostplayedgame[3] + '\'',
            'mostPlayedEmulator': '\'' + mostplayedgame[4] + '\'',
            'serverCode': 200
        }

        return jsonlist

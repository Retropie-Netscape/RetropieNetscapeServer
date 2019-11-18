from flask import (
    Flask,
    request,
    Response
)
from ..user_endpoints import create_user
from ..user_endpoints import user_info
from ..database_connection.connection import DatabaseConnection

# Create the application instance
app = Flask(__name__)
connection = DatabaseConnection('userbase.db')

# Create a URL route in our application for "/username"
@app.route('/user', methods=['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        serverstatus = create_user.create_new_user(connection, request)
        response = Flask.make_response(app, serverstatus)
        return response
    else:
        userdata = user_info.get_user_connection_details(connection, request)
        response = Flask.make_response(app, userdata)
        return response


@app.route('/user/connection-details', methods=['GET', 'PUT'])
def connection_details():
    if request.method == 'PUT ':
        return Flask.make_response(app, create_user.update_ip(connection, request))
    else:
        ipaddress = user_info.get_user_connection_details(connection, request)
        response = Flask.make_response(app, ipaddress)
        return response
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
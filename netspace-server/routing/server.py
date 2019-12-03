from flask import (
    Flask,
    request
)
import create_user
import user_info
from connection import DatabaseConnection

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/username"
@app.route('/user', methods=['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        response = Flask.make_response(app, create_user.create_new_user(request))
        return response
    else:
        response = Flask.make_response(app, user_info.get_user_connection_details(request))
        return response


@app.route('/user/connection-details', methods=['GET', 'PUT'])
def connection_details():
    if request.method == 'PUT':
        return Flask.make_response(app, create_user.update_ip(request))
    else:
        response = Flask.make_response(app, user_info.get_user_connection_details(request))
        return response


@app.route('/user/leaderboard-details', methods=['GET', 'PUT'])
def leaderboard_details():
    if request.method == 'PUT':
        return Flask.make_response(app, create_user.update_leaderboard_stats(request))
    else:
        return Flask.make_response(app, user_info.get_leaderboard_details(request))


if __name__ == '__main__':
    app.run(host='10.0.0.119', port=5000, debug=True, ssl_context='adhoc')

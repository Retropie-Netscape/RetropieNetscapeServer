from flask import (
    Flask,
    render_template,
    request
)
from user_endpoints import create_user
from user_endpoints import user_info as getUserData
from database_connection import connection

# Create the application instance
app = Flask(__name__)

def initialize_server():
    conn = 
# Create a URL route in our application for "/username"
@app.route('/user', methods=['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        return create_user.create_new_user()
    else:
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=True)
    initialize_server()
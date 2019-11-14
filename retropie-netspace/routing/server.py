from flask import (
    Flask,
    render_template,
    request
)
import user_endpoints

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/username"
@app.route('/user', methods=['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        
    else:
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=True)
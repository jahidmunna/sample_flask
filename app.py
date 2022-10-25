from flask import Flask, jsonify, redirect

from api import api
from authentication import auth

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api/v1')


@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

@app.route('/home')
def home():
    return '''
        Hello, There!   This is a home button"
        '''
        
@app.route('/<user_input>', methods=['GET'])
@auth.login_required
def api_call(user_input):
    response = {
        'user_name': auth.username(),
        'input': user_input
    }
    return jsonify(response)


@app.route('/logout')
def logout_page():
    return '''
        <button onclick="myFunction()">Logout</button>
        <script>
        function myFunction(){
            alert("You Are Logged Out!")
            var loc = window.location;
            var url = "http://random_user:random_password@"+loc.hostname + ":"+  loc.port + '/';
            window.location.replace(url);
        };
        </script>
        '''

if __name__ == '__main__':
    app.run(debug=True)

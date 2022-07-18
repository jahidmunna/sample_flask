from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "demo": "123",
    "admin": "admin"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


@app.route('/<user_input>', methods=['GET'])
@auth.login_required
def api_call(user_input):
    response = {
        'user_name': auth.username(),
        'input': user_input
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
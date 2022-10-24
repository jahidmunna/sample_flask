from flask import Flask, jsonify, redirect

from api import api
from authentication import auth

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api/v1')


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

@app.route('/logged_out')
def Logout():
     return redirect("http://random_user:random_password@127.0.0.1:5000/logout")

@app.route('/logout')
def logout_page():
    return '''
        Logged Out! <br>Click <a href='/'> HERE</a> to go to the home page 
    '''

if __name__ == '__main__':
    app.run(debug=True)

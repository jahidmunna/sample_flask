from flask_httpauth import HTTPBasicAuth

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

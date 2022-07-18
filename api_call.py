import requests

username = 'demo'
password = '123'
auth = (username, password)

user_input = "sample_input"

response = requests.get(
    'http://127.0.0.1:5000/'+user_input,
    auth=auth
)

print(response.text)
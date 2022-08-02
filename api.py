from flask import Blueprint

from authentication import auth

api = Blueprint('api', __name__)


@api.route('/')
@auth.login_required
def sample_api():
    return {
        'response': 'sample_api'
    }


@api.route('/<input>')
@auth.login_required
def sample_api_input(input):
    return {
        'input': str(input)
    }

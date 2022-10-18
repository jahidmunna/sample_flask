from flask import Flask, jsonify
from book import book
from cache import cache

app = Flask(__name__)
cache.init_app(app)
app.register_blueprint(book, url_prefix='/book')

@app.route('/')
def home():
    return '''
        click <a href='/book'> HERE </a>to see the books
    '''
if __name__ == '__main__':
    app.run(debug=True)
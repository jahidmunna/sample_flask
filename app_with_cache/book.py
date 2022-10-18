from flask import Blueprint
from cache import cache
book = Blueprint('book', __name__)


@book.route('/')
@cache.cached(timeout=50)
def read_book():
    with open ('book_list.txt', 'r') as f:
        lines = f.readlines()  
    result = ""
    for line in lines:
        line = "<li>"+ line.replace("\n", "") + "</li>"
        result +=line
    return result

@book.route('create/<book_name>')
def sample_api_input(book_name:str):
    book_name = "\n"+book_name.strip()
    with open ('book_list.txt', 'a') as f:
        f.write(book_name)
    
    # Remove Caching To Reflact New Entry
    cache.clear()
    
    return '''
            <h2>Book {} is created! <br>
            Click <a href = '/book'> Here</> to see it 
        '''.format(book_name)
        
        
        
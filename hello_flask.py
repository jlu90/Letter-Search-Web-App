from flask import Flask
#flask = module; Flask = class

from letter_search import search_for_letters

app = Flask(__name__)

@app.route('/')

def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')

def search():
    return str(search_for_letters('this is dumb','booo'))

app.run()


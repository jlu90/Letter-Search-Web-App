# Letter Search Web App
# Created as a project from Head First Python, 2nd Edition in January 2020

from flask import Flask, render_template, request, escape, session
from letter_search import search_for_letters

from DBcm import UseDatabase
from checker import check_logged_in


app = Flask(__name__)

app.config['dbconfig'] = {'host':'127.0.0.1', 'user':'vsearch','password':'vsearchpasswd','database':'vsearchlogDB'}

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in', None)
    return 'You are now logged out.'

def log_request(req: 'flask_request', res: str) -> None:
    '''Log details of the webrequest and results into a MySQL database'''
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = '''insert into log (phrase,letters,ip,browser_string,results) values (%s, %s, %s, %s, %s)'''
        cursor.execute(_SQL, (req.form['phrase'],req.form['letters'],req.remote_addr,req.user_agent.browser,res,))
    
@app.route('/search4', methods = ['POST'])
def search():
   phrase = request.form['phrase']
   letters = request.form['letters']
   title = "Here are your results: "
   results = str(search_for_letters(phrase, letters))
   log_request(request, results)
   return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to Search For Letters on the web!')

@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = '''SELECT phrase, letters, ip, browser_string, results FROM log'''
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_Agent', 'Results')
    return render_template('viewlog.html',the_title='View Log', the_row_titles=titles, the_data=contents)

app.secret_key = 'Password1234'

if __name__ == "__main__":
    app.run(debug = True)


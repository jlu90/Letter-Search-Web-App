from flask import Flask, session
# Importing session gives the WebApp the ability to remember state
# Any data stored in a session exists for the entire time that the webapp runs
app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'
# Encrypts the cookie

@app.route('/setuser/<user>')
def setuser(user:str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

if __name__ == "__main__":
    app.run(debug=True)     
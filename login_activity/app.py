from flask import Flask
from flask import Flask, alert, session, show, request
app = Flask(__name__)

@app.route ('/')
def home():
    return show('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'username':
        session['logged_in'] = True
    else:
        alert['Wrong password!!!']
        return home()
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=4000)
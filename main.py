from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
counter = 0
@app.get('/game')
def login_get():
    return render_template('main.html', counter = counter)

@app.post('/game')
def login_post():
    global counter
    counter += 1
    return render_template('main.html',counter = counter)
import string
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for, request
import random

app = Flask(__name__)
current_lobies = {}


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/game?room=<roomId>")
def game(roomId):
    current_lobies[roomId]
    GameRoom = current_lobies[roomId]
    return f"Post {GameRoom}"


@app.get("/lobby")
def signup_form():
    return render_template("room_form.html")


@app.post("/lobby")
def post_form():
    randomID = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    players = []
    players.append(request.form["name"])
    current_lobies[randomID] = players
    return redirect(url_for("game", roomId=randomID))

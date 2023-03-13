

from flask import Flask, render_template, request, url_for, flash, redirect
from random import randint
from datetime import datetime

app = Flask(__name__)


weapons = [[0,"nůžky", "papír"], [1,"kámen", "nůžky"], [2,"papír", "kámen"]]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/collection/", methods = ("GET", "POST"))
def collection():
    if request.method == "POST":

        id = request.form["id"]
        return redirect(url_for("fight", id = id))
    return render_template("collection.html", weapons = weapons)

@app.route("/fight/<id>")
def fight(id):
    
    count = len(weapons)
    player = weapons[int(id)]
    bot = weapons[randint(0, count-1)]
    
    return render_template("fight.html", bot = bot, player = player)


if __name__ == "__main__":
    app.run(debug=True)
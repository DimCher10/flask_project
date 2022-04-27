from flask import Flask, render_template
from random import randint
from datetime import datetime

app = Flask(__name__)

def index():
   return render_template("index.html")

@app.route("/about")
def  about():
    return render_template("about.html")

@app.route("/random")
def random():
    number  =  randint(1, 6)
    with open("random.txt", "w") as f:
        f.write(f"... {number}")
    return render_template("random.html", result=number)
    # Вы бросили кубик, выпало число 5

app.run()
from flask import render_template
from taskmanager import app, 



@app.route("/")
def home():
    return render_template("base.html")

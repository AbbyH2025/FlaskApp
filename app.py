from flask import Flask
from flask import render_template
app = Flask(__name__)

#index route for web app
@app.route("/")
def index():
    return ("no work")

@app.route("/hello/")
@app.route("/route/<name_data>/")
def hello_there(name_data = None):
    return render_template("hello_there.html", name=name_data)
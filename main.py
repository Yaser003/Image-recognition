from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template("home.html")

@app.route("/test")
def render_test():
    return render_template("test.html")

@app.route("/mvm")
def render_mvm():
    return render_template("mvm.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0")
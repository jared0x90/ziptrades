#!/usr/bin/env pypy
from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/post")
def post_listing():
    return render_template("post.html")

@app.route("/about")
def route():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80)

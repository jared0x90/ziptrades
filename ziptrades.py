#!/usr/bin/env pypy
#
# Copyright (c) 2013 Jared De Blander
# jared0x90@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# -----------------------------------------------------------------------------
#
# Installation dependencies
#
# pip install flask

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/post")
def post_listing():
    return render_template("post.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)

@app.route('/zip/<int:zipcode>')
def zip(zipcode):
    return render_template("zip.html", zipcode=zipcode)

@app.route('/search_zip_base', methods=['POST'])
def search_zip_base():
    return redirect(url_for('zip', zipcode=request.form['zip']))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80)

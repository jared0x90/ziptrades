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

##############################################################################
# imports
##############################################################################

# flask imports
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

# my imports
import validators
import os
import sys

##############################################################################
# environment variables
##############################################################################

# Check for environment variables
def check_environment_exists(variable_name):
    if variable_name in os.environ:
        return True
    else:
        print("Missing environment variable: " + variable_name)
        sys.exit(1)

# check_environment_exists("ZT_DB_PATH")
# check_environment_exists("ZT_SECRET_KEY")


##############################################################################
# initiate flask
##############################################################################
app = Flask(__name__, static_folder='static', static_url_path='/static')

##############################################################################
# Create routes
##############################################################################
# General routes
##############################################################################
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/post")
def post_listing():
    return render_template("post.html")

@app.route("/new")
def newest_listings():
    return render_template("new.html")

@app.route("/hot")
def hot():
    return render_template("hot.html")

@app.route("/user_agreement")
def user_agreement():
    return render_template("user_agreement.html")

@app.route("/privacy_policy")
def privacy_policy():
    return render_template("privacy_policy.html")

@app.route("/etiquette")
def etiquette():
    return render_template("etiquette.html")

@app.route("/random")
def random_listing():
    return render_template("random.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)

@app.route('/zip/<zipcode>')
def zip(zipcode):
    if validators.valid_zipcode(zipcode):
        return render_template("zip.html", zipcode=zipcode)
    else:
        return redirect(url_for('error_invalid_zip'))

@app.route('/error_invalid_zip')
def error_invalid_zip():
    return render_template('error_invalid_zip.html')
##############################################################################
# Post routes
##############################################################################
@app.route('/search_zip_base', methods=['POST'])
def search_zip_base():
    if validators.valid_zipcode(request.form['zip']):
        return redirect(url_for('zip', zipcode=request.form['zip']))
    else:
        return redirect(url_for('error_invalid_zip'))

@app.route('/create_post_listing', methods=['POST'])
def create_post_listing():
    if validators.valid_zipcode(request.form['zip']):
        return redirect(url_for('zip', zipcode=request.form['zip']))
    else:
        return redirect(url_for('error_invalid_zip'))


##############################################################################
# Run application
##############################################################################
if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 80)
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hi():
    return render_template("index.html")
@app.route("/1006")
def exercise():
    return render_template("1006.html")
@app.route("/frank")
def frank():
    return render_template("frank.html")
@app.route("/awards")
def awards():
    return render_template("awards.html")
#start the server
if __name__ == "__main__":
    app.run()
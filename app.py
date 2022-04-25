import os

from flask import Flask, flash, redirect, render_template, request, session
# from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3

from website.helpers import error

# Configure application
app = Flask(__name__)

# Require templates to be auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure system to use filesystem (rather than cookies)
# app.config["SESSION_PERMANENT"] = False
# # app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

conn = sqlite3.connect("userdata.db")
c = conn.cursor()

# create table to store user data
c.execute(
    '''CREATE TABLE IF NOT EXISTS users
    (name text NOT NULL, email text, password_hash)''')
conn.commit()
conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            flash("Must provide username", category = 'error')

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password", category='error')

        # Query database for username
        rows = c.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
           flash("Invalid username and/or password", category='error')

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("login.html")
import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Require templates to be auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure system to use filesystem (rather than cookies)
# app.config["SESSION_PERMANENT"] = False
# # app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

@app.route("/")
def home():
    return render_template("simple.html")
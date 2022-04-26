from flask import Blueprint, render_template, request, flash, redirect, url_for


auth= Blueprint('auth', __name__)

@auth.route("/")
def home():
    return render_template("index.html")


@auth.route("/register")
def register():
    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    #session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            flash("Must provide username", category = 'error')

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password", category='error')

        # Query database for username
       # rows = c.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
           flash("Invalid username and/or password", category='error')

        # Remember which user has logged in
      #  session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("login.html")
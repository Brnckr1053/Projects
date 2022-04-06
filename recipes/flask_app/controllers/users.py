from flask_app import app
from flask import render_template,flash,redirect,request,session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=["POST"])
def register():
    if User.validate_user(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data = {
            "first_name":request.form["first_name"],
            "last_name":request.form["last_name"],
            "email":request.form["email"],
            "password":pw_hash
        }
        user_in_db = User.get_by_email(data)

        if user_in_db:
            flash("User already exists")
            return redirect("/")

        user_id = User.insert_user(data)
        session["user_id"] = user_id
        flash("User created!")
        return redirect("/")
    else:
        return redirect("/")

@app.route("/login",methods=["POST"])
def login():
    if User.validate_login(request.form):
        data = {"email":request.form["email"]}
        user_in_db = User.get_by_email(data)
        
        if not user_in_db:
            flash("Invalid Email/Password")
            return redirect("/")
        if not bcrypt.check_password_hash(user_in_db.password,request.form["password"]):
            flash("Invalid Email/Password")
            return redirect("/")
        
        session["user_id"] = user_in_db.id
        session["first_name"] = user_in_db.first_name
        session["email"] = user_in_db.email
        return redirect("/recipes")
    else:
        return redirect("/")

@app.route("/edit")
def edit():
    if "user_id" not in session:
        flash("Must be logged in to view page")
        return redirect("/")
        
    data = {
        "email":session["email"]
    }
    user = User.get_by_email(data)
    return render_template("edituser.html",user=user)

@app.route("/edituser",methods=["POST"])
def edit_user():
    if User.validate_update(request.form):
        data = {
            "first_name":request.form["first_name"],
            "last_name":request.form["last_name"],
            "email":request.form["email"],
            "id":session["user_id"]
        }
        User.update_user(data)
        session["first_name"]=request.form["first_name"]
        session["email"]=request.form["email"]
        return redirect("/recipes")
    else:
        return redirect("/edit")

@app.route("/recipes")
def secret_page():
    if "user_id" not in session:
        flash("Must be logged in!")
        return redirect("/")
    else:
        return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged Out!")
    return redirect("/")
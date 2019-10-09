from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, CreateUserForm
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form, error = "No such username")

    password = form.password.data
    password_hash = user.password

    if bcrypt.check_password_hash(password_hash, password):    
        login_user(user)
        return redirect(url_for("index"))

    return render_template("auth/loginform.html", form=form, error= "Wrong password")    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))      

@app.route("/auth/create_user", methods = ["GET", "POST"])
def auth_create():
    if request.method == "GET":
        return render_template("auth/newuserform.html", form = CreateUserForm())

    form = CreateUserForm(request.form)
    
    if not form.validate():
        return render_template("auth/newuserform.html", form=form)

    username = form.username.data
    email = form.email.data
    password = form.password.data

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Varmistetaan, että username ja email ovat uniikkeja
    username_exists = User.query.filter_by(username=username).first()
    email_exists = User.query.filter_by(email=email).first()

    if username_exists and not email_exists:
        return render_template("auth/newuserform.html", form=form, error="Username {} exists already".format(username))
    if email_exists and not username_exists:
        return render_template("auth/newuserform.html", form=form, error="Email {} exists already".format(email)) 
    if username_exists and email_exists:
        return render_template("auth/newuserform.html", form=form, error="Username {0} and email {1} exist already".format(username, email))       

    # Luodaan uusi käyttäjä ja lisätään tietokantaann
    new_user = User(form.name.data, form.email.data, form.username.data, password_hash, form.role.data)
    db.session().add(new_user)
    db.session().commit()

    return redirect(url_for("auth_login"))





    


        




    
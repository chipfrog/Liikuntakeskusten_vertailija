from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.clubs.models import Club
from application.reviews.models import Review
from application.reviews.forms import ReviewForm
from application.clubs.forms import CreateClubForm

@app.route("/clubs", methods=["GET"])
def clubs_index():
    return render_template("clubs/list.html", clubs_average_grade = Club.clubs_by_avg_grade())

@app.route("/clubs/new", methods=["POST", "GET"])
@login_required(role="owner")
def clubs_create():
    if request.method == "GET":
        return render_template("clubs/new.html", form = CreateClubForm())

    form = CreateClubForm(request.form)    

    if not form.validate():
        return render_template("clubs/new.html", form=form)

    c = Club(form.name.data, form.city.data, form.address.data, form.email.data, form.tel.data, form.price.data)
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("clubs_index"))

@app.route("/clubs/myclub", methods=["GET"])
@login_required(role="owner")
def clubs_edit():
    club = Club.query.filter_by(account_id = current_user.id).first()
    form = CreateClubForm(request.form)
    
    form.name.data = club.name
    form.city.data = club.city
    form.address.data = club.address
    form.email.data = club.email
    form.price.data = club.price

    return render_template("clubs/update.html", form=form)
    



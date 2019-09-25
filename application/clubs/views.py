from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.clubs.models import Club
from application.reviews.models import Review
from application.reviews.forms import ReviewForm
from application.clubs.forms import CreateClubForm

@app.route("/clubs", methods=["GET"])
def clubs_index():
    return render_template("clubs/list.html", clubs_average_grade = Club.clubs_by_avg_grade())

@app.route("/clubs/new", methods=["POST", "GET"])
@login_required
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


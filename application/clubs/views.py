from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.clubs.models import Club
from application.reviews.models import Review
from application.reviews.forms import ReviewForm
from application.clubs.forms import CreateClubForm

@app.route("/clubs", methods=["GET"])
def clubs_index():
    return render_template("clubs/list.html", clubs = Club.query.all())
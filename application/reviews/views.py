from flask import render_template, request, redirect, url_for
from flask_login import current_user

import math
from application.pagination import ITEMS_PER_PAGE, offsets

from application import app, db, login_required
from application.reviews.models import Review
from application.clubs.models import Club
from application.auth.models import User
from application.reviews.forms import ReviewForm

@app.route("/reviews/<offset>/", methods=["GET"])
@login_required(role="user")
def reviews_index(offset):
    # Lasketaan montako sivua arvosteluja varten tarvitaan
    pages = math.ceil(Review.query.filter_by(account_id = current_user.id).count()/ITEMS_PER_PAGE)
    
    # Yhtä sivua varten haettavat arvostelut
    reviews = Review.get_users_reviews(current_user.id, ITEMS_PER_PAGE, offset)
    offset_array = offsets(pages)

    return render_template("reviews/list.html", reviews=reviews, pages=pages, offset_array=offset_array)
    
@app.route("/reviews/new/<club_id>/", methods=["GET"])
@login_required(role="user")
def reviews_form(club_id):
    users_reviews = User.clubs_reviewed(current_user.id)
    
    # Varmistetaan ettei käyttäjä ole jo arvosttelut seuraa
    if int(club_id) in users_reviews:
        message="You have already reviewed this club!"
        
        return render_template("error.html", message = message)

    return render_template("reviews/new.html", form = ReviewForm(), club_id=club_id)

@app.route("/reviews/edit/<review_id>/", methods=["GET"])
@login_required(role="user")
def reviews_edit(review_id):
    review = Review.query.get(review_id)
    
    # Varmistetaan, että kirjautunut käyttäjä on myös arvostelun kirjoittaja
    if not review.account_id == current_user.id:
        message = "You can't edit someone else's review!"
        
        return render_template("error.html", message=message)
    
    form = ReviewForm(request.form)
    form.grade.data = review.grade
    form.review.data = review.review

    return render_template("reviews/update.html", form=form, review_id=review_id)
    
@app.route("/reviews/update/<review_id>/", methods=["POST"])
@login_required(role="user")   
def reviews_update(review_id):
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/update.html", form=form, review_id=review_id)

    r = Review.query.get(review_id)
    
    if not r.account_id == current_user.id:
        message = "You can't edit someone else's review!"
        return render_template("error.html", message = message)
    
    r.grade = form.grade.data
    r.review = form.review.data

    db.session().commit()   

    return redirect(url_for("reviews_index", offset=0)) 

@app.route("/reviews/create/<club_id>/", methods=["POST"])
@login_required(role="user")
def reviews_create(club_id):
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/new.html", form=form, club_id=club_id)

    r = Review(form.grade.data, form.review.data)
    r.account_id = current_user.id
    r.club_id = club_id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("clubs_index"))

@app.route("/reviews/delete/<review_id>/", methods=["POST"])
@login_required(role="user")
def reviews_delete(review_id):
    r = Review.query.get(review_id)
    if not r.account_id == current_user.id:
        message = "You can't delete someone else's review!"
        return render_template("error.html", message=message)

    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("reviews_index", offset=0))    

from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.reviews.models import Review
from application.clubs.models import Club
from application.reviews.forms import ReviewForm

@app.route("/reviews", methods=["GET"])
@login_required(role="user")
def reviews_index():
    return render_template("reviews/list.html", reviews = Review.get_users_reviews(current_user.id))
    
@app.route("/reviews/new/<club_id>/", methods=["GET"])
@login_required(role="user")
def reviews_form(club_id):
    return render_template("reviews/new.html", form = ReviewForm(), club_id=club_id)

@app.route("/reviews/<review_id>/", methods=["GET"])
@login_required(role="user")
def reviews_edit(review_id):
    review = Review.query.get(review_id)
    if not review.account_id == current_user.id:
        return render_template("error.html")
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
        return render_template("error.html")
    
    r.grade = form.grade.data
    r.review = form.review.data

    db.session().commit()   

    return redirect(url_for("reviews_index")) 

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
        return render_template("error.html")

    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("reviews_index"))    

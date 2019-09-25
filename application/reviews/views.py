from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.reviews.models import Review
from application.reviews.forms import ReviewForm

@app.route("/reviews", methods=["GET"])
@login_required
def reviews_index():
    return render_template("reviews/list.html", reviews = Review.query.filter_by(account_id = current_user.id))

@app.route("/reviews/new/<club_id>/", methods=["GET"])
@login_required
def reviews_form(club_id):
    return render_template("reviews/new.html", form = ReviewForm(), club_id=club_id)

@app.route("/reviews/<review_id>/", methods=["GET"])
@login_required
def reviews_edit(review_id):
    form = ReviewForm(request.form)
    review = Review.query.get(review_id)
    form.grade.data = review.grade
    form.review.data = review.review

    return render_template("reviews/update.html", form=form, review_id=review_id)
    
@app.route("/reviews/update/<review_id>/", methods=["POST"])
@login_required   
def reviews_update(review_id):
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/update.html", form=form, review_id=review_id)

    r = Review.query.get(review_id)
    r.grade = form.grade.data
    r.review = form.review.data

    db.session().commit()   

    return redirect(url_for("reviews_index")) 

@app.route("/reviews/create/<club_id>/", methods=["POST"])
@login_required
def reviews_create(club_id):
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/new.html", form=form)

    r = Review(form.grade.data, form.review.data)
    r.account_id = current_user.id
    r.club_id = club_id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reviews_index"))

@app.route("/reviews/delete/<review_id>/", methods=["POST"])
@login_required
def reviews_delete(review_id):
    r = Review.query.get(review_id)
    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("reviews_index"))    

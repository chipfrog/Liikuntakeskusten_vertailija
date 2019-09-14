from application import app, db
from flask import render_template, request, redirect, url_for
from application.reviews.models import Review
from application.reviews.forms import ReviewForm

@app.route("/reviews", methods=["GET"])
def reviews_index():
    return render_template("reviews/list.html", reviews = Review.query.all())

@app.route("/reviews/new/")
def reviews_form():
    return render_template("reviews/new.html", form = ReviewForm())

@app.route("/reviews/<review_id>/", methods=["GET"])
def reviews_edit(review_id):
    form = ReviewForm(request.form)
    review = Review.query.get(review_id)
    form.grade.data = review.grade
    form.review.data = review.review

    return render_template("reviews/update.html", form=form, review_id=review_id)
    
    # return render_template("reviews/update.html", review = Review.query.get(review_id))
    # r = Review.query.get(review_id)
    # r.review = request.form.get("modifiedReview")
    # db.session().commit()
    # return redirect(url_for("reviews_index"))

@app.route("/reviews/update/<review_id>/", methods=["POST"])   
def reviews_update(review_id):
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/update.html", form=form, review_id=review_id)

    r = Review.query.get(review_id)
    r.grade = form.grade.data
    r.review = form.review.data

    db.session().commit()   

    return redirect(url_for("reviews_index")) 

@app.route("/reviews/", methods=["POST"])
def reviews_create():
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/new.html", form=form)

    r = Review(form.grade.data, form.review.data)

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reviews_index"))
from application import app, db
from flask import render_template, request, redirect, url_for
from application.reviews.models import Review

@app.route("/reviews", methods=["GET"])
def reviews_index():
    return render_template("reviews/list.html", reviews = Review.query.all())

@app.route("/reviews/new/")
def reviews_form():
    return render_template("reviews/new.html")

@app.route("/reviews/<review_id>/", methods=["POST"])
def reviews_update(review_id):
    r = Review.query.get(review_id)
    r.review = request.form.get("modifiedReview")

    db.session().commit()

    return redirect(url_for("reviews_index"))

@app.route("/reviews/", methods=["POST"])
def reviews_create():
    grade = request.form.get("grade")
    review = request.form.get("review")
    
    r = Review(grade, review)

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reviews_index"))
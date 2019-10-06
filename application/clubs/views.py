from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.clubs.models import Club
from application.sports.models import Sport
from application.reviews.models import Review
from application.reviews.forms import ReviewForm
from application.clubs.forms import CreateClubForm, SearchClubForm

@app.route("/clubs", methods=["GET"])
def clubs_index():
    return render_template("clubs/list.html", clubs_average_grade = Club.clubs_by_avg_grade())

@app.route("/clubs/search/", methods=["GET", "POST"])
def clubs_search():
    if request.method == "GET":
        return render_template("clubs/search.html", form = SearchClubForm()) 

    form = SearchClubForm(request.form)

    if not form.validate():
        return render_template("clubs/search.html", form = form)
               
    city = form.city.data
    score = form.score_min.data
    sport = form.sport.data

    clubs = Club.filter_clubs(city, score, sport)
    
    return render_template("clubs/list.html", clubs_average_grade = clubs)           

@app.route("/clubs/new", methods=["POST", "GET"])
@login_required(role="owner")
def clubs_create():
    if request.method == "GET":
        return render_template("clubs/new.html", form = CreateClubForm())

    form = CreateClubForm(request.form)
     
    if not form.validate():
        return render_template("clubs/new.html", form=form)

    # Tarkistetaan ettei samannimistä seuraa ole tietokannassa.
    club_name = Club.query.filter_by(name=form.name.data).first()
    if club_name:
        return render_template("clubs/new.html", form=form, error="{} already exists.".format(form.name.data))       
    # Luodaan uusi seura ja lisätään tietokantaan
    c = Club(form.name.data, form.city.data, form.address.data, form.email.data, form.tel.data, form.price.data)
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("clubs_my_clubs"))

@app.route("/clubs/myclubs", methods=["GET"])
@login_required(role="owner")
def clubs_my_clubs():
    clubs = Club.my_clubs_by_avg_grade(current_user.id)
    return render_template("clubs/list_my_clubs.html", clubs=clubs)

@app.route("/clubs/edit/<club_id>/", methods=["GET"])
@login_required(role="owner")
def clubs_edit(club_id):
    club = Club.query.get(club_id)
    if not club.account_id == current_user.id:
        return render_template("error.html")
    form = CreateClubForm(request.form)
    
    form.name.data = club.name
    form.city.data = club.city
    form.address.data = club.address
    form.email.data = club.email
    form.tel.data = club.tel
    form.price.data = club.price

    return render_template("clubs/update.html", form=form, club_id=club_id)

@app.route("/clubs/update/<club_id>/", methods=["POST"])
@login_required(role="owner")
def clubs_update(club_id):
    form = CreateClubForm(request.form)

    if not form.validate():
        return render_template("clubs/update.html", form=form, club_id=club_id)

    club = Club.query.get(club_id)
    
    if not club.account_id == current_user.id:
        return render_template("error.html")
    
    club.name = form.name.data
    club.city = form.city.data
    club.address = form.address.data
    club.email = form.email.data
    club.tel = form.tel.data
    club.price = form.price.data

    db.session().commit()

    return redirect(url_for("clubs_my_clubs")) 

@app.route("/clubs/delete/<club_id>/", methods=["POST"])
@login_required(role="owner")
def clubs_delete(club_id):
    club = Club.query.get(club_id)
    
    if not club.account_id == current_user.id:
        return render_template("error.html")

    reviews = Review.query.filter_by(club_id = club_id)

    # Poistaa seuraan liittyvät arvostelut
    for review in reviews:
        db.session().delete(review)    

    # Poistaa seuran 
    db.session().delete(club)
    db.session().commit()

    return redirect(url_for("clubs_my_clubs"))        

@app.route("/clubs/reviews/<club_id>/", methods=["GET"])
def clubs_reviews(club_id):
    return render_template("clubs/club_reviews.html", reviews = Review.get_clubs_reviews(club_id))

@app.route("/clubs/info/<club_id>/", methods=["GET"])
def clubs_info(club_id):
    club = Club.get_club_info(club_id).first()
    sports = Sport.get_sports(club_id)
    return render_template("clubs/info.html", club = club, sports = sports)




    




from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.clubs.models import Club
from application.sports.models import Sport
from application.reviews.models import Review
from application.auth.models import User
from application.reviews.forms import ReviewForm
from application.clubs.forms import CreateClubForm, SearchClubForm

# Tietokannan kaikkien urheiluseurojen järjestäminen eri kriteerein
@app.route("/clubs", methods=["GET"])
def clubs_index():
    if current_user.is_authenticated:
        users_reviews = User.clubs_reviewed(current_user.id)
        return render_template("clubs/list.html", clubs = Club.clubs_by_avg_grade(), users_reviews = users_reviews)

    return render_template("clubs/list.html", clubs = Club.clubs_by_avg_grade())

@app.route("/clubs/byname", methods=["GET"])
def clubs_index_by_name():
    if current_user.is_authenticated:
        users_reviews = User.clubs_reviewed(current_user.id)
        return render_template("clubs/list.html", clubs = Club.clubs_by_name(), users_reviews = users_reviews)

    return render_template("clubs/list.html", clubs = Club.clubs_by_name())

@app.route("/clubs/bycity", methods=["GET"])
def clubs_index_by_city():
    if current_user.is_authenticated:
        users_reviews = User.clubs_reviewed(current_user.id)
        return render_template("clubs/list.html", clubs = Club.clubs_by_city(), users_reviews = users_reviews)
    return render_template("clubs/list.html", clubs = Club.clubs_by_city())

@app.route("/clubs/bypricemin", methods=["GET"])
def clubs_index_by_price_min():
    if current_user.is_authenticated:
        users_reviews = User.clubs_reviewed(current_user.id)
        return render_template("clubs/list.html", clubs = Club.clubs_by_price_min(), users_reviews = users_reviews)
    return render_template("clubs/list.html", clubs = Club.clubs_by_price_min())

@app.route("/clubs/bypricemax", methods=["GET"])
def clubs_index_by_price_max():
    if current_user.is_authenticated:
        users_reviews = User.clubs_reviewed(current_user.id)
        return render_template("clubs/list.html", clubs = Club.clubs_by_price_max(), users_reviews = users_reviews)
    return render_template("clubs/list.html", clubs = Club.clubs_by_price_max())

# Käyttäjän antamien kriteerien mukaisten urheiluseurojen hakeminen
@app.route("/clubs/search/", methods=["GET", "POST"])
def clubs_search():
    if request.method == "GET":
        return render_template("clubs/search.html", form = SearchClubForm()) 

    form = SearchClubForm(request.form)

    if not form.validate():
        return render_template("clubs/search.html", form = form)
               
    # Tallennetaan käyttäjän syöttämät kriteerit muuttujiin           
    city = form.city.data
    score = form.score_min.data
    price_min = form.price_min.data
    price_max = form.price_max.data
    sport = form.sport.data

    # Etsitään seuroja annetuilla kriteereillä
    clubs = Club.filter_clubs(city, score, price_min, price_max, sport)

    if len(clubs) == 0:
        message = "No results..."
        return render_template("clubs/search.html", form=form, message=message)
    
    # Otetaan seurojen järjestäminen pois päältä, sillä jokainen järjestelynappi (name, city jne.)tekee uuden 
    # SQL-kyselyn. Järjestely ei siis toimi kertaalleen filteröityyn SQL-kyselyyn (clubs).

    no_filtering = 0    
    
    return render_template("clubs/list.html", clubs = clubs, no_filtering = no_filtering)

# Urheiluseuran luominen
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

# Käyttäjän hallinnoimien seurojen listaaminen
@app.route("/clubs/myclubs", methods=["GET"])
@login_required(role="owner")
def clubs_my_clubs():
    clubs = Club.my_clubs_by_avg_grade(current_user.id)
    return render_template("clubs/list_my_clubs.html", clubs=clubs)

@app.route("/clubs/edit/<club_id>/", methods=["GET"])
@login_required(role="owner")
def clubs_edit(club_id):
    club = Club.query.get(club_id)
    
    # Varmistetaan käyttöoikeus
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

# Seuran tietojen päivittäminen
@app.route("/clubs/update/<club_id>/", methods=["POST"])
@login_required(role="owner")
def clubs_update(club_id):
    form = CreateClubForm(request.form)

    if not form.validate():
        return render_template("clubs/update.html", form=form, club_id=club_id)

    club = Club.query.get(club_id)
    
    # Varmistetaan käyttöoikeus
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
     
# Seuran poistaminen tietokannasta
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

# Seuran saamien arvostelujen listaaminen
@app.route("/clubs/reviews/<club_id>/", methods=["GET"])
def clubs_reviews(club_id):
    return render_template("clubs/club_reviews.html", reviews = Review.get_clubs_reviews(club_id))
# Seuran koostesivu
@app.route("/clubs/info/<club_id>/", methods=["GET"])
def clubs_info(club_id):
    club = Club.get_club_info(club_id).first()
    sports = Sport.get_sports(club_id)
    reviews = Review.get_clubs_reviews(club_id)
    
    return render_template("clubs/info.html", club = club, sports = sports, reviews = reviews)




    




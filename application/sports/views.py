from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.clubs.models import Club, sports
from application.sports.models import Sport
from application.sports.forms import SportForm

from sqlalchemy.sql import text

@app.route("/clubs/addsport/<club_id>/", methods=["GET", "POST"])
@login_required(role="owner")
def add_sport(club_id):
    if request.method == "GET":
        return render_template("sports/new_sport.html", form=SportForm(), club_id=club_id, sports=Sport.get_sports(club_id))

    form = SportForm(request.form)

    if not form.validate():
        return render_template("sports/new_sport.html", form=form, club_id=club_id, sports=Sport.get_sports(club_id))

    c = Club.query.get(club_id)
    s = Sport(form.name.data.lower())

    if not c.account_id == current_user.id:
        return render_template("error.html")
    
    # Tarkistetaan löytyykö lajia sport-taulusta ollenkaann
    sportExists = Sport.query.filter(Sport.name == s.name).first()
    
    if sportExists is None:

        # Lisätään laji sport-tauluun ja liitostauluun
        c.sports.append(s)
        db.session().add(c)
        db.session().commit()

        message = s.name + " added successfully!"

        return render_template("sports/new_sport.html", form=form, club_id=club_id, message=message, sports=Sport.get_sports(club_id))

    # Tarkistetaan löytyyko liitostaulusta jo yhteys lajin ja seuran välillä
    clubs_sports = Club.club_has_sport(club_id)
    if s.name in clubs_sports:
        message = s.name + " has already been added!"
        return render_template("sports/new_sport.html", form=SportForm(), club_id=club_id, message=message, sports=Sport.get_sports(club_id))

    # Lisätään uusi yhteys lajin ja seuran välille sports-liitostauluun    
    c.sports.append(sportExists)
    db.session().add(c)
    db.session().commit()

    message = s.name + " added successfully!"

    return render_template("sports/new_sport.html", form=SportForm(), club_id=club_id, message=message, sports=Sport.get_sports(club_id))

@app.route("/clubs/deletesport/<sport_id>/<club_id>/", methods=["POST"])
@login_required(role="owner")
def sports_delete_association(sport_id, club_id):
    club = Club.query.get(club_id)
    
    # Varmistaa, että kirjautunut käyttäjä on seuran omistaja
    if not club.account_id == current_user.id:
        return render_template("error.html") 
    
    # Poistaa sports-liitostaulusta yhteyden liikuntalajin ja seuran väliltä 
    Sport.delete_sport_association(sport_id, club_id)
    db.session().commit()
    
    return redirect(url_for("add_sport", club_id=club_id))




  


 

from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application.clubs.models import Club
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
    s = Sport(form.name.data)

    if not c.account_id == current_user.id:
        return render_template("error.html")

    sportExists = Sport.query.filter(Sport.name == s.name).first()
    
    if sportExists is None:
        c.sports.append(s)
        db.session().add(c)
        db.session().commit()

        message = s.name + " added successfully!"

        return render_template("sports/new_sport.html", form=SportForm(), club_id=club_id, message=message, sports=Sport.get_sports(club_id))
        
    c.sports.append(sportExists)
    db.session().add(c)
    db.session().commit()

    message = s.name + " added successfully!"

    return render_template("sports/new_sport.html", form=SportForm(), club_id=club_id, message=message, sports=Sport.get_sports(club_id))


  


 






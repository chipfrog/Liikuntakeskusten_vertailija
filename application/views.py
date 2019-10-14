from application import app, db
from flask import redirect, render_template, request
from application.models import Base

@app.route("/")
def index():
    info = Base.general_info()
    
    return render_template("index.html", info=info[0])

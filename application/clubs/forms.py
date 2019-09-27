from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from wtforms.fields.html5 import EmailField

class CreateClubForm(FlaskForm):
    name = StringField("Name of the sports club", [validators.input_required()])
    city = StringField("City", [validators.input_required()])
    address = StringField("Address")
    email = EmailField("Email")
    tel = StringField("Phone number")
    price = IntegerField("Price per month", [validators.input_required()])

    class Meta():
        csrf = False


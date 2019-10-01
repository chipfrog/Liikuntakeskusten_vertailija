from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from wtforms.fields.html5 import EmailField

class CreateClubForm(FlaskForm):
    name = StringField("Name of the sports club", [validators.input_required(), validators.Length(max=30)])
    city = StringField("City", [validators.input_required(), validators.Length(max=20)])
    address = StringField("Address", [validators.Length(max=30)])
    email = EmailField("Email", [validators.Length(max=30)])
    tel = StringField("Phone number", [validators.Length(max=20)])
    price = IntegerField("Price per month", [validators.input_required()])

    class Meta():
        csrf = False
        

        


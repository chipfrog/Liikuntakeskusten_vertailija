from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SportForm(FlaskForm):
    name = StringField("Sport", [validators.input_required(), validators.Length(max=30, message='Name too long')])

    class Meta():
        csrf = False
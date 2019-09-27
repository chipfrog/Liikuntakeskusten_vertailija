from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.input_required()])
    password = PasswordField("Password", [validators.input_required()])

    class Meta:
        csrf = False

class CreateUserForm(FlaskForm):
    name = StringField("Name", [validators.input_required()])
    email = EmailField("Email", [validators.input_required()])
    username = StringField("Username", [validators.Length(min=4)])
    password = PasswordField("Password", [validators.Length(min=8)])
    role = StringField("User role", [validators.input_required()])
    
    class Meta:
        csrf = False         
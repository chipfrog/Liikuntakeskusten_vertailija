from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.input_required()])
    password = PasswordField("Password", [validators.input_required()])

    class Meta:
        csrf = False

class CreateUserForm(FlaskForm):
    name = StringField("Name", [validators.input_required(), validators.Length(max=40, message='Name too long')])
    email = EmailField("Email", [validators.input_required(), validators.Length(max=40, message='Email too long')])
    username = StringField("Username", [validators.Length(min=4, max=20)])
    password = PasswordField("Password", [validators.Length(min=4, max=20)])
    role = StringField("User role", [validators.input_required()])

    class Meta:
        csrf = False         
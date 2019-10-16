from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, validators

class ReviewForm(FlaskForm):
    grade = IntegerField("Grade", [validators.NumberRange(min=1, max=5)])
    review = TextAreaField("Review", [validators.Length(max=500)])

    class Meta:
        csrf = False

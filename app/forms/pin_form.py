from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError


class PinForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(message="Title is required")])
    description=TextAreaField('description', validators=[DataRequired(message="Description is required")])
    ingredients=TextAreaField('ingredients', validators=[DataRequired(message='Ingredients are required.')])
    time=StringField('time', validators=[DataRequired(message="Time is required")])
    image_url = StringField('image_url', validators=[DataRequired(message='Image is required.')])
    
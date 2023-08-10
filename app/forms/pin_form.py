from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError

"""
    Creates form for pin
"""
class PinForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(message="Title is required")])
    description=TextAreaField('description', validators=[DataRequired(message="Description is required")])
    ingredients=TextAreaField('ingredients', validators=[DataRequired(message='Ingredients are required.')])
    time=StringField('time', validators=[DataRequired(message="Time is required")])
    image_url = StringField('image_url', validators=[DataRequired(message='Image is required.')])
    is_saved = BooleanField('is_saved')
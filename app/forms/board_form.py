from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField
from wtforms.validators import DataRequired, Email, ValidationError

# list of kitchens for select
kitchens = [
    "American", "Mexican", "Chinese", "Japanese", "Korean", "French", "Italian", "Ukrainian", "Mediterranean", "Vegetarian",
]

"""
    Creates form for board
"""
class BoardForm(FlaskForm):
    title = SelectField('title', choices=kitchens, validators=[
                        DataRequired(message="Title is required")])
    description = TextAreaField('description', validators=[
                                DataRequired(message="Description is required")])
    board_image_url = StringField('board_image_url',validators=[
                                DataRequired(message="Description is required")] )
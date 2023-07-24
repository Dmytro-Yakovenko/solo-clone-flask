from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError

kitchens =[
    "American", "Mexican", "Chinese", "Japanese", "Korean", "French", "Italian", "Ukrainian", "Mediterranean", "Vegetarian",
]



class BoardForm(FlaskForm):
    title = SelectField('title', choices=kitchens, validators=[DataRequired(message="Title is required")])
    description=TextAreaField('description', validators=[DataRequired(message="Description is required")])
   
   
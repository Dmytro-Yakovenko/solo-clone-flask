from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError


class BoardForm(FlaskForm):
    title = SelectField('title', validators=[DataRequired(message="Title is required")])
    description=TextAreaField('description', validators=[DataRequired(message="Description is required")])
   
   
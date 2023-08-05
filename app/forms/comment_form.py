from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

"""
    Creates form for comment
"""
class CommentForm(FlaskForm):
    comment = TextAreaField('comment', validators=[DataRequired(message='Comment is required.')])
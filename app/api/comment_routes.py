from flask import Blueprint, jsonify, session, request
from flask_login import current_user, login_required
from app.models import db, Comment, Pin
from app.forms import CommentForm
from app.api.auth_routes import validation_errors_to_error_messages

comment_routes = Blueprint('comments', __name__)


@comment_routes.route('/')
@login_required

def get_all_comments():
    """
    Query for all boards of  and returns them in a list of board dictionaries
    """
    
    comments = Comment.query.all()
    comment_list=[]
    for comment in comments:
        comment_dict=comment.to_dict()
        comment_list.append(comment_dict)
    return jsonify({"comments":comment_list})







@comment_routes.route('/<int:expense_id>', methods=["POST"])
@login_required
def create_comment(pin_id):
    """
    Creates a new comment
    """
    pin = Pin.query.get(pin_id)
    # checks if pin exists
    if not pin:
        return {'errors': f"Pin {pin_id} does not exist"}, 400
   

    form = CommentForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        comment = Comment(
            comment=form.data['comment'],
            user_id=current_user.id,
            pin_id=pin_id
        )
        db.session.add(comment)
        db.session.commit()
        return comment.to_dict(), 201
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@comment_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_comment(id):
    """
    Updates a comment
    """
    comment = Comment.query.get(id)
    # checks if comment exists
    if not comment:
        return {'errors': f"Comment {id} does not exist."}, 400
    # checks if current user is a creator of the comment
    if comment.user_id != current_user.id:
        return {'errors': f"User is not the creator of comment {id}."}, 401
    form = CommentForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        form.populate_obj(comment)
        db.session.commit()
        return comment.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@comment_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_comment(id):
    """
    Deletes a comment
    """
    comment = Comment.query.get(id)
    # checks if comment exists
    if not comment:
        return {'errors': f"Comment {id} does not exist."}, 400
    # checks if current user is a creator of the comment
    if comment.user_id != current_user.id:
        return {'errors': f"User is not the creator of comment {id}."}, 401
    db.session.delete(comment)
    db.session.commit()
    return {'message': 'Delete successful.'}
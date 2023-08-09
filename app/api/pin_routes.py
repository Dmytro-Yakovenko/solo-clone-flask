from flask import Blueprint, jsonify, session, request
from flask_login import current_user, login_required
from app.models import db, Pin, Comment, PinBoard
from app.forms import CommentForm, PinForm
from app.api.auth_routes import validation_errors_to_error_messages

pin_routes = Blueprint('pins', __name__)


@pin_routes.route('/')
@login_required
def get_all_pins():
    """
    Query for all pins of  and returns them in a list of pin dictionaries
    """
    pins = Pin.query.all()
    pin_list=[]
    for pin in pins:
        pin_dict=pin.to_dict()
        pin_list.append(pin_dict)
    return jsonify({"pins":pin_list})


@pin_routes.route('/<int:id>')
@login_required
def get_pin(id):
    """
    Query for a pin  by id and returns that pin in a dictionary
    """
    pin = Pin.query.get(id)
    pin_board =PinBoard.query.filter(PinBoard.pin_id==id).first()
    # checks if pin exists
    if not pin:
        return {'errors': f"Pin {id} does not exist."}
    pin_for_response = pin.to_dict()
    pin_for_response['board_id']=pin_board.to_dict()
    return pin_for_response


@pin_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_pin(id):
    """
    Updates a pin
    """
    pin = Pin.query.get(id)
    # checks if pin exists
    if not pin:
        return {'errors': f"Pin {id} does not exist."}, 400
    # checks if current user is a creator of the pin
    if pin.user_id != current_user.id:
        return {'errors': f"User is not the creator of pin {id}."}, 401
    form = PinForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        form.populate_obj(pin)
        db.session.commit()
        return pin.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@pin_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_pin(id):
    """
    Deletes a comment
    """
    pin = Pin.query.get(id)
    # checks if pin exists
    if not pin:
        return {'errors': f"Pin {id} does not exist."}, 400
    # checks if current user is a creator of the comment
    if pin.user_id != current_user.id:
        return {'errors': f"User is not the creator of pin {id}."}, 401
    db.session.delete(pin)
    db.session.commit()
    return {'message': 'Delete successful.'}


@pin_routes.route('/<int:pin_id>/comments')
@login_required
def get_comments(pin_id):
    """
    Query for all comments of a specific pin and returns them in a list of comment dictionaries
    """
    pin = Pin.query.get(pin_id)
    # checks if pin exists
    if not pin:
        return {'errors': f"Pin {pin_id} does not exist"}, 400
    comments = Comment.query.filter(Comment.pin_id == pin_id).all()
    return {'comments': [comment.to_dict() for comment in comments]}


@pin_routes.route('/<int:pin_id>/comments/<int:comment_id>', methods=["PUT"])
@login_required
def update_comment(pin_id, comment_id):
    """
    Updates a comment
    """
    pin = Pin.query.get(pin_id)
    # checks if pin exists
    if not pin:
        return {'errors': f"Pin {pin_id} does not exist."}, 400
    comment = Comment.query.get(comment_id)
    # checks if comment exists
    if not comment:
        return {'errors': f"Comment {comment_id} does not exist."}, 400
    # checks if current user is a creator of the comment
    if comment.user_id != current_user.id:
        return {'errors': f"User is not the creator of comment {comment_id}."}, 401
    form = CommentForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        form.populate_obj(comment)
        db.session.commit()
        return comment.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@pin_routes.route('/<int:pin_id>/comments', methods=["POST"])
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


@pin_routes.route('/<int:pin_id>/comments/<int:comment_id>', methods=["DELETE"])
@login_required
def delete_comment(pin_id, comment_id):
    """
    Deletes a comment
    """
    pin = Pin.query.get(pin_id)
    # checks if pin exists
    if not pin:
        return {'errors': f"Pin {pin_id} does not exist"}, 400
    comment = Comment.query.get(comment_id)
    # checks if comment exists
    if not comment:
        return {'errors': f"Comment {comment_id} does not exist."}, 400
    # checks if current user is a creator of the comment
    if comment.user_id != current_user.id:
        return {'errors': f"User is not the creator of comment {comment_id}."}, 401
    db.session.delete(comment)
    db.session.commit()
    return {'message': 'Delete successful.'}





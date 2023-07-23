from flask import Blueprint, jsonify, session, request
from flask_login import current_user, login_required
from app.models import db, Pin, Comment
from app.forms import CommentForm, PinForm
from app.api.auth_routes import validation_errors_to_error_messages

pin_routes = Blueprint('pins', __name__)


@pin_routes.route('/')
# @login_required

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
    # checks if pin exists
    if not pin:
        return {'errors': f"Pin {id} does not exist."}
    comments = Comment.query.filter(Comment.pin_id == id).all()
    comments_ids = [comment for comment in comments]
    return pin.to_dict()



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

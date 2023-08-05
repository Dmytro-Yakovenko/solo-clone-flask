from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Board

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>/boards')
@login_required
def get_boards_by_user_id(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    # checking if user exist
    user = User.query.get(id)
    if not user:
        return {'errors': f"User {id} does not exist"}, 404
    boards = Board.query.filter_by(user_id=id)
    board_list=[]
    for board in boards:
        board_dict=board.to_dict()
        board_list.append(board_dict)
    return jsonify({"boards":board_list})
   


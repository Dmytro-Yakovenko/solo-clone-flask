from flask import Blueprint, jsonify, request
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


@user_routes.route('/<int:id>/boards/search')
@login_required
def get_boards_by_title(id):
    """
    Query for a board by user_id and title and returns board or message "no boards"
    """
    # checking if user exist
    user = User.query.get(id)
    if not user:
        return {'errors': f"User {id} does not exist"}, 404
    args = request.args
    title =args.to_dict()
    board = Board.query.filter(Board.user_id==id, Board.title==title['title']).first()
    if board:
        return board.to_dict()
    return jsonify({'message':"no boards"})


@user_routes.route('/<int:id>/edit')
@login_required
def edit_user(id):
    """
    Update for a user by user_id  "coming soon"
    """
    # checking if user exist
    user = User.query.get(id)
    if not user:
        return {'errors': f"User {id} does not exist"}, 404
   
   
  
    return jsonify({'message':"coming soon"})


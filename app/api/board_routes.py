from flask import Blueprint, jsonify, session, request
from flask_login import current_user, login_required
from app.models import db, Pin, Comment, Board
from app.forms import CommentForm, PinForm, BoardForm
from app.api.auth_routes import validation_errors_to_error_messages

board_routes = Blueprint('boards', __name__)
board_image_urls ={
     "American":"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689654276/pexels-robin-stickel-70497_1_ehdkcs.jpg",
     "Mexican":"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689865891/pexels-hana-brannigan-3642718_daru6k.jpg",
     "Chinese": "https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866146/pexels-prince-photos-3054690_bdu2rr.jpg",
     "Japanese":"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689866449/pexels-rajesh-tp-2098085_lylhr7.jpg",
     "Korean":"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867051/pexels-senuscape-2313682_q11qva.jpg",
     "French":"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689867882/pexels-chevanon-photography-323682_1_jkrutt.jpg",
     "Italian":"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868810/pexels-vincent-rivaud-2295285_jrjr9q.jpg",
     "Ukrainian":"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868646/pexels-polina-tankilevitch-8601410_xln2nn.jpg",
     "Mediterranean":"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868414/pexels-max-ravier-10563267_mdgbsj.jpg",
     "Vegetarian":"https://res.cloudinary.com/dr1ekjmf4/image/upload/v1689868220/pexels-maarten-van-den-heuvel-2284166_i6ptee.jpg",
}

@board_routes.route('/')
@login_required

def get_all_boards():
    """
    Query for all boards of  and returns them in a list of board dictionaries
    """
    
    boards = Board.query.all()
    board_list=[]
    for board in boards:
        board_dict=board.to_dict()
        board_list.append(board_dict)
    return jsonify({"boards":board_list})


@board_routes.route('/<int:id>')
@login_required
def get_board(id):
    """
    Query for a board  by id and returns that board in a dictionary
    """
    board = Board.query.get(id)
    # checks if pin exists
    if not board:
        return {'errors': f"Board {id} does not exist."}, 404
    # pins = Pin.query.filter(Pin.pin_id == id).all()
    # pin_ids = [pin for pin in pins]
    return board.to_dict()








@board_routes.route('/', methods=["POST"])
@login_required
def create_board():
    """
    Creates a new board
    """
  
    form = BoardForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        board = Board(
            title=form.data['title'],
            user_id=current_user.id,
            description=form.data['description'],
            board_image_url=board_image_urls[form.data['title']]
        )
        db.session.add(board)
        db.session.commit()
        return board.to_dict(), 201
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400



@board_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_board(id):
    """
    Updates a pin
    """
    board = Board.query.get(id)
   
    # checks if board exists
    if not board:
        return {'errors': f"Board {id} does not exist."}, 404
    # checks if current user is a creator of the board
    if board.user_id != current_user.id:
        return {'errors': f"User is not the creator of pin {id}."}, 401
    form = BoardForm()
   
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        
        form.populate_obj(board)
        
        db.session.commit()
        return board.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400




@board_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_board(id):
    """
    Deletes a board
    """
    board = Board.query.get(id)
    # checks if board exists
    if not board:
        return {'errors': f"Board {id} does not exist."}, 400
    # checks if current user is a creator of the board
    if board.user_id != current_user.id:
        return {'errors': f"User is not the creator of board {id}."}, 401
    db.session.delete(board)
    db.session.commit()
    return {'message': 'Delete successful.'}





@board_routes.route('/<int:board_id>/pins', methods=["POST"])
@login_required
def create_pin(board_id):
    """
    Creates a new pin
    """
    board = Board.query.get(board_id)
    # checks if board exists
    if not board:
        return {'errors': f"Board {board_id} does not exist"}, 404
   
    form = PinForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        
        pin = Pin(
            title=form.data['title'],
            description= form.data['description'],
            ingredients=form.data['ingredients'],
            time = form.data['time'],
           
            user_id= current_user.id,
            image_url= form.data['image_url'],
         
        )
        db.session.add(pin)
        db.session.commit()
        return pin.to_dict(), 201
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400
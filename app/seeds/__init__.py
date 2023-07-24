from flask.cli import AppGroup
from .users import seed_users, undo_users
from .pins import seed_pins, undo_pins
from .boards import seed_boards, undo_boards
from .pinboards import seed_pins_boards, undo_pins_boards
from .comments import seed_comments, undo_comments
from app.models.db import db, environment, SCHEMA


# Creates a seed group to hold our commands
# So we can type flask seed --help
seed_commands = AppGroup('seed')

# Creates the flask seed all command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
       
        undo_users()
        undo_pins()
        undo_boards()
        undo_pins_boards()
        undo_comments()
    seed_users()
    seed_boards()
    seed_pins()
    seed_comments()
    seed_pins_boards()

    # Add other seed functions here


# Creates the flask seed undo command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_pins()
    undo_boards()
    undo_pins_boards()
    undo_comments()
    # Add other undo functions here
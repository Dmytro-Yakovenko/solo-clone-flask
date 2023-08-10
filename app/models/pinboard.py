from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod


class PinBoard(db.Model):
    __tablename__ = 'pins_boards'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    pin_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('pins.id')), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('boards.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    

    def to_dict(self):
        return {
            'board_id':self.board_id,
            # 'pin_id':self.pin_id,
            # 'created_at': self.created_at,
            # 'updated_at': self.updated_at
        }

    
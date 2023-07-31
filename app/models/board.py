from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod


class Board(db.Model):
    __tablename__ = 'boards'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    description =  db.Column(db.String(1500), nullable=False)
    title =  db.Column(db.String(255), nullable=False, unique=True)
    board_image_url=db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    pin = db.relationship("Pin", secondary=add_prefix_for_prod("pins_boards"), back_populates= "board")
    user = db.relationship("User", back_populates="board")
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id':self.user_id,
            'description': self.description,
            'title': self.title,
            'pins': [pin.to_dict() for pin in self.pin],
            'board_image_url':self.board_image_url,
            'created_at': self.created_at,
            'updated_at': self.updated_at
            
            
        }
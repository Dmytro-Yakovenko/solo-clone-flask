from .db import db, environment, SCHEMA, add_prefix_for_prod


class Board(db.Model):
    __tablename__ = 'boards'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    description =  db.Column(db.String(500), nullable=False)
    title =  db.Column(db.String(255), nullable=False)
    
    pin = db.relationship("Pin", secondary=add_prefix_for_prod("board_pins", back_populates= "boards"))
    user = db.relationship("User", back_populates="board")
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id':self.user_id,
            'description': self.description,
            'title': self.title,
            'pins': [pin.to_dict() for pin in self.pin]
            
        }
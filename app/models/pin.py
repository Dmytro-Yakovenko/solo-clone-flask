from .db import db, environment, SCHEMA, add_prefix_for_prod


class Pin(db.Model):
    __tablename__ = 'pins'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(255), nullable=False)
    description =  db.Column(db.String(500), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    time =  db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    
    
    user=db.relationship("User", back_populates="pin")
    board = db.relationship("Board", secondary=add_prefix_for_prod("board_pins", back_populates="pin"))
    comment = db.relationship("Comment", back_populates="pin", cascade="all , delete-orphan")
    image = db.relationship("Image", back_populates="pin",cascade="all , delete-orphan" )
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'ingredients': self.ingredients,
            'time': self.time,
            "user_id":self.user_id,
            "comments": [comment.to_dict() for comment in self.comment],
            "images": [image.to_dict() for image in self.image]
        }
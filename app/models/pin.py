from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod


class Pin(db.Model):
    __tablename__ = 'pins'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(255), nullable=False)
    description =  db.Column(db.String(1500), nullable=False)
    ingredients = db.Column(db.String(1500), nullable=False)
    time =  db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    image_url = db.Column(db.String(255), default ="https://res.cloudinary.com/dr1ekjmf4/image/upload/v1691726195/bc2d04276b5bfde9bce68c7a91914b7f_mi6kmp.jpg")
    is_saved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user=db.relationship("User", back_populates="pin")
    board = db.relationship("Board", secondary=add_prefix_for_prod('pins_boards'), back_populates="pin")
    comment = db.relationship("Comment", back_populates="pin", cascade="all , delete-orphan")
   
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'ingredients': self.ingredients,
            'time': self.time,
            "user_id":self.user_id,
            "comments": [comment.to_dict() for comment in self.comment],
            "images": self.image_url,
            "user": self.user.to_dict(),
            "is_saved":self.is_saved,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
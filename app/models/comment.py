from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod


class Comment(db.Model):
    __tablename__ = 'comments'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    pin_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("pins.id")))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user =db.relationship("User", back_populates="comment")
    pin =db.relationship("Pin", back_populates="comment")
    
    def to_dict(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'user_id': self.user_id,
            'pin_id': self.pin_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'user':self.user.to_dict()
        }
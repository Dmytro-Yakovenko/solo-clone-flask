from .db import db, environment, SCHEMA, add_prefix_for_prod


class Comment(db.Model):
    __tablename__ = 'comments'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    user_pin = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("pins.id")))
    
    user =db.relationship("User", back_populates="comment")
    pin =db.relationship("Pin", back_populates="comment")
    
    def to_dict(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'user_id': self.user_id,
            'user_pin': self.user_pin,
        }
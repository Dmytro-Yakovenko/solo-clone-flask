from .db import db, environment, SCHEMA, add_prefix_for_prod


class Pin(db.Model):
    __tablename__ = 'images'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    image_url=db.Column(db.String(255), nullable=False)
    title =  db.Column(db.String(255), nullable=False)
    pin_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("pins.id")))
    
    pin = db.relationship("Pin", back_populates="Image")
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'title': self.title,
            'pin_id': self.pin_id,
        }
    
    
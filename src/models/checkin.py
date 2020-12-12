from app import db
import enum


class CheckInStatus(enum.Enum):
    active = 'active'
    deleted = 'deleted'

class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hours = db.Column(db.Float, nullable=False)
    tag_id = db.Column(db.Integer, nullable=False, db.ForeignKey('tags.id'))    
    activity = db.Column(db.Unicode, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(CheckInStatus), nullable=False)
    user_id = db.Column(db.Integer, nullable=False, db.ForeignKey('users.id'))


    tag = db.relationship("Tag", back_populates="checkins")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

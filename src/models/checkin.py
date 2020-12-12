from dataclasses import dataclass
from app import db
import enum

from src.models.tag import Tag


class CheckInStatus(enum.Enum):
    active = 'active'
    deleted = 'deleted'


@dataclass
class CheckIn(db.Model):
    __tablename__ = 'checkins'

    id: int
    hours: float
    activity: str
    date: str
    status: CheckInStatus
    tag: Tag


    id = db.Column(db.Integer, primary_key=True)
    hours = db.Column(db.Float, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)    
    activity = db.Column(db.Unicode, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(CheckInStatus), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    tag = db.relationship("Tag", foreign_keys=tag_id)
    user = db.relationship("User", foreign_keys=user_id, lazy=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

from dataclasses import dataclass, asdict
from datetime import datetime
from app import db
from flask import session
import enum

from src.models.tag import Tag
# from src.models.user import User


class CheckInStatus(str, enum.Enum):
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
    # user: User



    id = db.Column(db.Integer, primary_key=True)
    hours = db.Column(db.Float, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)    
    activity = db.Column(db.Unicode, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(CheckInStatus), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    tag = db.relationship("Tag", foreign_keys=tag_id)
    user = db.relationship("User", foreign_keys=user_id, lazy=True)





    def __init__(self, 
        hours = None, 
        tag_id = None, 
        tag_name = None,
        activity = None,
        date = datetime.now(),
        status = CheckInStatus.active,
        user_id = None,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        # Default user_id to session user id
        if user_id is None and session.get('user') is not None:
            self.user_id = session.get('user')['id']

       
        self.hours = hours
        self.tag_id = tag_id
        self.activity = activity
        self.date = date
        self.status = status
        self.__tmp_tag_name = tag_name


    def add(self):
         # Create new tag entry if tag_name exists
        if self.__tmp_tag_name is not None:
            t = Tag.get_by_name(self.__tmp_tag_name)

            if t is None:
                newTag = Tag(name=self.__tmp_tag_name)
                newTag.add()

                self.tag_id = newTag.id
            else:
                self.tag_id = t.id

            del self.__tmp_tag_name


        db.session.add(self)
        db.session.commit()



    @staticmethod
    def get_all_by_user(user_id):
        s = CheckIn.query.filter_by(user_id = user_id, status=CheckInStatus.active).all()

        return [asdict(checkin) for  checkin in s]

    @staticmethod
    def verify_user_id(checkin_id):
        c = CheckIn.query.filter_by(id=checkin_id).first()
        
        if c is None:
            return -1

        return c.user_id, c


    def delete(self):
        self.status = CheckInStatus.deleted
        db.session.commit()


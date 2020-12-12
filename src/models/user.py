from dataclasses import dataclass
from app import db

@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id: int
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode, nullable=False)
    password = db.Column(db.Unicode, nullable=False)

    checkins = db.relationship("CheckIn", back_populates="user", lazy=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    @staticmethod
    def login(username, password):
        return User.query.filter_by(username=username, password=password).first()
        
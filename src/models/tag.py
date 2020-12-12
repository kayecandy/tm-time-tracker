from dataclasses import dataclass
from app import db

@dataclass
class Tag(db.Model):
    __tablename__ = 'tags'

    id: int
    name: str


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
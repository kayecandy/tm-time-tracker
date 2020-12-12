from dataclasses import dataclass, asdict
import os
from app import db


@dataclass
class Tag(db.Model):
    __tablename__ = 'tags'

    id: int
    name: str


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)

    def __init__(
        self, 
        name = None,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.name = name


    @staticmethod
    def get_by_name(name):
        return Tag.query.filter_by(
            name = name
        ).first()

    @staticmethod
    def search(keyword, 
        limit=os.getenv('SEARCH_LIMIT', 10)
    ):
        s = Tag.query.filter(Tag.name.like('%{}%'.format(keyword))).limit(limit).all()

        return [asdict(tag) for tag in s]


    def add(self):
        db.session.add(self)
        db.session.commit()
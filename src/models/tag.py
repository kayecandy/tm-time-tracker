from app import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
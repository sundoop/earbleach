from app import db
from sqlalchemy.dialects.postgresql import JSON


class Worm(db.Model):
    __tablename__ = 'worms'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True)
    url = db.Column(db.String(), unique=True)

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __repr__(self):
        return '<id: {} title: {} url: {}>'.format(self.id, self.title, self.url)

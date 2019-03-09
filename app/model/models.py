from app import db
from datetime import datetime

# this is the schema (a basic model for the database setup)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')  # referenced via the classname (the many side)!

    def __repr__(self):
        return 'This is User {}'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(110))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # lowercase <tablename>.value!

    def __repr__(self):
        return 'This is Post {}'.format(self.body)

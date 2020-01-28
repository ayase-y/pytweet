from datetime import datetime
from Pytweet.database import db
from flask_login import UserMixin


class User(UserMixin,db.Model):

    __tablename__="users"

    id = db.Column(db.Integer,primary_key = True)
    fullname = db.Column(db.String(255),nullable=False)
    username = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255),nullable=False)

    posts = db.relationship("Post",backref="author",lazy=True)
    profiles = db.relationship("Profile",backref="author",lazy=True)
    comments = db.relationship("Comments",backref="author",lazy=True)

    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)

    def __init__(self,fullname,username,password):
        self.fullname = fullname
        self.username = username
        self.password = password

    def is_active(self):
        return True
    def is_authenticated(self):
        return True

class Post(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    comments = db.relationship("Comments",backref="post",lazy=True)
    post = db.Column(db.String(1000),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)


class Profile(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    first_name = db.Column(db.String(1000),nullable=False)
    second_name = db.Column(db.String(1000),nullable=False)
    address = db.Column(db.String(1000),nullable=False)
    occupation = db.Column(db.String(1000),nullable=False)
    birth_day = db.Column(db.DateTime,nullable=False)
    skills = db.Column(db.String(1000),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)


class Comments(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey("post.id"),nullable=False)
    comment = db.Column(db.String(1000),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)
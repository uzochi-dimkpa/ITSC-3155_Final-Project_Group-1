from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()



#: TEMPORARY; WILL EDIT/UPDATE LATER

# CRUD Resource #1
class User(db.Model):
    # TODO: Update SQLAlchemy Table here
    __tablename__ = 't_user'

    user_id = db.Column(db.Integer, nullable = False, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    user_password = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    num_friends = db.Column(db.Integer, nullable = True)

    def __init__(self, username, user_password, first_name, last_name, num_friends):
        self.username = username; self.password = user_password
        self.first_name = first_name; self.last_name = last_name
        self.num_friends = num_friends

    def __repr__(self):
        return f'User #{self.user_id}:\n\
                Username: {self.username}, Password: {self.user_password}\n\
                First Name: {self.first_name}, Last Name: {self.last_name}\n\
                # of Friends: {self.num_friends}\n\n\n'



# CRUD Resource #2
class Post(db.Model):
    # TODO: Update SQLAlchemy Table here
    __tablename__ = 't_post'

    post_id = db.Column(db.Integer, nullable = False, primary_key = True)
    title = db.Column(db.String, nullable = False)
    body = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, server_default=func.now()) #- server_default=db.func.now()
    updated_at = db.Column(db.DateTime, nullable = True, server_default=None, onupdate=func.now()) #- server_default=db.func.now(),

    user_id = db.Column(db.Integer, db.ForeignKey('t_user.user_id'), nullable = False)
    user = db.relationship('User', backref='posts', lazy=True)

    def __init__(self, title, body, user_id, created_at, updated_at):
        self.title = title; self.body = body
        self.created_at = created_at; self.updated_at = updated_at
        self.user_id = user_id

    def get_top_four_posts():
        return Post.query.filter_by(Post.post_id < 5)

    def __repr__(self):
        return f'Post #{self.post_id}:\n\
                User #{self.user_id}\n\
                Title: {self.title}\n\
                Body: {self.body}\n\
                Created At: {self.created_at}, Updated At: {self.updated_at}\n\n\n'



# CRUD Resource #3
class Comment(db.Model):
    # TODO: Update SQLAlchemy Table here
    __tablename__ = 't_comment'

    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('t_post.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('t_user.user_id'), nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime, nullable=True, server_default=None, onupdate=func.now())

    def __init__(self, comment_text, user_id, post_id, created_at, updated_at):
        self.comment_text = comment_text
        self.user_id = user_id; self.post_id = post_id
        self.created_at = created_at; self.updated_at = updated_at

    def __repr__(self):
        return f'Comment #{self.comment_id}:\n\
                Post #{self.post_id}, User #{self.user_id}\n\
                Text: {self.comment_text}\n\
                Created At: {self.created_at}, Updated At: {self.updated_at}\n\n\n'



# Server-side resource #1
class Language(db.Model):
    # TODO: Update SQLAlchemy Table here
    __tablename__ = 't_language'

    language_name = db.Column(db.String, nullable=False,unique=True,primary_key=True)

    def __repr__(self):
        return f'Language class'

language_singleton = Language()



# Server-side resource #2
class Tag(db.Model):
    # TODO: Update SQLAlchemy Table here
    __tablename__ = 't_tag'

    tag_name = db.Column(db.String, nullable=False,unique=True,primary_key=True)

    def __repr__(self):
        return f'Tag class'

tag_singleton = Tag()



# Server-side resource #3
class Relationship(db.Model):
    # TODO: Update SQLAlchemy Table here
    __tablename__ = 't_relate'

    relate_type = db.Column(db.String, nullable = False, unique = True, primary_key = True)

    # def __init__(self, relate_type):
    #     self.relate_type = relate_type

    def __repr__(self):
        return f'Relationship type: {self.relate_type}\n'

relationship_singleton = Relationship()
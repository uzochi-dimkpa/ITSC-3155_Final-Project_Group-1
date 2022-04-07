from enum import unique
from flask_sqlalchemy import SQLAlchemy

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
        return f'User #{self.user_id}:\
                \nUsername: {self.username}, Password: {self.user_password}\n\
                First Name: {self.first_name}, Last Name: {self.last_name}\n\
                # of Friends: {self.num_friends}\n\n\n'



# CRUD Resource #2
class Post(db.Model):
    # TODO: Update SQLAlchemy Table here

    def __repr__(self):
        return f'Post class'



# CRUD Resource #3
class Comment(db.Model):
    # TODO: Update SQLAlchemy Table here

    def __repr__(self):
        return f'Question class'



# Server-side resource #1
class Language(db.Model):
    # TODO: Update SQLAlchemy Table here

    def __repr__(self):
        return f'Language class'

language_singleton = Language()



# Server-side resource #2
class Tag(db.Model):
    # TODO: Update SQLAlchemy Table here

    def __repr__(self):
        return f'Tag class'

tag_singleton = Tag()



# Server-side resource #3
class Relationship(db.Model):
    # TODO: Update SQLAlchemy Table here
    __tablename__ = 't_relate'

    relate_type = db.Column(db.String, nullable = False, unique = True, primary_key = True)

    def __init__(self, relate_type):
        self.relate_type = relate_type

    def __repr__(self):
        return f'Relationship type: {self.relate_type}\n'

relationship_singleton = Relationship()
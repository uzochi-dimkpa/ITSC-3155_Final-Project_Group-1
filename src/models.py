from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



#: TEMPORARY; WILL EDIT/UPDATE LATER

# CRUD Resource #1
class User(db.Model):
    # TODO: Update SQLAlchemy Table here

    def __repr__(self):
        return f'User class'



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

    def __repr__(self):
        return f'Relationship class'

relationship_singleton = Relationship()
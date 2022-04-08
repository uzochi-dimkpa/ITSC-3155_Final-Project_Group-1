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
    comment_id = db.Column(db.Integer, primary_key=true)
    post_id = db.Column(db.Integer, nullable=true)
    user_id = db.Column(db.Integer, nullable=true)
    title = db.Colum(db.Text, nullable=false)
    comment_text = db.Column(db.Text, nullable=false)
    created_at = db.Column(db.DateTime, nullable=false)
    updated_at = db.Column(db.DateTime, nullable=true)



    def __repr__(self):
        return f'Question class'



# Server-side resource #1
class Language(db.Model):
    # TODO: Update SQLAlchemy Table here
    language_name = db.Column(db.VarChar(255), nullable=false,unique=true,primary_key=true)

    def __repr__(self):
        return f'Language class'

language_singleton = Language()



# Server-side resource #2
class Tag(db.Model):
    # TODO: Update SQLAlchemy Table here
    tag_name = db.Column(db.VarChar(255), nullable=true,unique=true,primary_key=true)

    def __repr__(self):
        return f'Tag class'

tag_singleton = Tag()



# Server-side resource #3
class Relationship(db.Model):
    # TODO: Update SQLAlchemy Table here

    def __repr__(self):
        return f'Relationship class'

relationship_singleton = Relationship()
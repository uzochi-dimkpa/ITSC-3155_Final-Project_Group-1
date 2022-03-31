from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#: TEMPORARY; WILL EDIT/UPDATE LATER

class Profile(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    profile_role = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Profile class'

profile_singleton = Profile()



class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Question class'

question_singleton = Question()



class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Question class'

comment_singleton = Comment()
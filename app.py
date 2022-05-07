import os
import re
from flask import Flask, abort, redirect, render_template, request, session, g
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from sqlalchemy.sql import func
from src.models import User, Post, Comment, db
from src.blueprints.user_blueprint import router as user_router
from src.blueprints.post_blueprint import router as post_router
# from src.blueprints.comment_blueprint import router as comment_router

app = Flask(__name__)
bcrypt = Bcrypt(app)

load_dotenv()

#This will need to be correctly adjusted:
users = {}


# TODO: RENAME '.env_' FILE TO '.env' AND MAKE CHANGES TO THE
# FIELDS IN YOUR '.env' FILE AS NECESSARY
sql_echo = os.getenv('SQL_ECHO') # Default: False

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL', 'sqlite:///test.db') #- 'CLEARDB_DATABASE_URL', #- f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = eval(str(sql_echo))

db.init_app(app)



@app.before_request
def inject_user_session_profile():
    # TODO: PLACEHODER; the following code will be replaced with code for user login
    # session querying and for returning the user object to the '_layout.html' page
    user_id = 1
    g.logged_in_user = User.query.get(user_id)
    # g.user = db.session.get(session["user_id"])
    # return dict(logged_in_user = g.logged_in_user) #- key = "value",
    # return render_template('_layout.html', logged_in_user = g.logged_in_user)

# @app.context_processor
# def inject_user():
#     user_id = 1
#     logged_in_user = User.query.get(user_id)
#     g.logged_in_user = User.query.get(user_id)
#     return dict(user_id = logged_in_user.user_id) #- key = "value",

@app.get('/')
# Index page should display 4 user-created posts
def index():
    # top_four_posts = Post.query.filter(Post.post_id < 5).all()
    all_posts = Post.query.all()
    post_users = {}; num_comments = {}

    for post in all_posts:
        post_users.update({post.user_id: User.query.filter(post.user_id == User.user_id).first().username})
        num_comments.update({post.post_id: Comment.query.filter(post.post_id == Comment.post_id).count()})

    # Debug
    # print(f'\n\nCurrent DATETIME: {db.func.now()}\n\n')
    # print(f'\n\n\nhashed_user_password: {bcrypt.generate_password_hash(User.query.get(1).user_password).decode("utf-8")}\n\n\n')
    # print(f'\n\n\ncheck_user_password_hash: {bcrypt.check_password_hash(, User.query.get(1).user_pasword)}\n\n\n')
    # print(f'\n\n\n{type(func.now())}\n\n\n')

    return render_template('index.html', all_posts = all_posts, post_users = post_users, num_comments = num_comments) #- , num_posts=num_posts

@app.get('/login')
def login():
    return render_template('login.html')

@app.get('/signup')
def signup():
    return render_template('signup.html')

@app.get('/about')
def about():
    return render_template('about.html')

@app.get('/faq')
def faq():
    return render_template('faq.html')


# CURRENTLY BROKEN
# @app.post('/register')
# def register():
#     username = request.form.get('username', '')
#     password = request.form.get('password', '')

#     if username == '' or password == '':
#         abort(400)

#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

#     new_user = User(username, hashed_password)
#     db.session.add(new_user)
#     db.session.commit()

#     return redirect('/')

# @app.post('/login')
# def login():
#     username = request.form.get('username', '')
#     password = request.form.get('password', '')

#     if username == '' or password == '':
#         abort(400)

#     existing_user = User.query.filter_by(username=username).first()

#     if not existing_user or existing_user.user_id == 0:
#         return redirect('/fail')

#     if not bcrypt.check_password_hash(existing_user.password, password):
#         return redirect('/fail')

#     session['user'] = {
#         'username': username,
#         'user_id': existing_user.user_id,
#     }

#     return redirect('/') #- '/success'



# @app.get('/example')
# def post_example():
#     return render_template('post-example.html')

# @app.get('/profile')
# def user_profile():
#     return render_template('profile.html')

# @app.get('/create-post')
# def create_post():
#     return render_template('create-post.html')

# @app.post('/create-post')
# def create_post_form():
#     redirect('/create-post')



app.register_blueprint(user_router)
app.register_blueprint(post_router)
# app.register_blueprint(comment_router)



if __name__ == '__main__':
    app.run(debug=True)
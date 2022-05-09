import os
import re
from flask import Flask, abort, redirect, render_template, request, session, g
from flask_session import Session
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
# users = {}


# TODO: RENAME '.env_' FILE TO '.env' AND MAKE CHANGES TO THE
# FIELDS IN YOUR '.env' FILE AS NECESSARY
sql_echo = os.getenv('SQL_ECHO') # Default: False
session_secret_key = os.getenv('LOGIN_SIGNUP_SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL', 'sqlite:///test.db') #- 'CLEARDB_DATABASE_URL', #- f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = eval(str(sql_echo))
app.secret_key = session_secret_key

db.init_app(app)



def get_all_users_dict():
    usernames = {}
    all_users = User.query.all()

    for user in all_users:
        usernames.update({user.user_id:user.username})
    
    return usernames

@app.before_first_request
def inject_user_before_first_request():
    first_three_test_users = User.query.filter(User.user_id < 4).all()

    # for i in range(3):
    for user in first_three_test_users:
        # user = User.query.get(i + 1)

        hashed_password = bcrypt.generate_password_hash(user.user_password).decode('utf-8')
        user.user_password = hashed_password

        db.session.add(user)
        db.session.commit()

    
@app.before_request
def inject_user_before_requests():
    # user_id = 1
    # g.logged_in_user = User.query.get(user_id)
    # g.logged_in_user = None


    g.usernames = get_all_users_dict()

    if "user" in session:
        g.logged_in_user = User.query.filter(User.username == session["user"]["username"]).first()

    # print(f'\n\n\n{g.logged_in_user.user_id}\n\n\n')
        # g.logged_in_user = db.session.get(session["user"])
    # g.user = db.session.get(session["user_id"])
    # return dict(logged_in_user = g.logged_in_user) #- key = "value",
    # return render_template('_layout.html', logged_in_user = g.logged_in_user)
    
    if "user" in session:
        g.logged_in_user = User.query.filter(User.username == session["user"]["username"]).first()

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
    # print(f"\n\n\n{session['user']['username'][0]}\n\n\n")
    # print(f"\n\n\n{User.query.filter(User.username == session['user']['username']).first()}\n\n\n")

    return render_template('index.html', all_posts = all_posts, post_users = post_users, num_comments = num_comments) #- , num_posts=num_posts

@app.get('/loginpage')
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

@app.post('/register')
def register():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    bio = request.form.get('bio', '')

    if username == '' or password == '' or username is None or password is None:
        # abort(400)
        return redirect('/signup')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(username=username, user_password=hashed_password,first_name=first_name,last_name=last_name,bio=bio,num_friends=0)

    session['user'] = {
        'username': username,
        'user_id': new_user.user_id,
    }
    
    
    #SQL Session
    db.session.add(new_user)
    db.session.commit()

    #User Session
    # session['user'] = {
    #     'username': username,
    # }


    return redirect('/')

@app.post('/login')
def login_to_webpage():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    if username == '' or password == '':
        return redirect('/loginpage')

    # existing_user = User.query.filter_by(username=username).first()
    existing_user = User.query.filter(User.username == username).first()

    if not existing_user or existing_user.user_id == 0:
        # return redirect('/fail')
        return redirect('/loginpage')

    if not bcrypt.check_password_hash(existing_user.user_password, password):
        # return redirect('/fail')
        return redirect('/loginpage')

    session['user'] = {
        'username': username,
        'user_id': existing_user.user_id,
    }


    return redirect('/')

# @app.get('/success')
# def success():
#     if not 'user' in session:
#         abort(401)
#     return render_template('index.html', user=session['user']['username'])


@app.get('/fail')
def fail():
    if 'user' in session and User.query.filter(User.username == session['user']['username']).first() is not None: #- and User.query.get(session['user']['username'][0] is not None #- 
        return redirect('/')
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'user' not in session:
        abort(401)

    del session['user']
    # session['user']['username'] = None

    return redirect('/')


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
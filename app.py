import os
from flask import Flask, abort, redirect, render_template, request, session, g
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from sqlalchemy.sql import func
from src.models import User, Post, Comment, db
from src.blueprints.user_blueprint import router as user_router
from src.blueprints.post_blueprint import router as post_router

app = Flask(__name__)
bcrypt = Bcrypt(app)



load_dotenv()



# TODO: RENAME '.env_' FILE TO '.env' AND MAKE CHANGES TO THE
# FIELDS IN YOUR '.env' FILE AS NECESSARY
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL', 'sqlite:///test.db') #- 'CLEARDB_DATABASE_URL', #- f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = eval(str(os.getenv('SQL_ECHO')))
app.config['SECRET_KEY'] = os.getenv('LOGIN_SIGNUP_SECRET_KEY')
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 60}
# app.config['SESSION_TYPE'] = 'filesystem'



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
    g.usernames = get_all_users_dict()

    if "user" in session:
        g.logged_in_user = User.query.filter(User.username == session["user"]["username"]).first()

@app.get('/')
# Index page should display all user-created posts
def index():
    all_posts = Post.query.all()
    post_users = {}; num_comments = {}

    for post in all_posts:
        post_users.update({post.user_id: User.query.filter(post.user_id == User.user_id).first().username})
        num_comments.update({post.post_id: Comment.query.filter(post.post_id == Comment.post_id).count()})

    # if "user" not in session:
    #     print("no user")
    # Debug
    # print(f'\n\nCurrent DATETIME: {db.func.now()}\n\n')
    # print(f'\n\n\nhashed_user_password: {bcrypt.generate_password_hash(User.query.get(1).user_password).decode("utf-8")}\n\n\n')
    # print(f'\n\n\ncheck_user_password_hash: {bcrypt.
    # check_password_hash(, User.query.get(1).user_pasword)}\n\n\n')
    # print(f'\n\n\n{type(func.now())}\n\n\n')
    
    # user = User.query.get(int(session["user"]["user_id"]))

    return render_template('index.html', all_posts = all_posts, post_users = post_users, num_comments = num_comments) #- , num_posts=num_posts

@app.get('/loginpage')
def login():
    return render_template('login.html')

# @app.get('/signup_error')
# def signup_error():
#     return render_template('signup.html',message="Username is already taken!")

@app.get('/signup')
def signup():
    return render_template('signup.html')

@app.get('/about')
def about():
    return render_template('about.html')

@app.get('/faq')
def faq():
    return render_template('faq.html')

# @app.get('/success')
# def success():
#     return render_template("index.html")

# @app.get('/fail')
# def fail():
#     return render_template("login.html",message="Incorrect password!")

@app.get('/logout')
def logout():
    del session['user']

    return redirect('/')

@app.post('/register')
def register():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    bio = request.form.get("bio", '')

    if username == '' or password == '':
        return render_template("signup.html", message = "You didn't enter in anything!")
        # return redirect("/signup")

    if db.session.query(User.user_id).filter_by(username=username).first():
        return render_template("signup.html", message = "This user already exists!")
        # return redirect("/signup")

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, user_password=hashed_password,first_name=first_name,last_name=last_name,bio=bio,num_friends=0)
    
    # SQL Session
    db.session.add(new_user)
    db.session.commit()

    # User login session
    session['user'] = {
        'username': username,
        'user_id': new_user.user_id,
    }

    return redirect('/')

@app.post('/login')
def login_to_webpage():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    if username == '' or password == '':
        return render_template("login.html", message = "You didn't enter in anything!")
        # return redirect('/loginpage')

    existing_user = User.query.filter_by(username=username).first()

    if not existing_user or existing_user.user_id == 0:
        return render_template("login.html", message = "This user doesn't exist!")
        # return redirect('/loginpage')

    if not bcrypt.check_password_hash(existing_user.user_password, password):
        return render_template("login.html", message = "You entered incorrect information!")
        # return redirect('/loginpage')

    session['user'] = {
        'username': username,
        'user_id': existing_user.user_id,
    }

    return redirect('/')


app.register_blueprint(user_router)
app.register_blueprint(post_router)



if __name__ == '__main__':
    app.run(debug=True)
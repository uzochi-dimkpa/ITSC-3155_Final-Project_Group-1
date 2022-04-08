import os
import re
from flask import Flask, abort, redirect, render_template, request
from dotenv import load_dotenv
from src.models import db
from src.blueprints.user_blueprint import router as user_router
from src.blueprints.post_blueprint import router as post_router
from src.blueprints.comment_blueprint import router as comment_router

app = Flask(__name__)

load_dotenv()


# RENAME '.env_' FILE TO '.env' AND MAKE CHANGES TO FIELDS AS NECESSARY
db_host = os.getenv('DB_HOST') # Default: localhost
db_port = os.getenv('DB_PORT') # Default: 3306
db_user = os.getenv('DB_USER', 'root') # Default: root
db_pass = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME') # Server default: DuoLing
sql_echo = os.getenv('SQL_ECHO') # Default: False

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = sql_echo

db.init_app(app)


@app.get('/')
def index():
    return render_template('index.html')


app.register_blueprint(user_router)
app.register_blueprint(post_router)
app.register_blueprint(comment_router)


@app.get('/login')
def login():
    return render_template('login.html')

@app.get('/signup')
def signup():
    return render_template('signup.html')

@app.get('/create-post')
def create_question():
    return render_template('create-post.html')

@app.post('/create-post')
def create_question_form():
    
    redirect('/create-post')

@app.get('/about')
def about():
    return render_template('about.html')

@app.get('/faq')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(debug=True)

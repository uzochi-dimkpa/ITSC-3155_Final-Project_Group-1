import os
import re
from flask import Flask, abort, redirect, render_template, request
from dotenv import load_dotenv
from src.models import db
from src.blueprints.profile_blueprint import router as profile_router
from src.blueprints.question_blueprint import router as question_router
from src.blueprints.comment_blueprint import router as comment_router

app = Flask(__name__)

load_dotenv()


db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER', 'root')
db_pass = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)


@app.get('/')
def index():
    return render_template('index.html')


app.register_blueprint(profile_router)
app.register_blueprint(question_router)
app.register_blueprint(comment_router)


@app.get('/login')
def login():
    return render_template('login.html')

@app.get('/signup')
def signup():
    return render_template('signup.html')

#app get for /create-question
@app.get('/create-question')
def create_question():
    return render_template('create-question.html')

@app.post('/create-question')
def create_question_form():
    
    redirect('/create-question')

if __name__ == '__main__':
    app.run(debug=True)

@app.get('/profile')
def profile():
    return render_template('profile.html')

@app.get('/about')
def about():
    return render_template('about.html')

@app.get('/faq')
def faq():
    return render_template('faq.html')

from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


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

@app.get('/faq')
def faq():
    return render_template('faq.html')
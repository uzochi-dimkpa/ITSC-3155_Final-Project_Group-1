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


if __name__ == '__main__':
    app.run(debug=True)
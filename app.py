from flask import Flask, abort, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h3>SSF ORGANIZATION. ALL THE RIGHTS COPYRIGHTED</h3>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

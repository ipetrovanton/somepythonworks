from flask import render_template
from . import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Никита'}
    posts = [
        {
            'author': {'username': 'Марк'},
            'body': 'O, hi, Mark!'
        },
        {
            'author': {'username': 'Боб'},
            'body': 'Совы не то, чем кажутся'
        },
        {
            'author': {'username': 'Билл'},
            'body': 'Помни! Реальность — иллюзия, вселенная — голограмма, скупай золото, пока! '
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
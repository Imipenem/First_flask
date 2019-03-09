from app import app
from flask import render_template
from app.model.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Philipp'}
    posts = [
        {'autor': 'Dummy1',
         'body': 'LoremIpsum'
         },

        {'autor': 'Dummy2',
         'body': 'DolorSiAmet'
         }

    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

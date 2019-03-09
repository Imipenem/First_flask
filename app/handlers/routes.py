from app import app
from flask import render_template, redirect, flash, url_for
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


# default function decorator for methods is only GET !!!
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successful {}, will be soon redirected'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

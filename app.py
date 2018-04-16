from flask import Flask, render_template, flash, redirect
from config import Config
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models


@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Иполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/actors')
def show_actors():
    user = {'username': 'Эльдар Рязанов'}
    needed = list()
    actors = models.Actor.query.all()

    for actor in actors:
        a = dict()
        a['name'] = str(models.Employee.query.get(actor.employee_id).name)
        a['genre'] = str(models.Genre.query.get(actor.best_genre))
        a['voice'] = str(models.Voice.query.get(actor.voice_range))
        needed.append(a)

    return render_template('actors.html', title='Actors', user=user, actors=needed)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run()

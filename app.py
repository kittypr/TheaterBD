import datetime

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

actors_page_dir = "/act/"
actors_photos_dir = "/static/images/photos/"


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/act/<actor_id>')
def actor_page(actor_id):
    actor = models.Actor.query.filter_by(employee_id=actor_id).first()
    actor_awards = models.Award.query.filter_by(actor_id=actor_id).order_by(models.Award.date).all()

    actor_info = dict()
    name = str(models.Employee.query.get(actor.employee_id).name)
    age = datetime.date.today().year - models.Employee.query.get(actor.employee_id).birth.year
    sex = str(models.Employee.query.get(actor.employee_id).sex)
    sex = 'female' if sex == 'f' else 'male'
    actor_info['name'] = name
    actor_info['age'] = age
    actor_info['sex'] = sex
    actor_info['about'] = str(actor.about)
    actor_info['hire'] = models.Employee.query.get(actor.employee_id).hire_date.year
    actor_info['genre'] = str(models.Genre.query.get(actor.best_genre))
    actor_info['voice'] = str(models.Voice.query.get(actor.voice_range))
    actor_info['photo_id'] = actors_photos_dir + str(actor.employee_id) + ".png"
    actor_awards = actor_awards if len(actor_awards) > 0 else None
    return render_template('act/actor_page.html', title=name, actor=actor_info, awards=actor_awards)


@app.route('/actors')
def show_actors():
    needed = list()
    actors = models.Actor.query.all()

    for actor in actors:
        a = dict()
        a['name'] = str(models.Employee.query.get(actor.employee_id).name)
        a['genre'] = str(models.Genre.query.get(actor.best_genre))
        a['voice'] = str(models.Voice.query.get(actor.voice_range))
        a['page_id'] = actors_page_dir + str(actor.employee_id)
        needed.append(a)

    return render_template('actors.html', title='Actors', actors=needed, sort_allowed=True)


@app.route('/act/genre/<genre>')
def genre_selected_actors(genre):
    needed = list()
    actors = models.Actor.query.join(models.Genre).filter_by(name=genre).join(models.Employee).order_by(models.Employee.name)

    for actor in actors:
        a = dict()
        a['name'] = str(models.Employee.query.get(actor.employee_id).name)
        a['genre'] = str(models.Genre.query.get(actor.best_genre))
        a['voice'] = str(models.Voice.query.get(actor.voice_range))
        a['page_id'] = actors_page_dir + str(actor.employee_id)
        needed.append(a)

    return render_template('actors.html', title='Actors', actors=needed, sort_allowed=False)


@app.route('/act/voice/<voice>')
def voice_selected_actors(voice):
    needed = list()
    actors = models.Actor.query.join(models.Voice).filter_by(name=voice).join(models.Employee).order_by(models.Employee.name)

    for actor in actors:
        a = dict()
        a['name'] = str(models.Employee.query.get(actor.employee_id).name)
        a['genre'] = str(models.Genre.query.get(actor.best_genre))
        a['voice'] = str(models.Voice.query.get(actor.voice_range))
        a['page_id'] = actors_page_dir + str(actor.employee_id)
        needed.append(a)

    return render_template('actors.html', title='Actors', actors=needed, sort_allowed=False)


@app.route('/actors/<sort>')
def sorted_show_actors(sort):
    needed = list()
    if sort == 'genre':
        actors = models.Actor.query.order_by(models.Actor.best_genre)
    elif sort == 'voice':
        actors = models.Actor.query.order_by(models.Actor.voice_range)
    else:
        actors = models.Actor.query.join(models.Employee).order_by(models.Employee.name)

    for actor in actors:
        a = dict()
        a['name'] = str(models.Employee.query.get(actor.employee_id).name)
        a['genre'] = str(models.Genre.query.get(actor.best_genre))
        a['voice'] = str(models.Voice.query.get(actor.voice_range))
        a['page_id'] = actors_page_dir + str(actor.employee_id)
        needed.append(a)

    return render_template('actors.html', title='Actors', actors=needed, sort_allowed=True)


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
